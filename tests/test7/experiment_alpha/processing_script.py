#!/usr/bin/env python3
"""
Experiment Alpha - Complex Mathematical Calculation
Created by: テストAI7
Formula: Σ(i=1 to 100) [a * i^2 + b * i + c] / (d + e * i)
"""

import json
import time
from decimal import Decimal, getcontext

def load_config():
    """Load configuration parameters from config.json"""
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_alpha_formula(a, b, c, d, e, max_iterations=100, precision=5):
    """
    Calculate the complex summation formula with high precision
    """
    # Set decimal precision for accurate calculations
    getcontext().prec = precision + 10
    
    total_sum = Decimal('0')
    intermediate_values = []
    
    start_time = time.time()
    
    for i in range(1, max_iterations + 1):
        # Calculate numerator: a * i^2 + b * i + c
        numerator = Decimal(a) * Decimal(i) ** 2 + Decimal(b) * Decimal(i) + Decimal(c)
        
        # Calculate denominator: d + e * i
        denominator = Decimal(d) + Decimal(e) * Decimal(i)
        
        # Calculate term value
        term_value = numerator / denominator
        total_sum += term_value
        
        # Record intermediate values every 10 iterations
        if i % 10 == 0:
            intermediate_values.append({
                'iteration': i,
                'numerator': float(numerator),
                'denominator': float(denominator),
                'term_value': float(term_value),
                'cumulative_sum': float(total_sum)
            })
    
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return {
        'final_result': round(float(total_sum), precision),
        'intermediate_values': intermediate_values,
        'execution_time_ms': round(execution_time, 3),
        'total_iterations': max_iterations
    }

def main():
    """Main execution function"""
    try:
        # Load configuration
        config = load_config()
        params = config['parameters']
        
        # Perform calculation
        result = calculate_alpha_formula(
            params['a'], params['b'], params['c'], 
            params['d'], params['e'], 100, config['precision']
        )
        
        # Save results to output_results.json
        with open('output_results.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        # Generate metrics
        metrics = [
            f"Final Result: {result['final_result']}",
            f"Execution Time: {result['execution_time_ms']} ms",
            f"Total Iterations: {result['total_iterations']}",
            f"Intermediate Points Recorded: {len(result['intermediate_values'])}",
            f"Average Time per Iteration: {result['execution_time_ms'] / result['total_iterations']:.6f} ms"
        ]
        
        with open('metrics.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(metrics))
        
        print(f"Calculation completed successfully!")
        print(f"Final result: {result['final_result']}")
        
    except Exception as e:
        error_msg = f"Error in experiment_alpha: {str(e)}"
        print(error_msg)
        
        with open('error_log.txt', 'w', encoding='utf-8') as f:
            f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Error: {error_msg}\n")
            f.write(f"Error Type: {type(e).__name__}\n")

if __name__ == "__main__":
    main()