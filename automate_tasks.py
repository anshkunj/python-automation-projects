"""
Example of simple automation: log a message every 5 seconds.
"""
import time

def auto_task():
    for i in range(5):
        print(f"Task run {i+1}")
        time.sleep(5)

# Example usage
# auto_task()