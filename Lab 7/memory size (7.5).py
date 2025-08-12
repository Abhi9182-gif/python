import numpy as np
# e. Find the memory size of a NumPy array
arr4 = np.array([1, 2, 3, 4, 5])
memory_size = arr4.size * arr4.itemsize
print("\ne. Memory Size in Bytes:", memory_size)
