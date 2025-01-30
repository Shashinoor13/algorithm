from typing import List
from base_sort import BaseSorter

class QuickSort(BaseSorter):
    def __init__(self):
        super().__init__("Quick Sort")
    
    def _quick_sort(self, arr: List[int], low: int, high: int):
        if low < high:
            pivot_idx = self._partition(arr, low, high)
            self._quick_sort(arr, low, pivot_idx - 1)
            self._quick_sort(arr, pivot_idx + 1, high)
    
    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def sort(self, arr: List[int]) -> List[int]:
        self._quick_sort(arr, 0, len(arr) - 1)
        return arr