import unittest

from src.data.data_iterator import DataIterator


class TestDataIterator(unittest.TestCase):

    def test_iterator_skips_header(self):
        iterator = DataIterator("data/raw/sample_data.csv")

        first_record = next(iterator)

        self.assertEqual(first_record, "1,Alice,85")

        iterator.close()

    def test_iterator_returns_all_records(self):
        iterator = DataIterator("data/raw/sample_data.csv")

        records = list(iterator)

        self.assertEqual(len(records), 5)

    def test_iterator_stops_at_end(self):
        iterator = DataIterator("data/raw/sample_data.csv")

        for _ in range(5):
            next(iterator)

        with self.assertRaises(StopIteration):
            next(iterator)


if __name__ == "__main__":
    unittest.main()