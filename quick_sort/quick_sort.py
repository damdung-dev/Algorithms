class QuickSort:
    def __init__(self, elements):
        self.__elements = list(elements)  # Chuyển về list để dễ xử lý

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, elements):
        self.__elements = list(elements)

    def sort(self):
        self.__elements = self._quick_sort(self.__elements)

    def _quick_sort(self, array):
        if len(array) <= 1:
            return array

        pivot = array[0]
        less = [compare for compare in array[1:] if compare <= pivot]
        greater = [compare for compare in array[1:] if compare > pivot]

        return self._quick_sort(less) + [pivot] + self._quick_sort(greater)
