import unittest

from src.pipeline.pipeline import Pipeline
from src.pipeline.steps import (
    CleanStep,
    FilterStep,
    NormalizeStep,
    PrefixStep,
)


class TestPipeline(unittest.TestCase):

    def test_pipeline_runs_steps_in_sequence(self):
        data = [" Alice ", "", "Bob", " Charlie "]

        pipeline = Pipeline([
            CleanStep(),
            FilterStep(),
            NormalizeStep()
        ])

        result = pipeline.run(data)

        self.assertEqual(
            result,
            ["alice", "charlie"]
        )

    def test_pipeline_can_use_different_step(self):
        data = [" Alice ", " Bob "]

        pipeline = Pipeline([
            CleanStep(),
            PrefixStep()
        ])

        result = pipeline.run(data)

        self.assertEqual(
            result,
            ["USER: Alice", "USER: Bob"]
        )


if __name__ == "__main__":
    unittest.main()