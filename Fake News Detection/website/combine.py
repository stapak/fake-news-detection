import csv
import random

def shuffle_and_combine_csv(file1, file2, output_file):
    rows = []

    # Read the first CSV file and store the rows
    with open(file1, 'r', newline='', encoding='utf-8') as f1:
        reader1 = csv.reader(f1)
        header1 = next(reader1)  # Read the header
        for row in reader1:
            rows.append(row)
    
    # Read the second CSV file and store the rows
    with open(file2, 'r', newline='', encoding='utf-8') as f2:
        reader2 = csv.reader(f2)
        header2 = next(reader2)  # Read the header
        for row in reader2:
            rows.append(row)

    # Ensure headers from both files match
    if header1 != header2:
        raise ValueError("CSV files have different headers")

    # Shuffle the combined rows
    random.shuffle(rows)

    # Write the shuffled rows to the output CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as out:
        writer = csv.writer(out)
        writer.writerow(header1)  # Write the header
        writer.writerows(rows)

# Usage
file1 = 'Fake.csv'
file2 = 'True.csv'
output_file = 'train.csv'

shuffle_and_combine_csv(file1, file2, output_file)
