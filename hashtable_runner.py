"""
hash_runner.py

Runner script to test and measure performance of HashTable implementation.
Runs experiments on multiple dataset sizes and prints timing and sample data.
"""

import random
import time
from hash_table_algorithm import HashTable

def measure_time(func, *args, **kwargs):
    """
    Measure execution time of a function.

    Args:
        func (callable): Function to measure.
        *args, **kwargs: Arguments for the function.

    Returns:
        tuple: (elapsed_time in seconds, result of function)
    """
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return end - start, result

def run_experiment():
    """
    Run hash table experiments on multiple dataset sizes.
    Measures insertion, search, delete times, and prints load factor and sample elements.
    """
    print("\n===== PART 2: HASH TABLE WITH CHAINING =====\n")

    # Different dataset sizes to test scalability
    dataset_sizes = [1000, 5000, 10000]

    for num_elements in dataset_sizes:
        print(f"\n--- Dataset Size: {num_elements} ---")

        # Initialize hash table
        ht = HashTable(size=11)

        # Generate random keys and values
        keys = [f"key{i}" for i in range(num_elements)]
        values = [random.randint(0, 100000) for _ in range(num_elements)]

        # Measure insertion time
        t_insert, _ = measure_time(lambda: [ht.insert(k, v) for k, v in zip(keys, values)])
        print(f"Inserting {num_elements} elements took: {t_insert:.6f} sec")

        # Display sample elements
        print("Sample of first 10 elements:", ht.display_sample(10))

        # Search for 10 random keys
        search_keys = random.sample(keys, 10)
        t_search, search_results = measure_time(lambda: [ht.search(k) for k in search_keys])
        print(f"\nSearching 10 random keys took: {t_search:.6f} sec")
        print("Search results:", search_results)

        # Delete 10 random keys
        delete_keys = random.sample(keys, 10)
        t_delete, _ = measure_time(lambda: [ht.delete(k) for k in delete_keys])
        print(f"\nDeleting 10 random keys took: {t_delete:.6f} sec")

        # Print final load factor
        print(f"Final load factor: {ht.load_factor():.4f}\n")

if __name__ == "__main__":
    run_experiment()
