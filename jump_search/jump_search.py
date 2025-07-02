import math

class JumpSearch:
    def __init__(self, data):
        self.__data = sorted(list(data))  # Jump Search cần dữ liệu được sắp xếp

    def __str__(self):
        return f"Danh sách (đã sắp xếp): {self.__data}"

    def search(self, target):
        n = len(self.__data)
        step = int(math.sqrt(n))
        prev = 0

        while prev < n and self.__data[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1

        for i in range(prev, min(step, n)):
            if self.__data[i] == target:
                return i

        return -1
