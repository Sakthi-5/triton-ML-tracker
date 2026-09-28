from src.data.data_iterator import DataIterator

iterator = DataIterator("data/raw/sample_data.csv")

for record in iterator:
    print(record)