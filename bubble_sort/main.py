from bubble_sort_oop import BubbleSort
import random

user=int(input("Nhập vào 1 số: "))
for i1 in range(0,user):
    newdata=BubbleSort(random.randint(1,100))
    newdata.create_list()
print(f"Dãy ban đầu: {BubbleSort.list_number}")
newdata.find_and_sort()
print(f"Dãy số sau khi sắp xếp: {BubbleSort.list_number}", end="")