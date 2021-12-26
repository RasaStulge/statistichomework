# TASK 3
# Create a 3X3 matrix (by using reshape) with values between 2 and 10.

import numpy as np

array_a = np.array([(2, 3, 4), (5, 6, 7), (8, 9, 10)])
print(array_a.shape)
print(array_a.size)

array_b = array_a.reshape(3,3)
print(array_b)

# reshape by Terminal and not run the function because its not printing result on pycharm with:  python3 StatTask3.py
