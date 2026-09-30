import logging

from src.exceptions.errors import ProcessingError
from src.pipeline.step import Step
from src.utils.decorators import retry, timeit


logger = logging.getLogger(__name__)


class Pipeline:

    def __init__(self, steps: list[Step]):
        self.steps = steps

    @timeit
    @retry(max_attempts=3)
    def run(self, data):
        logger.info(
            "pipeline started",
            extra={"records": len(data)},
        )

        for step in self.steps:
            data = self._run_step(step, data)

        logger.info(
            "pipeline completed",
            extra={"records": len(data)},
        )

        return data

    def _run_step(self, step: Step, data):
        step_name = step.__class__.__name__

        logger.info(
            "pipeline step started",
            extra={
                "step": step_name,
                "records": len(data),
            },
        )

        try:
            data = step.process(data)

        except Exception as error:
            logger.exception(
                "pipeline step failed",
                extra={
                    "step": step_name,
                    "records": len(data),
                },
            )

            raise ProcessingError(
                f"Pipeline processing failed in "
                f"{step_name}: {error}"
            ) from error

        logger.info(
            "pipeline step completed",
            extra={
                "step": step_name,
                "records": len(data),
            },
        )

        return data