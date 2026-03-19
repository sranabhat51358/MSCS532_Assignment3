"""
quicksort_runner.py

Runs empirical comparison between:
- Randomized Quicksort
- Deterministic Quicksort
"""

import random
import time
from quicksort_algorithm import randomized_quicksort, deterministic_quicksort


# ------------------------------
# Input Generator
# ------------------------------
def generate_inputs(n):
    """
    Generates different input distributions.

    Returns:
        dict: Input types mapped to arrays
    """
    return {
        "Random": [random.randint(0, 100000) for _ in range(n)],
        "Sorted": list(range(n)),
        "Reverse Sorted": list(range(n, 0, -1)),
        "Repeated": [5] * n
    }


# ------------------------------
# Timing Utility
# ------------------------------
def measure_time(sort_func, arr, runs=3):
    """
    Measures average execution time.

    Parameters:
        sort_func (function): Sorting function
        arr (list): Input array
        runs (int): Number of repetitions

    Returns:
        float: Average time
    """
    total = 0
    for _ in range(runs):
        start = time.time()
        sort_func(arr.copy())
        total += time.time() - start

    return total / runs


# ------------------------------
# Experiment Runner
# ------------------------------
def run_experiment():
    input_sizes = [100, 500, 1000, 5000, 10000]
    distributions = ['Random', 'Sorted', 'Reverse', 'Repeated']

    print("\n===== PART 1: QUICKSORT ANALYSIS =====\n")

    for n in input_sizes:
        print(f"\n--- Input Size: {n} ---\n")
        for dist in distributions:
            # Generate array
            if dist == 'Random':
                arr = [random.randint(0, n) for _ in range(n)]
            elif dist == 'Sorted':
                arr = list(range(n))
            elif dist == 'Reverse':
                arr = list(range(n, 0, -1))
            elif dist == 'Repeated':
                arr = [random.choice([0, 1, 2, 3, 4, 5]) for _ in range(n)]

            # Print first 10 elements
            print(f"{dist} Input Sample (first 10): {arr[:10]}")

            # Measure time
            t_rand = measure_time(randomized_quicksort, arr)
            try:
                t_det = measure_time(deterministic_quicksort, arr)
            except RecursionError:
                t_det = "RecursionError: Maximum recursion depth exceeded"

            # Print times
            print(f"  Randomized Quicksort    = {t_rand:.6f} sec" if isinstance(t_rand, float) else f"  Randomized QS   = {t_rand}")
            print(f"  Deterministic Quicksort = {t_det}" if isinstance(t_det, str) else f"  Deterministic QS= {t_det:.6f} sec")

# ------------------------------
# Main Entry Point
# ------------------------------
if __name__ == "__main__":
    run_experiment()
