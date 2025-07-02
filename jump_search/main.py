from jump_search import JumpSearch

print("=== Jump Search ===")
data = [1, 3, 5, 7, 9, 11, 13]
js = JumpSearch(data)
print(js)
print("Tìm 7:", js.search(7))
