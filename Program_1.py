import numpy as np

arr1 = np.array([10, 20, 30, 49, 50])
arr2 = np.array([[1, 2], [3, 4]])

print("1D Array: ", arr1)
print("2D Array: \n", arr2)

# array properties
print("Shape: ", arr1.shape)  # to check how many elements are there in array
print("Datatype: ", arr1.dtype)  # used to check the datatype of the array elements
print("size: ", arr2.size)  # to check the size of the array (n)

# array operations
print("add 5 to arr1: ", arr1 + 5)  # add 5 in all elements of the array
print("multiply arr1 by 2: ", arr1 * 2)  # multiply 2 by all elements in array

arr3 = np.array([10, 15, 20, 25])
arr4 = np.array([1, 1, 1, 1])

print("Element wise addition: ", arr3 + arr4)

# Indexing and slicing
print("First element of arr1: ", arr1[0])
print("slice arr1: ", arr1[1:])




