"""
Rename multiple files in a folder with a prefix.
"""
import os

def rename_files(folder, prefix):
    for count, filename in enumerate(os.listdir(folder)):
        new_name = f"{prefix}_{count+1}{os.path.splitext(filename)[1]}"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

# Example usage
# rename_files('my_folder', 'Project')