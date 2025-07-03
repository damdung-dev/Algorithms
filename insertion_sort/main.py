from insertion_sort import InsertionSort
import numpy as np
from numpy import random

user=int(input("Please input a number: "))
data=np.array(random.randint(1,1000,user))
print("Original:",data)
data = InsertionSort(data)
data.sort()
print(data.__str__())

