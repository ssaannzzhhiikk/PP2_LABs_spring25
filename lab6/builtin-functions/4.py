import time
import math


def invoke_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")


# 25100 2123


num = int(input())
tm = int(input())
invoke_square_root(num, tm)
