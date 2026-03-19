"""
quicksort_algorithms.py

Contains implementations of:
1. Randomized Quicksort
2. Deterministic Quicksort (first element as pivot)
"""

import random


def randomized_quicksort(arr):
    """
    Sorts an array using Randomized Quicksort.

    Parameters:
        arr (list): Input list

    Returns:
        list: Sorted list
    """
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort(left) + middle + randomized_quicksort(right)


def deterministic_quicksort(arr):
    """
    Sorts an array using Deterministic Quicksort
    (first element as pivot).

    Parameters:
        arr (list): Input list

    Returns:
        list: Sorted list
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)
