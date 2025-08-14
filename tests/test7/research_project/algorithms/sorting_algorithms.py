#!/usr/bin/env python3
"""
Sorting Algorithms Implementation
Created by: テストAI7
Implements: Quick Sort, Merge Sort, Heap Sort
"""

import time
import random
from typing import List, Tuple

def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort implementation with random pivot selection
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n)
    """
    if len(arr) <= 1:
        return arr
    
    # Random pivot selection to avoid worst case
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    # Partition array
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    return quick_sort(less) + equal + quick_sort(greater)

def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort implementation - stable sorting algorithm
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer - merge sorted halves
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Helper function to merge two sorted arrays
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort implementation using max heap
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    arr = arr.copy()  # Don't modify original
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)
    
    return arr

def heapify(arr: List[int], n: int, i: int):
    """
    Helper function to maintain heap property
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def benchmark_sorting_algorithms(data_size: int = 1000) -> dict:
    """
    Benchmark all three sorting algorithms
    """
    # Generate random test data
    test_data = [random.randint(1, 10000) for _ in range(data_size)]
    
    results = {}
    
    # Test Quick Sort
    start_time = time.time()
    quick_sorted = quick_sort(test_data.copy())
    quick_time = (time.time() - start_time) * 1000
    
    # Test Merge Sort
    start_time = time.time()
    merge_sorted = merge_sort(test_data.copy())
    merge_time = (time.time() - start_time) * 1000
    
    # Test Heap Sort
    start_time = time.time()
    heap_sorted = heap_sort(test_data.copy())
    heap_time = (time.time() - start_time) * 1000
    
    # Verify all algorithms produced correct results
    python_sorted = sorted(test_data)
    
    results = {
        'data_size': data_size,
        'quick_sort': {
            'time_ms': round(quick_time, 4),
            'correct': quick_sorted == python_sorted
        },
        'merge_sort': {
            'time_ms': round(merge_time, 4),
            'correct': merge_sorted == python_sorted
        },
        'heap_sort': {
            'time_ms': round(heap_time, 4),
            'correct': heap_sorted == python_sorted
        }
    }
    
    return results

if __name__ == "__main__":
    # Demo and benchmark
    print("Sorting Algorithms Demo - Created by テストAI7")
    print("=" * 50)
    
    # Small demo
    demo_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original data: {demo_data}")
    print(f"Quick Sort:    {quick_sort(demo_data.copy())}")
    print(f"Merge Sort:    {merge_sort(demo_data.copy())}")
    print(f"Heap Sort:     {heap_sort(demo_data.copy())}")
    print()
    
    # Benchmark
    print("Benchmarking with 1000 random integers...")
    benchmark_results = benchmark_sorting_algorithms(1000)
    
    for algorithm, result in benchmark_results.items():
        if algorithm != 'data_size':
            print(f"{algorithm}: {result['time_ms']:.4f}ms, Correct: {result['correct']}")