from binary_search import BinarySearch

data = [5, 3, 7, 1, 9, 4]

print("\n=== Binary Search ===")
bs = BinarySearch(data)
print(bs)
target = 4
result = bs.search(target)
print(f"Vị trí của {target}: {result}" if result != -1 else f"{target} không tồn tại.")

