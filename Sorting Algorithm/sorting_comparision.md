# Sorting Algorithm Comparison

This repository compares the performance of various sorting algorithms, including QuickSort, HeapSort, MergeSort, SelectionSort, and InsertionSort.

## Algorithms
1. **QuickSort**: Divide-and-conquer algorithm with `O(n log n)` average time complexity.
2. **HeapSort**: Uses a binary heap to sort elements with `O(n log n)` time complexity.
3. **MergeSort**: Divide-and-conquer algorithm with stable sorting and `O(n log n)` time complexity.
4. **SelectionSort**: Simple algorithm with `O(n^2)` time complexity.
5. **InsertionSort**: Efficient for small datasets with `O(n^2)` time complexity.

## Performance Comparison
The performance of all algorithms is compared for different array sizes. The results are visualized in the following plot:

- **`sorting_comparison.png`**: A comparison of execution times for all sorting algorithms.

## How to Run
1. Clone the repository.
2. Run the `main.py` script:
   ```bash
   python main.py