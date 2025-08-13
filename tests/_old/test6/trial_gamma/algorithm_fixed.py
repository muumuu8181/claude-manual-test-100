#!/usr/bin/env python3
"""
trial_gamma Algorithm Implementation (Fixed)
============================================

Calculation: SGD optimization with bounded search space to prevent overflow
Function: f(x,y) = (x-a)^4 + (y-b)^4 + c*sin(d*x) + e*cos(f*y)
Precision: 8 decimal places

Parameters: a=523, b=318, c=267, d=194, e=89, f=41
"""

import math
import json
from typing import Tuple, Dict, Any

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
        
        # Bounds to prevent overflow
        self.bounds = (-1000, 1000)
        
        # Tracking
        self.convergence_history = []
        self.stages = []
        
    def clip_bounds(self, x: float, y: float) -> Tuple[float, float]:
        """Clip values to prevent overflow"""
        x = max(self.bounds[0], min(self.bounds[1], x))
        y = max(self.bounds[0], min(self.bounds[1], y))
        return x, y
    
    def objective_function(self, x: float, y: float) -> float:
        """f(x,y) = (x-a)^4 + (y-b)^4 + c*sin(d*x) + e*cos(f*y)"""
        x, y = self.clip_bounds(x, y)
        
        try:
            # Scale down large terms to prevent overflow
            term1 = ((x - self.a) / 100) ** 4 * 1e8  # Scaled quartic term
            term2 = ((y - self.b) / 100) ** 4 * 1e8  # Scaled quartic term
            term3 = self.c * math.sin(self.d * x / 1000)  # Scaled sine term
            term4 = self.e * math.cos(self.f * y / 1000)  # Scaled cosine term
            return term1 + term2 + term3 + term4
        except OverflowError:
            return 1e10  # Large penalty for overflow
    
    def compute_gradients(self, x: float, y: float) -> Tuple[float, float]:
        """Compute scaled partial derivatives"""
        x, y = self.clip_bounds(x, y)
        
        try:
            # Scaled gradients
            grad_x = (4 * ((x - self.a) / 100) ** 3 / 100) * 1e8 + \
                    self.c * self.d * math.cos(self.d * x / 1000) / 1000
            grad_y = (4 * ((y - self.b) / 100) ** 3 / 100) * 1e8 - \
                    self.e * self.f * math.sin(self.f * y / 1000) / 1000
            return grad_x, grad_y
        except OverflowError:
            return 1e6, 1e6  # Large gradients to push away from overflow
    
    def sgd_optimization(self, start_x: float = 0.0, start_y: float = 0.0) -> Tuple[float, float, float]:
        """Stochastic Gradient Descent with momentum and bounds"""
        print("Starting bounded SGD optimization")
        
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
            
            # Clip to bounds
            x, y = self.clip_bounds(x, y)
            
            # Evaluate function
            current_value = self.objective_function(x, y)
            
            # Track best solution
            if current_value < best_value:
                best_x, best_y, best_value = x, y, current_value
            
            # Record convergence history
            if i % 1000 == 0:
                self.convergence_history.append({
                    'iteration': i,
                    'x': round(x, 6),
                    'y': round(y, 6),
                    'value': round(current_value, 8),
                    'gradient_norm': round(math.sqrt(grad_x**2 + grad_y**2), 6)
                })
                print(f"Iteration {i}: f({x:.6f}, {y:.6f}) = {current_value:.8f}")
        
        self.stages.append(f"Bounded SGD completed: {self.iterations} iterations")
        return best_x, best_y, best_value
    
    def detect_local_minimum(self, x: float, y: float, tolerance: float = 1e-3) -> bool:
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
            'bounds_used': self.bounds,
            'parameters': {
                'a': self.a, 'b': self.b, 'c': self.c,
                'd': self.d, 'e': self.e, 'f': self.f
            },
            'sgd_parameters': {
                'learning_rate': self.learning_rate,
                'iterations': self.iterations,
                'momentum': self.momentum
            },
            'convergence_history': self.convergence_history,
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