---
title: Primality Testing
layout: default
---


# Primality Testing

This repository implements two probabilistic primality tests: Fermat's test and the Miller-Rabin test.

## Problem Description
Given a number, determine if it is prime or composite using probabilistic methods.

## Approaches
1. **Fermat's Test**:
   - Based on Fermat's Little Theorem.
   - Fast but has some limitations (e.g., Carmichael numbers).

2. **Miller-Rabin Test**:
   - More accurate than Fermat's test.
   - Uses additional checks to reduce the probability of false positives.

## How to Run
1. Clone the repository.
2. Run the `primality.py` script:
   ```bash
   python primality.py