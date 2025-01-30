from base_sort import BaseSorter
from typing import List

class SelectionSort(BaseSorter):
    def __init__(self):
        super().__init__("Selection Sort")
    
    def sort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
