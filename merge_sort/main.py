from merge_sort import MergeSort
from numpy import random
import numpy as np

user=input("Type in your order:\n1. increase\n2. decrease\nYour choice: ")
sorter = MergeSort(np.array(random.randint(1,1000,5)),user)
print("Original:", sorter.elements)
sorter.sort()
print("Sorted:", np.array(sorter.elements))
