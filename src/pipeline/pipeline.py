from src.utils.decorators import timeit, retry


class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    @timeit
    @retry(max_attempts=3)
    def run(self, data):
        for step in self.steps:
            data = step.process(data)

        return data