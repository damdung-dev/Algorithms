from merge_sort import MergeSort

arr = [5, 2, 9, 1, 5, 6]
sorter = MergeSort(arr)

print("Original:", sorter.elements)
sorter.sort()
print("Sorted:", sorter.elements)
