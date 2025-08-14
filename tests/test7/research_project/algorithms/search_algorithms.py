#!/usr/bin/env python3
"""
Search Algorithms Implementation
Created by: テストAI7
Implements: Binary Search, Linear Search
"""

import time
from typing import List, Optional, Tuple

def linear_search(arr: List[int], target: int) -> Tuple[Optional[int], int]:
    """
    Linear Search implementation
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Returns: (index, comparisons_made) or (None, comparisons_made)
    """
    comparisons = 0
    
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    
    return None, comparisons

def binary_search(arr: List[int], target: int) -> Tuple[Optional[int], int]:
    """
    Binary Search implementation (requires sorted array)
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Returns: (index, comparisons_made) or (None, comparisons_made)
    """
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None, comparisons

def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: int = None, comparisons: int = 0) -> Tuple[Optional[int], int]:
    """
    Recursive Binary Search implementation
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return None, comparisons
    
    comparisons += 1
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)

def interpolation_search(arr: List[int], target: int) -> Tuple[Optional[int], int]:
    """
    Interpolation Search implementation
    Time Complexity: O(log log n) for uniformly distributed data, O(n) worst case
    Space Complexity: O(1)
    
    Works best with uniformly distributed sorted data
    """
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        comparisons += 1
        
        # If array has only one element
        if left == right:
            if arr[left] == target:
                return left, comparisons
            return None, comparisons
        
        # Calculate probe position using interpolation formula
        if arr[right] == arr[left]:
            pos = left
        else:
            pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        # Ensure pos is within bounds
        pos = max(left, min(right, pos))
        
        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return None, comparisons

def benchmark_search_algorithms(data_size: int = 10000) -> dict:
    """
    Benchmark search algorithms with various scenarios
    """
    import random
    
    # Generate sorted test data
    sorted_data = sorted([random.randint(1, data_size * 10) for _ in range(data_size)])
    
    # Test cases: element at beginning, middle, end, and not found
    test_cases = [
        ('first', sorted_data[0]),
        ('middle', sorted_data[len(sorted_data) // 2]),
        ('last', sorted_data[-1]),
        ('not_found', max(sorted_data) + 1000)
    ]
    
    results = {}
    
    for case_name, target in test_cases:
        results[case_name] = {}
        
        # Linear Search
        start_time = time.time()
        linear_index, linear_comparisons = linear_search(sorted_data, target)
        linear_time = (time.time() - start_time) * 1000
        
        # Binary Search (Iterative)
        start_time = time.time()
        binary_index, binary_comparisons = binary_search(sorted_data, target)
        binary_time = (time.time() - start_time) * 1000
        
        # Binary Search (Recursive)
        start_time = time.time()
        binary_rec_index, binary_rec_comparisons = binary_search_recursive(sorted_data, target)
        binary_rec_time = (time.time() - start_time) * 1000
        
        # Interpolation Search
        start_time = time.time()
        interp_index, interp_comparisons = interpolation_search(sorted_data, target)
        interp_time = (time.time() - start_time) * 1000
        
        results[case_name] = {
            'target': target,
            'linear_search': {
                'index': linear_index,
                'comparisons': linear_comparisons,
                'time_ms': round(linear_time, 6)
            },
            'binary_search': {
                'index': binary_index,
                'comparisons': binary_comparisons,
                'time_ms': round(binary_time, 6)
            },
            'binary_search_recursive': {
                'index': binary_rec_index,
                'comparisons': binary_rec_comparisons,
                'time_ms': round(binary_rec_time, 6)
            },
            'interpolation_search': {
                'index': interp_index,
                'comparisons': interp_comparisons,
                'time_ms': round(interp_time, 6)
            }
        }
    
    return {
        'data_size': data_size,
        'test_cases': results
    }

if __name__ == "__main__":
    # Demo and benchmark
    print("Search Algorithms Demo - Created by テストAI7")
    print("=" * 50)
    
    # Small demo
    demo_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    print(f"Searching for {target} in: {demo_data}")
    
    linear_result, linear_comps = linear_search(demo_data, target)
    print(f"Linear Search:      Index {linear_result}, {linear_comps} comparisons")
    
    binary_result, binary_comps = binary_search(demo_data, target)
    print(f"Binary Search:      Index {binary_result}, {binary_comps} comparisons")
    
    binary_rec_result, binary_rec_comps = binary_search_recursive(demo_data, target)
    print(f"Binary Search (Rec): Index {binary_rec_result}, {binary_rec_comps} comparisons")
    
    interp_result, interp_comps = interpolation_search(demo_data, target)
    print(f"Interpolation:      Index {interp_result}, {interp_comps} comparisons")
    
    print("\nBenchmarking with 10,000 elements...")
    benchmark_results = benchmark_search_algorithms(10000)
    
    print(f"Data size: {benchmark_results['data_size']}")
    for case_name, case_results in benchmark_results['test_cases'].items():
        print(f"\n{case_name.upper()} (target: {case_results['target']}):")
        for algorithm, result in case_results.items():
            if algorithm != 'target':
                print(f"  {algorithm}: {result['comparisons']} comparisons, {result['time_ms']:.6f}ms")