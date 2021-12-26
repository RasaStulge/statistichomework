# TASK 4
# Create an array with six random values between 10 and 30.

from numpy import random

x=random.randint(10, 30, size=(6))
print(x)