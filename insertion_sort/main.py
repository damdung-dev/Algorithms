from insertion_sort import InsertionSort
import numpy as np

data=np.array([64, 25, 12, 22, 11])
print("Original:",data)
data = InsertionSort(data)

data.sort()
print(data.__str__())

