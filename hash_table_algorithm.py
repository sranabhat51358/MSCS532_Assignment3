"""
hash_table.py

Implementation of a Hash Table with Chaining for collision resolution.
Supports insert, search, delete operations and dynamic resizing.
"""

import random

class HashTable:
    """
    Hash Table with Chaining.

    Attributes:
        size (int): Number of buckets in the table.
        table (list): List of buckets (each bucket is a list of key-value pairs).
        num_elements (int): Current number of elements in the table.

    Methods:
        insert(key, value) : Insert or update a key-value pair.
        search(key)        : Retrieve value for a given key.
        delete(key)        : Remove a key-value pair.
        load_factor()      : Compute current load factor.
        display_sample(n)  : Show first n elements in the table.
    """

    def __init__(self, size=11):
        """
        Initialize the hash table.

        Args:
            size (int, optional): Initial number of buckets. Defaults to 11.
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.num_elements = 0

    def _hash(self, key):
        """
        Compute hash index for a given key.

        Args:
            key: Hashable object.

        Returns:
            int: Index of the bucket for this key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key exists, update its value.

        Args:
            key: The key to insert (hashable).
            value: Value associated with the key.
        """
        index = self._hash(key)
        # Check for existing key and update
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Append new key-value pair
        self.table[index].append((key, value))
        self.num_elements += 1

        # Resize table if load factor exceeds 0.75
        if self.load_factor() > 0.75:
            self._resize()

    def search(self, key):
        """
        Search for a value by key.

        Args:
            key: The key to search.

        Returns:
            The value associated with the key, or None if not found.
        """
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        Delete a key-value pair by key.

        Args:
            key: The key to delete.

        Returns:
            bool: True if key was found and deleted, False otherwise.
        """
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.num_elements -= 1
                return True
        return False

    def load_factor(self):
        """
        Compute current load factor of the table.

        Returns:
            float: Load factor (num_elements / number of buckets).
        """
        return self.num_elements / self.size

    def _resize(self):
        """
        Resize the table to reduce load factor.
        Doubles the size and rehashes all existing elements.
        """
        old_table = self.table
        self.size = self.size * 2 + 1  # Make size odd for better distribution
        self.table = [[] for _ in range(self.size)]
        self.num_elements = 0
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def display_sample(self, n=10):
        """
        Display first n elements from the table for inspection.

        Args:
            n (int, optional): Number of elements to display. Defaults to 10.

        Returns:
            list: List of first n key-value pairs.
        """
        sample = []
        for bucket in self.table:
            for pair in bucket:
                sample.append(pair)
                if len(sample) >= n:
                    return sample
        return sample
