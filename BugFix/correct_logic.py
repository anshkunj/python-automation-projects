"""
Correct logic: sum of even numbers
"""
def sum_even(lst):
    return sum(x for x in lst if x % 2 == 0)

# Example usage
# print(sum_even([1,2,3,4]))