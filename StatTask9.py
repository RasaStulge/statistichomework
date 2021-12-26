# TASK 9
# Create a function that takes two vectors (both with the same
# dimensions) as a numpy array and returns the Euclidean distance between them.
# https://www.educative.io/cdn-cgi/image/f=auto,fit=contain,w=3000/api/edpresso/shot/5811083295588352/image/6620922867351552.png

import numpy as np

array_1 = np.array([1,2,3,4,5])
array_2 = np.array([6,7,8,9,10])

# Euclidean distance

temp = array_1 - array_2
distance = np.linalg.norm(temp)

print("Euclidean distance:", distance)