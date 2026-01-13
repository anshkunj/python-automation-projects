"""
Remove duplicate rows from CSV
"""
import pandas as pd

def remove_duplicates(file_in, file_out):
    df = pd.read_csv(file_in)
    df.drop_duplicates(inplace=True)
    df.to_csv(file_out, index=False)

# Example usage
# remove_duplicates('data.csv', 'data_nodup.csv')