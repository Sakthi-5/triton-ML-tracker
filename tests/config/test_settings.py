import unittest
from pathlib import Path

from pydantic import ValidationError

from src.config.settings import PipelineConfig


class TestPipelineConfig(unittest.TestCase):

    def test_valid_config(self):
        config = PipelineConfig(
            data_path=Path("data/raw/sample_data.csv"),
            batch_size=32,
            image_size=224,
            mode="train",
            device="cpu",
            threshold=0.8,
        )

        self.assertEqual(config.batch_size, 32)
        self.assertEqual(config.mode, "train")

    def test_invalid_batch_size(self):
        with self.assertRaises(ValidationError):
            PipelineConfig(
                data_path=Path("data/raw/sample_data.csv"),
                batch_size=0,
                image_size=224,
                mode="train",
                device="cpu",
                threshold=0.8,
            )

    def test_invalid_mode(self):
        with self.assertRaises(ValidationError):
            PipelineConfig(
                data_path=Path("data/raw/sample_data.csv"),
                batch_size=32,
                image_size=224,
                mode="testing",
                device="cpu",
                threshold=0.8,
            )

    def test_invalid_data_path(self):
        with self.assertRaises(ValidationError):
            PipelineConfig(
                data_path=Path("data/raw/does_not_exist.csv"),
                batch_size=32,
                image_size=224,
                mode="train",
                device="cpu",
                threshold=0.8,
            )


if __name__ == "__main__":
    unittest.main()