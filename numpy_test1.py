import numpy as np

a = np.arange(6)
a2 = a[np.newaxis, :]
a2.shape
print(a2)

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

print(array_example.ndim)
