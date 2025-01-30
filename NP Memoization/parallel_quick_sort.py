import random
import time
import matplotlib.pyplot as plt
from multiprocessing import Pool
import numpy as np

def sequential_quicksort(arr):
    """Traditional sequential quicksort implementation"""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return sequential_quicksort(left) + middle + sequential_quicksort(right)

def parallel_partition(arr, pivot):
    """Helper function for parallel quicksort"""
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left, middle, right

def parallel_quicksort(arr, pool=None):
    """Parallel quicksort implementation using multiprocessing"""
    if len(arr) <= 1:
        return arr
    
    if pool is None:
        # Create a pool for the top-level call
        with Pool() as pool:
            return parallel_quicksort(arr, pool)
    
    if len(arr) <= 10000:
        return sequential_quicksort(arr)
    
    pivot = arr[len(arr) // 2]
    left, middle, right = parallel_partition(arr, pivot)
    
    # Recursively sort left and right partitions in parallel
    left_sorted, right_sorted = pool.map(
        sequential_quicksort, 
        [left, right]
    )
    
    return left_sorted + middle + right_sorted

def measure_sorting_time(sort_func, arr, **kwargs):
    """Measure the execution time of a sorting function"""
    start_time = time.time()
    sorted_arr = sort_func(arr.copy(), **kwargs)
    end_time = time.time()
    return (end_time - start_time) * 1000

def generate_random_array(size):
    """Generate a random array of given size"""
    return [random.randint(0, 1000) for _ in range(size)]

def run_sorting_comparison():
    """Main function to run the sorting comparison"""
    sizes = [1000, 5000, 10000, 50000, 100000]
    trials = 3 

    # Results storage
    sequential_times = []
    parallel_times = []
    sequential_std = []
    parallel_std = []

    # Run experiments
    for size in sizes:
        print(f"\nTesting with array size: {size}")
        
        size_sequential_times = []
        size_parallel_times = []
        
        for trial in range(trials):
            # Generate the same random array for both algorithms
            arr = generate_random_array(size)
            
            # Measure sequential quicksort
            seq_time = measure_sorting_time(sequential_quicksort, np.array(arr))
            size_sequential_times.append(seq_time)
            print(f"Sequential Trial {trial + 1}: {seq_time:.2f}ms")
            
            # Measure parallel quicksort
            par_time = measure_sorting_time(parallel_quicksort, np.array(arr))
            size_parallel_times.append(par_time)
            print(f"Parallel Trial {trial + 1}: {par_time:.2f}ms")
        
        # Calculate average and standard deviation
        sequential_times.append(np.mean(size_sequential_times))
        parallel_times.append(np.mean(size_parallel_times))
        sequential_std.append(np.std(size_sequential_times))
        parallel_std.append(np.std(size_parallel_times))

    # Plotting time comparison
    plt.figure(figsize=(12, 6))
    plt.errorbar(sizes, sequential_times, yerr=sequential_std, fmt='o-', 
                label='Sequential Quicksort', capsize=5, color='blue')
    plt.errorbar(sizes, parallel_times, yerr=parallel_std, fmt='o-', 
                label='Parallel Quicksort', capsize=5, color='red')
    plt.title('Sequential vs Parallel Quicksort Performance Comparison')
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (milliseconds)')
    plt.grid(True)
    plt.legend()
    plt.savefig('quicksort_time_comparison.png')
    plt.close()

    # Plotting speedup
    plt.figure(figsize=(12, 6))
    speedups = np.array(sequential_times) / np.array(parallel_times)
    plt.plot(sizes, speedups, 'go-', label='Speedup Factor')
    plt.title('Parallel Quicksort Speedup over Sequential Version')
    plt.xlabel('Array Size')
    plt.ylabel('Speedup Factor (Sequential Time / Parallel Time)')
    plt.grid(True)
    plt.legend()
    plt.savefig('quicksort_speedup.png')
    plt.close()

    # Print detailed results
    print("\nDetailed Results:")
    print("\nArray Size | Sequential (ms) | Parallel (ms) | Speedup")
    print("-" * 50)
    for i, size in enumerate(sizes):
        print(f"{size:9d} | {sequential_times[i]:13.2f} | {parallel_times[i]:11.2f} | {speedups[i]:.2f}x")

    # Save numerical results to a file
    with open('quicksort_results.txt', 'w') as f:
        f.write("Array Size | Sequential (ms) | Parallel (ms) | Speedup\n")
        f.write("-" * 50 + "\n")
        for i, size in enumerate(sizes):
            f.write(f"{size:9d} | {sequential_times[i]:13.2f} | {parallel_times[i]:11.2f} | {speedups[i]:.2f}x\n")

if __name__ == '__main__':
    run_sorting_comparison()