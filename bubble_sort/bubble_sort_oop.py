import random
class BubbleSort:
    list_number=[]
    def __init__(self, data):
        self.data=data
    def create_list(self):
        BubbleSort.list_number.append(self.data)
    def find_and_sort(self):
        while True:
            swapped = False
            for i in range(0, len(BubbleSort.list_number) - 1):
                if BubbleSort.list_number[i] > BubbleSort.list_number[i + 1]:
                    temp = BubbleSort.list_number[i + 1]
                    BubbleSort.list_number[i + 1] = BubbleSort.list_number[i]
                    BubbleSort.list_number[i] = temp
                    swapped = True
                else:
                    continue
            if not swapped:
                break
        return BubbleSort.list_number
