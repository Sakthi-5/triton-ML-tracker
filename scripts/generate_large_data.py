import csv

output_file = "data/raw/large_data.csv"
num_records = 1_000_000

with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["id", "name", "score"])

    for i in range(1, num_records + 1):
        writer.writerow([i, f"User{i}", i % 100])

print(f"Generated {num_records:,} records.")