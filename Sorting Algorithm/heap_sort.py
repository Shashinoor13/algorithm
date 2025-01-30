from typing import List
from base_sort import BaseSorter


class HeapSort(BaseSorter):
    def __init__(self):
        super().__init__("Heap Sort")
    
    def _heapify(self, arr: List[int], n: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)
    
    def sort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self._heapify(arr, i, 0)
        return arr
