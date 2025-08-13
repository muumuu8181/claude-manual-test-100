#!/usr/bin/env python3
"""
trial_gamma Algorithm Implementation
====================================

Calculation: Stochastic Gradient Descent optimization of f(x,y) = (x-a)^4 + (y-b)^4 + c*sin(d*x) + e*cos(f*y)
Precision: 8 decimal places
Learning rate: 0.001, Iterations: 10000, Momentum: 0.9

Parameters: a=523, b=318, c=267, d=194, e=89, f=41
"""

import math
import json
import numpy as np
from typing import Tuple, Dict, Any, List

class TrialGammaCalculator:
    def __init__(self):
        self.a = 523
        self.b = 318
        self.c = 267
        self.d = 194
        self.e = 89
        self.f = 41
        
        # SGD parameters
        self.learning_rate = 0.001
        self.iterations = 10000
        self.momentum = 0.9
        
        # Tracking
        self.convergence_history = []
        self.stages = []
        
    def objective_function(self, x: float, y: float) -> float:
        """f(x,y) = (x-a)^4 + (y-b)^4 + c*sin(d*x) + e*cos(f*y)"""
        term1 = (x - self.a) ** 4
        term2 = (y - self.b) ** 4
        term3 = self.c * math.sin(self.d * x)
        term4 = self.e * math.cos(self.f * y)
        return term1 + term2 + term3 + term4
    
    def compute_gradients(self, x: float, y: float) -> Tuple[float, float]:
        """Compute partial derivatives"""
        # ∂f/∂x = 4(x-a)^3 + c*d*cos(d*x)
        grad_x = 4 * (x - self.a) ** 3 + self.c * self.d * math.cos(self.d * x)
        
        # ∂f/∂y = 4(y-b)^3 - e*f*sin(f*y)
        grad_y = 4 * (y - self.b) ** 3 - self.e * self.f * math.sin(self.f * y)
        
        return grad_x, grad_y
    
    def sgd_optimization(self, start_x: float = 0.0, start_y: float = 0.0) -> Tuple[float, float, float]:
        """Stochastic Gradient Descent with momentum"""
        print("Starting SGD optimization")
        
        x, y = start_x, start_y
        vx, vy = 0.0, 0.0  # Momentum velocities
        
        best_x, best_y = x, y
        best_value = self.objective_function(x, y)
        
        for i in range(self.iterations):
            # Compute gradients
            grad_x, grad_y = self.compute_gradients(x, y)
            
            # Update velocities with momentum
            vx = self.momentum * vx - self.learning_rate * grad_x
            vy = self.momentum * vy - self.learning_rate * grad_y
            
            # Update positions
            x += vx
            y += vy
            
            # Evaluate function
            current_value = self.objective_function(x, y)
            
            # Track best solution
            if current_value < best_value:
                best_x, best_y, best_value = x, y, current_value
            
            # Record convergence history
            if i % 100 == 0:
                self.convergence_history.append({
                    'iteration': i,
                    'x': x,
                    'y': y,
                    'value': current_value,
                    'gradient_norm': math.sqrt(grad_x**2 + grad_y**2)
                })
                print(f"Iteration {i}: f({x:.6f}, {y:.6f}) = {current_value:.8f}")
        
        self.stages.append(f"SGD completed: {self.iterations} iterations")
        return best_x, best_y, best_value
    
    def detect_local_minimum(self, x: float, y: float, tolerance: float = 1e-6) -> bool:
        """Check if point is local minimum"""
        grad_x, grad_y = self.compute_gradients(x, y)
        gradient_norm = math.sqrt(grad_x**2 + grad_y**2)
        return gradient_norm < tolerance
    
    def calculate_final_result(self) -> Tuple[float, Dict[str, Any]]:
        """Calculate optimization result"""
        print("Starting trial_gamma calculation")
        
        # Run optimization
        opt_x, opt_y, min_value = self.sgd_optimization()
        
        # Check local minimum
        is_local_min = self.detect_local_minimum(opt_x, opt_y)
        
        # Round to 8 decimal places
        final_rounded = round(min_value, 8)
        
        metadata = {
            'optimal_x': round(opt_x, 8),
            'optimal_y': round(opt_y, 8),
            'minimum_value': final_rounded,
            'is_local_minimum': is_local_min,
            'parameters': {
                'a': self.a, 'b': self.b, 'c': self.c,
                'd': self.d, 'e': self.e, 'f': self.f
            },
            'sgd_parameters': {
                'learning_rate': self.learning_rate,
                'iterations': self.iterations,
                'momentum': self.momentum
            },
            'convergence_history': self.convergence_history[-10:],  # Last 10 points
            'stages': self.stages,
            'precision': 8
        }
        
        print(f"Final minimum: {final_rounded} at ({opt_x:.8f}, {opt_y:.8f})")
        return final_rounded, metadata

def main():
    """Main execution function"""
    calculator = TrialGammaCalculator()
    result, metadata = calculator.calculate_final_result()
    
    print(f"\\nTrial Gamma Final Result: {result}")
    print(f"Optimal point: ({metadata['optimal_x']}, {metadata['optimal_y']})")
    print(f"Local minimum: {metadata['is_local_minimum']}")
    
    # Save results to JSON
    with open('results.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return result, metadata

if __name__ == "__main__":
    main()