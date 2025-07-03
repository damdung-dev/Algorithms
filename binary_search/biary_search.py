class BinarySearch:
    def __init__(self, data):
        self.__data = sorted(list(data))  # Đảm bảo mảng đã được sắp xếp

    def __str__(self):
        return f"Danh sách (đã sắp xếp): {self.__data}"

    def search(self, target):
        left = 0
        right = len(self.__data) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.__data[mid] == target:
                return mid
            elif self.__data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
