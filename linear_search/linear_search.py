class LinearSearch:
    def __init__(self, data):
        self.__data = list(data)

    def __str__(self):
        return f"Danh sách: {self.__data}"

    def search(self, target):
        for search in range(len(self.__data)):
            if self.__data[search] == target:
                return seach
        return -1
