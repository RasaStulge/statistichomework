# TASK 6
# Create the 4X4 matrix below, then:
# Display the item from the second row and the third column,
# calculate its determinant
# calculate its trace (the sum of elements on the main diagonal),
# find the largest and smallest item.

import numpy as np

arr = np.array([1,15,4,13,8,21,3,12,11,13,11,5,32,13,0,2])
new_arr = arr.reshape(4,4)
print(new_arr)
print(new_arr.item((1,2)))

det = np.linalg.det(new_arr)
print(det)

trace = np.trace(np.eye(4))
print(trace)
print(arr.min())
print(arr.max())