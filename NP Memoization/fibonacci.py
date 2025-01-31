import time
import matplotlib.pyplot as plt

def fibonacci_normal(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_normal(n-1) + fibonacci_normal(n-2)

def fibonacci_memoization(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]

def fibonacci_tabulation(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def measure_time(func, n: int, *args) -> float:
    start_time = time.time()
    func(n, *args)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds

# Test range
n_values = range(0, 35, 5)  # Testing up to n=30 to avoid excessive computation time

# Measure execution times
normal_times = []
memo_times = []
tab_times = []

for n in n_values:
    # Normal recursion
    normal_time = measure_time(fibonacci_normal, n)
    normal_times.append(normal_time)
    
    # Memoization
    memo_time = measure_time(fibonacci_memoization, n, {})
    memo_times.append(memo_time)
    
    # Tabulation
    tab_time = measure_time(fibonacci_tabulation, n)
    tab_times.append(tab_time)

# Create visualization
plt.figure(figsize=(12, 6))
plt.plot(n_values, normal_times, 'r-o', label='Normal Recursion')
plt.plot(n_values, memo_times, 'g-o', label='Memoization')
plt.plot(n_values, tab_times, 'b-o', label='Tabulation')

plt.title('Fibonacci Implementation Performance Comparison')
plt.xlabel('n-th Fibonacci Number')
plt.ylabel('Execution Time (milliseconds)')
plt.grid(True)
plt.legend()

# Print sample values
print("\nSample execution times for n=20:")
print(f"Normal Recursion: {measure_time(fibonacci_normal, 20):.4f} ms")
print(f"Memoization: {measure_time(fibonacci_memoization, 20, {}):.4f} ms")
print(f"Tabulation: {measure_time(fibonacci_tabulation, 20):.4f} ms")

plt.yscale('log')  # Using log scale for better visualization
plt.show()