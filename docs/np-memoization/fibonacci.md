---
title: Fibonacci Sequence with Memoization
layout: default
---

# Fibonacci Sequence with Memoization

This repository explores different implementations of the Fibonacci sequence, including normal recursion, memoization, and tabulation.

## Problem Description
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The goal is to compute the nth Fibonacci number efficiently.

## Approaches
1. **Normal Recursion**:
   - Time Complexity: `O(2^n)`.
   - Simple but highly inefficient due to repeated calculations.

2. **Memoization**:
   - Time Complexity: `O(n)`.
   - Stores intermediate results to avoid redundant calculations.

3. **Tabulation**:
   - Time Complexity: `O(n)`.
   - Uses an iterative approach with a table to store results.

## Performance Comparison
The performance of the three approaches is compared for different values of `n`. The results are visualized in the following plot:

- **`fibonacci.png`**: A comparison of execution times for normal recursion, memoization, and tabulation.

## How to Run
1. Clone the repository.
2. Run the `fibonacci.py` script:
   ```bash
   python fibonacci.py