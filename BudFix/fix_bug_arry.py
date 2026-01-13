"""
Fix common array index errors
"""
def fix_index(arr, index):
    if 0 <= index < len(arr):
        return arr[index]
    else:
        return None

# Example usage
# arr = [10,20,30]
# print(fix_index(arr, 2))
