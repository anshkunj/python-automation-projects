"""
Simple stopwatch
"""
import time

def stopwatch(seconds):
    for i in range(seconds):
        print(f"{i+1} seconds")
        time.sleep(1)

# Example usage
# stopwatch(5)
