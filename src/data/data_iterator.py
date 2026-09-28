class DataIterator:

    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, "r")

        # Skip the CSV header
        self.file.readline()

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