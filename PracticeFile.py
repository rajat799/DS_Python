"""
import numpy as np

# creating a 5X5 matrix of all 1's
matrix = np.ones((5, 5), dtype=int)
print(matrix)

# change border elements to 0
matrix[0, :] = 0
matrix[-1:] = 0
matrix[:, 0] = 0
matrix[:, -1] = 0

print(matrix)
"""

"""
import numpy as np
matrix = np.identity(3)
print(matrix)
"""

"""

import numpy as np

arr = np.arange(10, 51, 5)

print(arr)
"""

import numpy as np

matrix = np.random.randint(1, 101, size=(4, 4))

mean = np.mean(matrix)

print("random 4x4 matrix: \n", matrix)

print("mean of the matrix \n", mean)