#!/usr/bin/env python3
"""
Experiment Beta - Matrix Operations
Created by: テストAI7
Operations: 5x5 matrix multiplication, determinant, and transpose
"""

import json
import time
import numpy as np
from decimal import Decimal, getcontext

def load_config():
    """Load configuration parameters from config.json"""
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def initialize_matrix(a, b, c, d, size=5):
    """
    Initialize matrix using formula: A[i][j] = (a+i*10) * (b-j*5) / (c+d)
    """
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            value = (a + i * 10) * (b - j * 5) / (c + d)
            row.append(value)
        matrix.append(row)
    return matrix

def matrix_multiply(A, B):
    """
    Perform matrix multiplication A * B
    """
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def calculate_determinant(matrix):
    """
    Calculate determinant using numpy for accuracy
    """
    np_matrix = np.array(matrix)
    return float(np.linalg.det(np_matrix))

def transpose_matrix(matrix):
    """
    Calculate transpose of matrix
    """
    n = len(matrix)
    transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]
    return transposed

def matrix_operations():
    """
    Perform all matrix operations
    """
    try:
        # Load configuration
        config = load_config()
        params = config['parameters']
        
        start_time = time.time()
        
        # Initialize matrices A and B
        matrix_A = initialize_matrix(params['a'], params['b'], params['c'], params['d'])
        matrix_B = initialize_matrix(params['a']+10, params['b']-10, params['c']+5, params['d']-5)
        
        # Perform matrix multiplication
        matrix_product = matrix_multiply(matrix_A, matrix_B)
        
        # Calculate determinant
        det_A = calculate_determinant(matrix_A)
        det_B = calculate_determinant(matrix_B)
        det_product = calculate_determinant(matrix_product)
        
        # Calculate transpose
        transpose_A = transpose_matrix(matrix_A)
        transpose_B = transpose_matrix(matrix_B)
        
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        
        results = {
            'matrix_A': matrix_A,
            'matrix_B': matrix_B,
            'matrix_product': matrix_product,
            'determinants': {
                'det_A': round(det_A, 8),
                'det_B': round(det_B, 8),
                'det_product': round(det_product, 8)
            },
            'transpose_A': transpose_A,
            'transpose_B': transpose_B,
            'execution_time_ms': round(execution_time, 3),
            'matrix_size': params['matrix_size']
        }
        
        # Save results
        with open('output_results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        # Generate metrics
        metrics = [
            f"Matrix Size: {params['matrix_size']}x{params['matrix_size']}",
            f"Determinant A: {results['determinants']['det_A']}",
            f"Determinant B: {results['determinants']['det_B']}",
            f"Determinant Product: {results['determinants']['det_product']}",
            f"Execution Time: {results['execution_time_ms']} ms",
            f"Operations Completed: Matrix Multiplication, Determinant, Transpose"
        ]
        
        with open('metrics.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(metrics))
        
        print("Matrix operations completed successfully!")
        print(f"Determinant A: {results['determinants']['det_A']}")
        print(f"Determinant Product: {results['determinants']['det_product']}")
        
        return results
        
    except Exception as e:
        error_msg = f"Error in experiment_beta: {str(e)}"
        print(error_msg)
        
        with open('error_log.txt', 'w', encoding='utf-8') as f:
            f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Error: {error_msg}\n")
            f.write(f"Error Type: {type(e).__name__}\n")
        
        return None

if __name__ == "__main__":
    matrix_operations()