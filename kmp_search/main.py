from kmp_search import KMPSearch

print("\n=== KMP Search ===")
text = "ababcabcabababd"
pattern = "ababd"
kmp = KMPSearch(text)
print(kmp)
print(f"Tìm '{pattern}':", kmp.search(pattern))
