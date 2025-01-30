from base_sort import BaseSorter
from typing import List

class InsertionSort(BaseSorter):
    def __init__(self):
        super().__init__("Insertion Sort")
    
    def sort(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr