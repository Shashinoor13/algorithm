import matplotlib.pyplot as plt
from quick_sort import QuickSort
from heap_sort import HeapSort
from merge_sort import MergeSort
from selection_sort import SelectionSort
from insertion_sort import InsertionSort


def run_comparison():
    # Initialize all sorters
    sorters = [
        QuickSort(),
        HeapSort(),
        MergeSort(),
        SelectionSort(),
        InsertionSort()
    ]
    
    # Run performance measurements for each sorter
    for sorter in sorters:
        print(f"Running tests for {sorter.name}...")
        sorter.measure_performance()
    
    # Prepare data for plotting
    sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000]
    plt.figure(figsize=(12, 8))
    
    for sorter in sorters:
        avg_times = [sorter.get_average_times()[size] for size in sizes]
        plt.plot(sizes, avg_times, marker='o', label=sorter.name)
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Array Size')
    plt.ylabel('Average Time (milliseconds)')
    plt.title('Sorting Algorithm Performance Comparison')
    plt.grid(True)
    plt.legend()
    plt.savefig('sorting_comparison.png')
    plt.close()
    
    # Print numerical results
    print("\nNumerical Results (Average time in milliseconds):")
    print("Size:", end="\t")
    for size in sizes:
        print(f"{size}", end="\t")
    print()
    
    for sorter in sorters:
        print(f"{sorter.name}:", end="\t")
        for size in sizes:
            print(f"{sorter.get_average_times()[size]:.2f}", end="\t")
        print()

if __name__ == "__main__":
    run_comparison()