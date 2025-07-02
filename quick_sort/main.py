from quick_sort import QuickSort
import numpy as np

data=np.array([64, 25, 12, 22, 11])
print("Original:",data)
data = QuickSort(data)

data.sort()
print("Sorted array:",np.array(data.elements))

