# MSCS532_Assignment3
This repository contains implementations and empirical analysis for Randomized Quicksort, Deterministic Quicksort, and a Hash Table with Chaining. The goal is to study the efficiency, scalability, and practical performance of these algorithms under different input conditions.
## Repository Structure
```
.
├── quicksort_algorithm.py                                       # Implementation of Randomized and Deterministic Quicksort
├── quicksort_runner.py                                          # Script to run empirical tests for Quicksort
├── hash_table_algorithm.py                                      # Implementation of Hash Table with Chaining
├── hashtable_runner.py                                          # Script to run empirical tests for Hash Table
└── Understanding Algorithm Efficiency and Scalability.pdf       # Report on Assignment
└── README.md                                                    # Instructions and summary

```

## Prerequisites

- Python 3.8 or higher

## Clone Repository
Open terminal and execute the command:

```
git clone https://github.com/sranabhat51358/MSCS532_Assignment3.git
cd MSCS532_Assignment3
```

## Randomized and Deterministic Quicksort:

Run the Quicksort experiment script with command:
```
python3 quicksort_runner.py
```
The script will generate arrays of different sizes and distributions and displays::

- Sample of the input array (first 10 elements)

- Average execution time for each algorithm

## Output of Quicksort:
```
===== PART 1: QUICKSORT ANALYSIS =====


--- Input Size: 100 ---

Random Input Sample (first 10): [38, 29, 95, 67, 37, 71, 65, 10, 9, 35]
  Randomized Quicksort   = 0.000072 sec
  Deterministic QS= 0.000062 sec
Sorted Input Sample (first 10): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  Randomized Quicksort   = 0.000078 sec
  Deterministic QS= 0.000235 sec
Reverse Input Sample (first 10): [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
  Randomized Quicksort   = 0.000075 sec
  Deterministic QS= 0.000242 sec
Repeated Input Sample (first 10): [0, 5, 1, 0, 5, 3, 2, 1, 5, 1]
  Randomized Quicksort   = 0.000020 sec
  Deterministic QS= 0.000084 sec

--- Input Size: 500 ---

Random Input Sample (first 10): [406, 217, 412, 431, 410, 30, 102, 30, 361, 366]
  Randomized Quicksort   = 0.000454 sec
  Deterministic QS= 0.000429 sec
Sorted Input Sample (first 10): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  Randomized Quicksort   = 0.000432 sec
  Deterministic QS= 0.004657 sec
Reverse Input Sample (first 10): [500, 499, 498, 497, 496, 495, 494, 493, 492, 491]
  Randomized Quicksort   = 0.000376 sec
  Deterministic QS= 0.004097 sec
Repeated Input Sample (first 10): [2, 3, 1, 0, 2, 0, 5, 0, 2, 1]
  Randomized Quicksort   = 0.000064 sec
  Deterministic QS= 0.000805 sec

--- Input Size: 1000 ---

Random Input Sample (first 10): [689, 277, 851, 880, 243, 596, 818, 133, 176, 166]
  Randomized Quicksort   = 0.000767 sec
  Deterministic QS= 0.000655 sec
Sorted Input Sample (first 10): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  Randomized Quicksort   = 0.000745 sec
  Deterministic Quicksort= RecursionError: Maximum recursion depth exceeded
Reverse Input Sample (first 10): [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]
  Randomized Quicksort   = 0.000697 sec
  Deterministic Quicksort= RecursionError: Maximum recursion depth exceeded
Repeated Input Sample (first 10): [3, 2, 3, 3, 0, 4, 4, 3, 4, 3]
  Randomized Quicksort   = 0.000115 sec
  Deterministic QS= 0.002586 sec

--- Input Size: 5000 ---

Random Input Sample (first 10): [3675, 4722, 4535, 2793, 1236, 63, 3994, 1603, 3436, 1596]
  Randomized Quicksort   = 0.003932 sec
  Deterministic QS= 0.003559 sec
Sorted Input Sample (first 10): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  Randomized Quicksort   = 0.003814 sec
  Deterministic Quicksort= RecursionError: Maximum recursion depth exceeded
Reverse Input Sample (first 10): [5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991]
  Randomized Quicksort   = 0.003771 sec
  Deterministic Quicksort= RecursionError: Maximum recursion depth exceeded
Repeated Input Sample (first 10): [0, 2, 0, 1, 2, 2, 2, 0, 0, 1]
  Randomized Quicksort   = 0.000496 sec
  Deterministic QS= 0.053940 sec

--- Input Size: 10000 ---

Random Input Sample (first 10): [9380, 7441, 4311, 6547, 9510, 7930, 9284, 9533, 2750, 4919]
  Randomized Quicksort   = 0.008083 sec
  Deterministic QS= 0.007773 sec
Sorted Input Sample (first 10): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  Randomized Quicksort   = 0.008195 sec
  Deterministic Quicksort= RecursionError: Maximum recursion depth exceeded
Reverse Input Sample (first 10): [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]
  Randomized Quicksort   = 0.007993 sec
  Deterministic Quicksort= RecursionError: Maximum recursion depth exceeded
Repeated Input Sample (first 10): [0, 5, 2, 2, 3, 0, 0, 2, 2, 4]
  Randomized Quicksort   = 0.000995 sec
  Deterministic Quicksort= RecursionError: Maximum recursion depth exceeded
```

