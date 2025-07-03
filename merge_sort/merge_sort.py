class MergeSort:
    def __init__(self, elements, order):
        self.__elements = elements
        self.__order = order

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, elements):
        self.__elements = elements

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    def sort(self):
        self.__elements = self._merge_sort(self.__elements)

    def _merge_sort(self, array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left = self._merge_sort(array[:mid])
        right = self._merge_sort(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        compare = scan = 0
        if self.order=="1":
            while compare < len(left) and scan < len(right):
                if left[compare] < right[scan]:
                    result.append(left[compare])
                    compare += 1
                else:
                    result.append(right[scan])
                    scan += 1

            result.extend(left[compare:])
            result.extend(right[scan:])
            return result
        elif self.order=="2":
            while compare < len(left) and scan < len(right):
                if left[compare] > right[scan]:
                    result.append(left[compare])
                    compare += 1
                else:
                    result.append(right[scan])
                    scan += 1

            result.extend(left[compare:])
            result.extend(right[scan:])
            return result
        else:
            print("Invalid choice")