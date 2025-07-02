class SelectionSort:
    def __init__(self,elements):
        self.__elements=elements
    @property
    def elements(self):
        return self.__elements
    @elements.setter
    def elements(self,elements):
        self.__elements=elements

    def sort(self):
        for compare in range(len(self.elements)):
            min_index = compare
            for scan in range(compare + 1, len(self.elements)):
                if self.elements[scan] < self.elements[min_index]:
                    min_index = scan
            self.elements[compare], self.elements[min_index] = self.elements[min_index], self.elements[compare]
        return self.elements
    
    def __str__(self):
        return f"Mảng sau khi sắp xếp là: {self.elements}"