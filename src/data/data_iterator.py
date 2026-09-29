from pathlib import Path

from src.exceptions.errors import DataValidationError


class DataIterator:

    def __init__(self, file_path):
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            raise DataValidationError(
                f"Data loading failed at '{self.file_path}': "
                "file does not exist"
            )

        if not self.file_path.is_file():
            raise DataValidationError(
                f"Data loading failed at '{self.file_path}': "
                "path is not a file"
            )

        try:
            self.file = open(self.file_path, "r")
            self.file.readline()
        except OSError as error:
            raise DataValidationError(
                f"Data loading failed at '{self.file_path}': "
                f"unable to open file: {error}"
            ) from error

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()

        if line == "":
            self.file.close()
            raise StopIteration

        return line.strip()

    def close(self):
        self.file.close()