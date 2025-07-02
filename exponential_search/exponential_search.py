class ExponentialSearch:
    def __init__(self, data):
        self.__data = sorted(list(data))

    def __str__(self):
        return f"Danh sách (đã sắp xếp): {self.__data}"

    def binary_search(self, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if self.__data[mid] == target:
                return mid
            elif self.__data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, target):
        if self.__data[0] == target:
            return 0
        i = 1
        while i < len(self.__data) and self.__data[i] <= target:
            i *= 2
        return self.binary_search(i // 2, min(i, len(self.__data)-1), target)
