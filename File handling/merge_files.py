"""
Merge multiple text files into one
"""
import os

def merge_files(folder, output_file):
    with open(output_file, 'w') as outfile:
        for fname in os.listdir(folder):
            if fname.endswith('.txt'):
                with open(os.path.join(folder, fname)) as infile:
                    outfile.write(infile.read() + "\n")

# Example usage
# merge_files('texts', 'all.txt')