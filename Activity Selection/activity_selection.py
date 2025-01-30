import time
import matplotlib.pyplot as plt
from itertools import combinations
import random

def activity_selection_greedy(start_times, finish_times):
    """
    Greedy approach for activity selection.
    Time Complexity: O(n log n) due to initial sorting
    """
    n = len(start_times)
    # Create list of activities with their start and finish times
    activities = list(zip(range(n), start_times, finish_times))
    # Sort activities by finish time
    activities.sort(key=lambda x: x[2])
    
    selected = [activities[0][0]]  # Select first activity
    last_finish = activities[0][2]
    
    for i in range(1, n):
        if activities[i][1] >= last_finish:
            selected.append(activities[i][0])
            last_finish = activities[i][2]
            
    return selected

def activity_selection_bruteforce(start_times, finish_times):
    """
    Brute force approach checking all possible combinations.
    Time Complexity: O(2^n)
    """
    n = len(start_times)
    activities = list(range(n))
    max_activities = []
    max_count = 0
    
    # Try all possible combinations of activities
    for r in range(1, n + 1):
        for combination in combinations(activities, r):
            # Check if this combination is valid (no overlapping)
            valid = True
            for i in range(len(combination)):
                for j in range(i + 1, len(combination)):
                    if (start_times[combination[i]] < finish_times[combination[j]] and 
                        finish_times[combination[i]] > start_times[combination[j]]):
                        valid = False
                        break
                if not valid:
                    break
            
            if valid and len(combination) > max_count:
                max_count = len(combination)
                max_activities = list(combination)
    
    return max_activities

def generate_test_case(n):
    """Generate random test case with n activities."""
    activities = []
    current_time = 0
    
    for _ in range(n):
        start = current_time + random.randint(0, 3)
        duration = random.randint(1, 5)
        finish = start + duration
        activities.append((start, finish))
        current_time = start
    
    return zip(*activities)

def measure_time(func, *args):
    """Measure execution time of a function."""
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return (end_time - start_time) * 1000, result

sizes = range(2, 11)  # Test with up to 10 activities
greedy_times = []
bruteforce_times = []

for size in sizes:
    # Generate test case
    start_times, finish_times = generate_test_case(size)
    
    # Measure greedy approach
    greedy_time, greedy_result = measure_time(activity_selection_greedy, start_times, finish_times)
    greedy_times.append(greedy_time)
    
    # Measure brute force approach
    bruteforce_time, bruteforce_result = measure_time(activity_selection_bruteforce, start_times, finish_times)
    bruteforce_times.append(bruteforce_time)
    
    # Print results for this size
    print(f"\nSize {size}:")
    print(f"Greedy solution: {greedy_result} (Time: {greedy_time:.4f}ms)")
    print(f"Brute force solution: {bruteforce_result} (Time: {bruteforce_time:.4f}ms)")

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(sizes, greedy_times, 'g-o', label='Greedy')
plt.plot(sizes, bruteforce_times, 'r-o', label='Brute Force')

plt.title('Activity Selection: Greedy vs Brute Force Performance')
plt.xlabel('Number of Activities')
plt.ylabel('Execution Time (milliseconds)')
plt.grid(True)
plt.legend()
plt.yscale('log')  # Using log scale due to large difference in times

# Save the plot
plt.savefig('performance_comparison.png')

# Add example problem visualization for n=5
plt.figure(figsize=(12, 6))
start_times, finish_times = generate_test_case(5)
activities = list(zip(range(5), start_times, finish_times))

for i, (start, finish) in enumerate(zip(start_times, finish_times)):
    plt.plot([start, finish], [i, i], 'b-', linewidth=2)
    plt.plot(start, i, 'go', markersize=8)
    plt.plot(finish, i, 'ro', markersize=8)

plt.title('Example Activity Schedule (n=5)')
plt.xlabel('Time')
plt.ylabel('Activity Number')
plt.grid(True)

# Save the example problem visualization
plt.savefig('activity_selection.png')
plt.show()