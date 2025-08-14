#!/usr/bin/env python3
"""
Experiment Gamma - Fibonacci Sequence Calculations
Created by: テストAI7
Calculations: F(50), F(60), and modified Fibonacci sequence
"""

import json
import time
from functools import lru_cache

def load_config():
    """Load configuration parameters from config.json"""
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@lru_cache(maxsize=None)
def fibonacci_standard(n):
    """
    Calculate standard Fibonacci number F(n) with memoization
    """
    if n <= 1:
        return n
    return fibonacci_standard(n-1) + fibonacci_standard(n-2)

def fibonacci_iterative(n):
    """
    Calculate Fibonacci iteratively for large numbers
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_modified(n, a, b, c):
    """
    Calculate modified Fibonacci: F(n) = a*F(n-1) + b*F(n-2) + c
    """
    if n == 1:
        return a * 1 + b * 0 + c  # F(1) = a*1 + b*0 + c
    elif n == 2:
        return a * 1 + b * 1 + c  # F(2) = a*1 + b*1 + c
    
    # Initialize base cases
    f_prev_prev = a * 1 + b * 0 + c  # F(1)
    f_prev = a * 1 + b * 1 + c       # F(2)
    
    for i in range(3, n + 1):
        f_current = a * f_prev + b * f_prev_prev + c
        f_prev_prev, f_prev = f_prev, f_current
    
    return f_prev

def fibonacci_calculations():
    """
    Perform all Fibonacci calculations with timing
    """
    try:
        # Load configuration
        config = load_config()
        params = config['parameters']
        
        results = {}
        
        # Calculate F(50)
        start_time = time.time()
        f50 = fibonacci_iterative(50)
        f50_time = (time.time() - start_time) * 1000
        
        # Calculate F(60)
        start_time = time.time()
        f60 = fibonacci_iterative(60)
        f60_time = (time.time() - start_time) * 1000
        
        # Calculate modified Fibonacci sequence F(1) to F(20)
        start_time = time.time()
        modified_sequence = []
        for n in range(1, 21):
            f_n = fibonacci_modified(n, params['a'], params['b'], params['c'])
            modified_sequence.append({
                'n': n,
                'value': f_n
            })
        modified_time = (time.time() - start_time) * 1000
        
        results = {
            'standard_fibonacci': {
                'F_50': {
                    'value': f50,
                    'execution_time_ms': round(f50_time, 6)
                },
                'F_60': {
                    'value': f60,
                    'execution_time_ms': round(f60_time, 6)
                }
            },
            'modified_fibonacci': {
                'sequence': modified_sequence,
                'total_execution_time_ms': round(modified_time, 6),
                'parameters': {
                    'a': params['a'],
                    'b': params['b'],
                    'c': params['c']
                }
            },
            'total_execution_time_ms': round(f50_time + f60_time + modified_time, 6)
        }
        
        # Save results
        with open('output_results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        # Generate metrics
        metrics = [
            f"F(50): {results['standard_fibonacci']['F_50']['value']}",
            f"F(60): {results['standard_fibonacci']['F_60']['value']}",
            f"F(50) Execution Time: {results['standard_fibonacci']['F_50']['execution_time_ms']} ms",
            f"F(60) Execution Time: {results['standard_fibonacci']['F_60']['execution_time_ms']} ms",
            f"Modified F(20): {modified_sequence[19]['value']}",
            f"Modified Sequence Time: {results['modified_fibonacci']['total_execution_time_ms']} ms",
            f"Total Execution Time: {results['total_execution_time_ms']} ms",
            f"Modified Fibonacci Parameters: a={params['a']}, b={params['b']}, c={params['c']}"
        ]
        
        with open('metrics.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(metrics))
        
        print("Fibonacci calculations completed successfully!")
        print(f"F(50): {f50}")
        print(f"F(60): {f60}")
        print(f"Modified F(20): {modified_sequence[19]['value']}")
        
        return results
        
    except Exception as e:
        error_msg = f"Error in experiment_gamma: {str(e)}"
        print(error_msg)
        
        with open('error_log.txt', 'w', encoding='utf-8') as f:
            f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Error: {error_msg}\n")
            f.write(f"Error Type: {type(e).__name__}\n")
        
        return None

if __name__ == "__main__":
    fibonacci_calculations()