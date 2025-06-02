"""
Sorting Algorithms Module
Contains Quick Sort and Merge Sort implementations with performance tracking
"""

import time
import psutil
import os
from typing import List
from performance_metrics import PerformanceMetrics

class SortingAlgorithms:
    """Quick Sort and Merge Sort algorithms with performance tracking"""
    
    def __init__(self):
        self.metrics = PerformanceMetrics()
    
    def quick_sort(self, arr: List[int]) -> List[int]:
        """
        Quick Sort algorithm with performance tracking
        
        Args:
            arr: List of numbers to sort
            
        Returns:
            Sorted list of numbers
        """
        self.metrics.reset()
        start_time = time.perf_counter()
        
        # Make a copy so we don't change the original list
        sorted_arr = arr.copy()
        
        # Check how much memory we're using at the start
        process = psutil.Process(os.getpid())
        memory_at_start = process.memory_info().rss
        
        self._quick_sort_helper(sorted_arr, 0, len(sorted_arr) - 1)
        
        # Calculate how long it took and how much memory we used
        self.metrics.execution_time = time.perf_counter() - start_time
        memory_at_end = process.memory_info().rss
        self.metrics.memory_usage = memory_at_end - memory_at_start
        
        return sorted_arr
    
    def _quick_sort_helper(self, arr: List[int], low: int, high: int):
        """
        Helper function that does the actual Quick Sort work
        
        Args:
            arr: List to sort
            low: Starting position
            high: Ending position
        """
        if low < high:
            # Split the array and get the position of the pivot
            pivot_position = self._partition(arr, low, high)
            
            # Sort the left and right parts separately
            self._quick_sort_helper(arr, low, pivot_position - 1)
            self._quick_sort_helper(arr, pivot_position + 1, high)
    
    def _partition(self, arr: List[int], low: int, high: int) -> int:
        """
        Split the array around a pivot (chosen as the last element)
        
        Args:
            arr: List to split
            low: Starting position
            high: Ending position
            
        Returns:
            Position where the pivot ends up
        """
        # Choose the last element as our pivot
        pivot = arr[high]
        
        # Keep track of where smaller elements should go
        smaller_index = low - 1
        
        for j in range(low, high):
            self.metrics.comparisons += 1
            # If current number is smaller than or equal to pivot
            if arr[j] <= pivot:
                smaller_index += 1
                arr[smaller_index], arr[j] = arr[j], arr[smaller_index]
                self.metrics.swaps += 1
        
        # Put pivot in its correct position
        arr[smaller_index + 1], arr[high] = arr[high], arr[smaller_index + 1]
        self.metrics.swaps += 1
        
        return smaller_index + 1
    
    def merge_sort(self, arr: List[int]) -> List[int]:
        """
        Merge Sort algorithm with performance tracking
        
        Args:
            arr: List of numbers to sort
            
        Returns:
            Sorted list of numbers
        """
        self.metrics.reset()
        start_time = time.perf_counter()
        
        # Check how much memory we're using at the start
        process = psutil.Process(os.getpid())
        memory_at_start = process.memory_info().rss
        
        sorted_arr = self._merge_sort_helper(arr)
        
        # Calculate how long it took and how much memory we used
        self.metrics.execution_time = time.perf_counter() - start_time
        memory_at_end = process.memory_info().rss
        self.metrics.memory_usage = memory_at_end - memory_at_start
        
        return sorted_arr
    
    def _merge_sort_helper(self, arr: List[int]) -> List[int]:
        """
        Helper function that does the actual Merge Sort work
        
        Args:
            arr: List to sort
            
        Returns:
            Sorted list
        """
        # Base case: array with one or zero elements is already sorted
        if len(arr) <= 1:
            return arr
        
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Sort both halves separately
        left_sorted = self._merge_sort_helper(left_half)
        right_sorted = self._merge_sort_helper(right_half)
        
        # Combine the sorted halves
        return self._merge(left_sorted, right_sorted)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """
        Combine two sorted arrays into one sorted array
        
        Args:
            left: Left sorted array
            right: Right sorted array
            
        Returns:
            Combined sorted array
        """
        merged = []
        i = j = 0
        
        # Compare elements from both arrays and merge in sorted order
        while i < len(left) and j < len(right):
            self.metrics.comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # Add remaining elements from left array
        while i < len(left):
            merged.append(left[i])
            i += 1
        
        # Add remaining elements from right array
        while j < len(right):
            merged.append(right[j])
            j += 1
        
        return merged
    
    def get_metrics(self) -> PerformanceMetrics:
        """Return current performance metrics"""
        return self.metrics