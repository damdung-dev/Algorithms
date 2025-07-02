class InterpolationSearch:
    def __init__(self, data):
        self.__data = sorted(list(data))

    def __str__(self):
        return f"Danh sách (đã sắp xếp): {self.__data}"

    def search(self, target):
        low = 0
        high = len(self.__data) - 1

        while low <= high and target >= self.__data[low] and target <= self.__data[high]:
            if self.__data[high] == self.__data[low]:
                break

            pos = low + ((high - low) * (target - self.__data[low])) // (self.__data[high] - self.__data[low])

            if pos >= len(self.__data):
                return -1

            if self.__data[pos] == target:
                return pos
            if self.__data[pos] < target:
                low = pos + 1
            else:
                high = pos - 1

        return -1
