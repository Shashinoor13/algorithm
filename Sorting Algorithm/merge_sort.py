from base_sort import BaseSorter
from typing import List

class MergeSort(BaseSorter):
    def __init__(self):
        super().__init__("Merge Sort")
    
    def _merge(self, arr: List[int], left: int, mid: int, right: int):
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    def _merge_sort(self, arr: List[int], left: int, right: int):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(arr, left, mid)
            self._merge_sort(arr, mid + 1, right)
            self._merge(arr, left, mid, right)
    
    def sort(self, arr: List[int]) -> List[int]:
        self._merge_sort(arr, 0, len(arr) - 1)
        return arr