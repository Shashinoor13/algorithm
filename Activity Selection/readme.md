# Activity Selection Problem

This repository contains the implementation and analysis of the Activity Selection problem using both Greedy and Brute Force approaches.

## Problem Description
Given a set of activities with their start and finish times, the goal is to select the maximum number of activities that can be performed by a single person, assuming that a person can only work on one activity at a time.

## Approaches
1. **Greedy Approach**: 
   - Time Complexity: `O(n log n)` (due to sorting).
   - Selects activities based on the earliest finish time.
   - Efficient and optimal for this problem.

2. **Brute Force Approach**:
   - Time Complexity: `O(2^n)`.
   - Checks all possible combinations of activities to find the maximum non-overlapping subset.
   - Inefficient for large inputs but guarantees correctness.

## Performance Comparison
The performance of both approaches is compared using randomly generated test cases. The results are visualized in the following plots:

- **`activity_selection.png`**: An example visualization of a schedule with 5 activities.
- **`performance_comparison.png`**: A comparison of execution times for the Greedy and Brute Force approaches.

## How to Run
1. Clone the repository.
2. Run the `activity_selection.py` script:
   ```bash
   python activity_selection.py