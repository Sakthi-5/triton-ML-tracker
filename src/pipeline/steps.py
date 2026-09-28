from src.pipeline.step import Step


class CleanStep(Step):

    def process(self, data):
        return [item.strip() for item in data if item.strip()]
class FilterStep(Step):

    def process(self, data):
        return [item for item in data if len(item) >= 5]
class NormalizeStep(Step):

    def process(self, data):
        return [item.lower() for item in data]
class UpperCaseStep(Step):

    def process(self, data):
        return [item.upper() for item in data]
class PrefixStep(Step):

    def process(self, data):
        return [f"USER: {item}" for item in data]