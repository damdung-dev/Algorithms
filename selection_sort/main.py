from selection_sort import SelectionSort
import numpy as np

data=np.array([64, 25, 12, 22, 11])
print("Original:",data)
data = SelectionSort(data)

data.sort()
print(data.__str__())

