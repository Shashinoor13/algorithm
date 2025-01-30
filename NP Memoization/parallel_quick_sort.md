# Parallel QuickSort

This repository implements and compares the performance of sequential and parallel versions of the QuickSort algorithm.

## Problem Description
QuickSort is a popular sorting algorithm that uses a divide-and-conquer approach. This project explores the benefits of parallelizing QuickSort using Python's multiprocessing module.

## Approaches
1. **Sequential QuickSort**:
   - Traditional implementation with `O(n log n)` average time complexity.
   - Efficient but limited to single-threaded execution.

2. **Parallel QuickSort**:
   - Uses multiprocessing to sort partitions in parallel.
   - Achieves speedup for large datasets by leveraging multiple CPU cores.

## Performance Comparison
The performance of both implementations is compared for different array sizes. The results are visualized in the following plots:

- **`quicksort_time_comparison.png`**: A comparison of execution times for sequential and parallel QuickSort.
- **`quicksort_speedup.png`**: A plot showing the speedup achieved by the parallel implementation.

## How to Run
1. Clone the repository.
2. Run the `parallel_quick_sort.py` script:
   ```bash
   python parallel_quick_sort.py