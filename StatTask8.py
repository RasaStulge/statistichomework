# TASK 8
# Create any array of values and then normalize them - i.e. from
# each element of the array subtract the mean and divide by the
# standard deviation.

import numpy as np
import numpy as ppool

arr = np.array([23, 45, 112, 150, 43, 254, 95, 8])
print(arr)
norm = np.linalg.norm(arr)
print(norm)
normalized_array = arr/norm
print(normalized_array)

mean_array = np.mean(normalized_array)
std_array = np.std(normalized_array)