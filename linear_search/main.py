from linear_search import LinearSearch

data = [5, 3, 7, 1, 9, 4]

print("=== Linear Search ===")
ls = LinearSearch(data)
print(ls)
target = 7
result = ls.search(target)
print(f"Vị trí của {target}: {result}" if result != -1 else f"{target} không tồn tại.")