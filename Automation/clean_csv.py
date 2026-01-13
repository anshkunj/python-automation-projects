"""
Clean CSV file by removing empty rows and columns.
"""
import csv

def clean_csv(input_file, output_file):
    with open(input_file, newline='') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if any(cell.strip() for cell in row)]
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

# Example usage
# clean_csv('data.csv', 'data_clean.csv')
