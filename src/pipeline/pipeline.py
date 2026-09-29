import logging

from src.exceptions.errors import ProcessingError
from src.utils.decorators import retry, timeit


logger = logging.getLogger(__name__)


class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    @timeit
    @retry(max_attempts=3)
    def run(self, data):
        logger.info(
            "pipeline started",
            extra={"records": len(data)},
        )

        for step in self.steps:
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

        logger.info(
            "pipeline completed",
            extra={"records": len(data)},
        )

        return data