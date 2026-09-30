from src.config.loader import load_config
from src.data.data_iterator import DataIterator
from src.exceptions.errors import (
    ConfigError,
    DataValidationError,
    ProcessingError,
)
from src.pipeline.pipeline import Pipeline



def demonstrate_config_error():
    try:
        load_config(
            data_path="data/raw/sample_data.csv",
            batch_size=0,
            image_size=224,
            mode="train",
            device="cpu",
            threshold=0.8,
        )
    except ConfigError as error:
        print("CONFIG ERROR:")
        print(error)
        print("Original cause:", error.__cause__)

def demonstrate_data_error():
    try:
        DataIterator("data/raw/missing.csv")
    except DataValidationError as error:
        print("\nDATA ERROR:")
        print(error)


def demonstrate_processing_error():
    class FailingStep:
        def process(self, data):
            raise ValueError("Invalid transformation")

    try:
        pipeline = Pipeline([FailingStep()])
        pipeline.run(["Alice"])
    except ProcessingError as error:
        print("\nPROCESSING ERROR:")
        print(error)


if __name__ == "__main__":
    demonstrate_config_error()
    demonstrate_data_error()
    demonstrate_processing_error()