## Running Hash Table with Chaining

Run the Hash table experiment script with command:
```
python3 hashtable_runner.py
```
The script will perform insertions, searches, and deletions on datasets of various sizes and display:

- Insertion time

- Search and deletion times for 10 random keys

- Load factor after insertion

- Sample elements from the table

## Output of Hash Table:
```
===== PART 2: HASH TABLE WITH CHAINING =====


--- Dataset Size: 1000 ---
Inserting 1000 elements took: 0.001361 sec
Sample of first 10 elements: [('key125', 72240), ('key476', 91485), ('key593', 1510), ('key387', 96284), ('key921', 99405), ('key6', 7589), ('key758', 60094), ('key154', 9130), ('key535', 26915), ('key895', 95885)]

Searching 10 random keys took: 0.000005 sec
Search results: [50222, 7888, 7171, 45643, 57786, 2111, 18848, 17340, 31744, 57803]

Deleting 10 random keys took: 0.000008 sec
Final load factor: 0.6450


--- Dataset Size: 5000 ---
Inserting 5000 elements took: 0.008860 sec
Sample of first 10 elements: [('key69', 44572), ('key592', 64251), ('key1531', 94311), ('key604', 21689), ('key221', 44624), ('key4790', 16568), ('key3542', 55611), ('key3675', 75874), ('key2377', 78248), ('key2773', 84967)]

Searching 10 random keys took: 0.000003 sec
Search results: [50336, 92867, 29054, 14064, 98676, 25411, 13402, 60693, 50144, 72790]

Deleting 10 random keys took: 0.000005 sec
Final load factor: 0.4061


--- Dataset Size: 10000 ---
Inserting 10000 elements took: 0.015706 sec
Sample of first 10 elements: [('key2297', 34513), ('key9485', 71151), ('key8080', 10443), ('key5784', 2832), ('key8055', 61911), ('key9241', 35205), ('key5545', 10033), ('key6359', 41961), ('key8998', 91186), ('key2300', 38870)]

Searching 10 random keys took: 0.000003 sec
Search results: [7357, 14533, 73041, 78948, 67217, 56044, 57957, 76842, 65262, 86393]

Deleting 10 random keys took: 0.000005 sec
Final load factor: 0.4065
```

## Summary of Findings

### Randomized vs Deterministic Quicksort

- Randomized Quicksort achieves O(n log n) performance consistently across all input types, including random, sorted, reverse-sorted, and arrays with repeated elements.

- Deterministic Quicksort performs well on small or random arrays but suffers from O(n²) worst-case behavior for sorted or reverse-sorted arrays, causing recursion errors on large inputs.

- Arrays with repeated elements demonstrate the advantage of randomized pivot selection, which allows large identical blocks to be sorted efficiently.

- Overall, randomized Quicksort scales reliably with input size, whereas deterministic Quicksort is highly sensitive to input order.

### Hash Table with Chaining

- The hash table uses a chaining method to handle collisions and dynamically resizes when the load factor exceeds 0.75.

- Insertions scale approximately linearly due to occasional resizing, while search and delete operations remain near-constant time even for large datasets.

- Empirical results confirm theoretical expectations: the expected time complexity for insert, search, and delete is O(1 + α), where α is the load factor.

- Dynamic resizing and a good hash function ensure efficient performance and even key distribution across buckets.