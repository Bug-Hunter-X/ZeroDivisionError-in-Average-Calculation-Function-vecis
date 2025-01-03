# Python Average Calculation Bug

This repository demonstrates a common bug in Python: a `ZeroDivisionError` that occurs when attempting to calculate the average of an empty list.  The original code lacks error handling for this specific case. The solution provides a robust way to handle empty input and avoids the error.

## Bug
The `calculate_average` function in `bug.py` fails when an empty list is passed to it, raising a `ZeroDivisionError`. 

## Solution
The corrected function in `bugSolution.py` checks for an empty list before performing the calculation, returning 0 in that case to prevent the error.