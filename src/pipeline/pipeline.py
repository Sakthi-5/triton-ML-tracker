from src.exceptions.errors import ProcessingError
from src.utils.decorators import retry, timeit


class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    @timeit
    @retry(max_attempts=3)
    def run(self, data):
        for step in self.steps:
            try:
                data = step.process(data)
            except Exception as error:
                raise ProcessingError(
                    f"Pipeline processing failed in "
                    f"{step.__class__.__name__}: {error}"
                ) from error

        return data