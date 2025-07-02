class InsertionSort:
    def __init__(self,elements):
        self.__elements=elements
    @property
    def elements(self):
        return self.__elements
    @elements.setter
    def elements(self,elements):
        self.__elements=elements

    def sort(self):
        for compare in range(1, len(self.elements)):
            key = self.elements[compare]
            scan = compare - 1
            while scan >= 0 and self.elements[scan] > key:
                self.elements[scan + 1] = self.elements[scan]
                scan -= 1
            self.elements[scan + 1] = key
        return self.elements
    
    def __str__(self):
        return f"Mảng sau khi sắp xếp là: {self.elements}"
