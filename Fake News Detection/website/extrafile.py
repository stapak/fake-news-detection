import csv

def add_column_to_csv(input_file, output_file, new_column_name, default_value):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    # Add the new column name to the header
    header = rows[0]
    header.append(new_column_name)

    # Add the default value to each row
    for row in rows[1:]:
        row.append(default_value)

    # Write the updated rows to the output file
    with open(output_file, 'w', newline='',encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

# Usage
input_file = 'Fake.csv'
output_file = 'Fake.csv'
new_column_name = 'label'
default_value = 0

add_column_to_csv(input_file, output_file, new_column_name, default_value)
