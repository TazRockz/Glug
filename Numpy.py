# Working With The Numpy Library #
import numpy as np

arr0 = np.array('Ara Ara Sayonara!')
print ('\n', arr0)
print (f'The Dimension of the Above Array is {arr0.ndim}')


arr1 = np.array([1, 2, 3, 4, 5])
print('\n', arr1)
print (f'The Dimension of the Above Array is {arr1.ndim}')


arr2 = np.array ([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
print ('\n', arr2)
print (f'\nThe Dimension of the Above Array is {arr2.ndim}')

arr3 = np.array([[[1,2,3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print ('\n', arr3)
print (f'The Dimension of the Abouve Array is {arr3.ndim}')

arr10 = np.array([1, 2, 3, 4, 5], ndmin = 10)
print('\n', arr10)
print (f'The Dimension of the Above Array is {arr10.ndim}')


print ('\n', arr1[4])
print ('\n', arr2[1, 2])
