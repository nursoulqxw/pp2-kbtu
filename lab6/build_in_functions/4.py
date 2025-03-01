import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  # Convert ms to seconds
    print(f"Square root of {number} after {delay} milliseconds is {math.sqrt(number)}")

# Example usage
delayed_sqrt(25100, 2123)
