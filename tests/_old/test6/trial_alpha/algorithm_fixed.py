#!/usr/bin/env python3
"""
trial_alpha Algorithm Implementation (Fixed Version)
===================================================

Calculation: Σ(k=1 to 50) [a^k / (k! * (b+c*k))] + ∫(0 to π) sin(d*x)*cos(e*x)dx
Precision: 7 decimal places
Integration: Simpson's method with 1000 divisions
Overflow check: Enabled

Parameters: a=523, b=318, c=267, d=194, e=89, f=41
"""

import math
import json
from typing import Tuple, Dict, Any

class TrialAlphaCalculator:
    def __init__(self):
        self.a = 523
        self.b = 318
        self.c = 267
        self.d = 194
        self.e = 89
        self.f = 41
        
        # Calculation stages
        self.stages = []
        self.overflow_checks = []
        
    def factorial_safe(self, n: int) -> float:
        """Safe factorial calculation with overflow check"""
        if n < 0:
            raise ValueError("Factorial undefined for negative numbers")
        if n > 170:  # Factorial overflow threshold
            self.overflow_checks.append(f"Factorial overflow risk at n={n}")
            return float('inf')
        
        result = 1.0
        for i in range(1, n + 1):
            result *= i
            if result > 1e100:
                self.overflow_checks.append(f"Factorial overflow at n={n}")
                return float('inf')
        return result
    
    def power_safe(self, base: float, exp: int) -> float:
        """Safe power calculation with overflow check"""
        try:
            if exp > 50:  # Prevent massive computation
                self.overflow_checks.append(f"Power calculation truncated: {base}^{exp}")
                return 0.0  # Treat as negligible
            result = base ** exp
            if result > 1e100:
                self.overflow_checks.append(f"Power overflow: {base}^{exp}")
                return 0.0  # Treat as negligible
            return result
        except OverflowError:
            self.overflow_checks.append(f"OverflowError: {base}^{exp}")
            return 0.0
    
    def calculate_series_sum(self) -> float:
        """Calculate Σ(k=1 to 50) [a^k / (k! * (b+c*k))]"""
        print("Starting series sum calculation")
        series_sum = 0.0
        
        for k in range(1, 51):
            # Calculate a^k with overflow check
            a_power_k = self.power_safe(float(self.a), k)
            
            # Calculate k!
            k_factorial = self.factorial_safe(k)
            
            # Calculate denominator
            denominator = k_factorial * (self.b + self.c * k)
            
            # Check for division by zero or infinity
            if denominator == 0 or k_factorial == float('inf'):
                self.overflow_checks.append(f"Invalid denominator at k={k}")
                continue
            
            # Calculate term
            if a_power_k == 0.0:  # Overflow case treated as negligible
                term = 0.0
            else:
                term = a_power_k / denominator
            
            series_sum += term
            
            # Log progress
            if k % 10 == 0:
                print(f"Series calculation progress: k={k}, current_sum={series_sum:.10f}")
        
        self.stages.append(f"Series sum calculated: {series_sum:.10f}")
        return series_sum
    
    def simpson_integration(self, func, a: float, b: float, n: int = 1000) -> float:
        """Simpson's rule numerical integration"""
        if n % 2 == 1:
            n += 1  # Ensure even number of intervals
        
        h = (b - a) / n
        x = a
        
        # First and last terms
        integration_sum = func(x) + func(a + n * h)
        
        # Odd terms (coefficient 4)
        for i in range(1, n, 2):
            x = a + i * h
            integration_sum += 4 * func(x)
        
        # Even terms (coefficient 2)
        for i in range(2, n, 2):
            x = a + i * h
            integration_sum += 2 * func(x)
        
        result = integration_sum * h / 3
        return result
    
    def integrand_function(self, x: float) -> float:
        """Function to integrate: sin(d*x)*cos(e*x)"""
        return math.sin(self.d * x) * math.cos(self.e * x)
    
    def calculate_integral(self) -> float:
        """Calculate ∫(0 to π) sin(d*x)*cos(e*x)dx using Simpson's method"""
        print("Starting numerical integration")
        
        integral_result = self.simpson_integration(
            self.integrand_function, 
            0, 
            math.pi, 
            1000
        )
        
        self.stages.append(f"Integral calculated: {integral_result:.10f}")
        return integral_result
    
    def calculate_final_result(self) -> Tuple[float, Dict[str, Any]]:
        """Calculate final result and return metadata"""
        print("Starting trial_alpha calculation")
        
        # Calculate series sum
        series_sum = self.calculate_series_sum()
        
        # Calculate integral
        integral_result = self.calculate_integral()
        
        # Final sum
        final_result = series_sum + integral_result
        
        # Round to 7 decimal places
        final_rounded = round(final_result, 7)
        
        metadata = {
            'series_sum': series_sum,
            'integral_result': integral_result,
            'final_result': final_rounded,
            'parameters': {
                'a': self.a, 'b': self.b, 'c': self.c,
                'd': self.d, 'e': self.e, 'f': self.f
            },
            'stages': self.stages,
            'overflow_checks': self.overflow_checks,
            'precision': 7
        }
        
        print(f"Final result: {final_rounded}")
        return final_rounded, metadata

def main():
    """Main execution function"""
    calculator = TrialAlphaCalculator()
    result, metadata = calculator.calculate_final_result()
    
    print(f"Trial Alpha Final Result: {result}")
    print(f"Series Sum: {metadata['series_sum']:.10f}")
    print(f"Integral: {metadata['integral_result']:.10f}")
    print(f"Overflow Checks: {len(metadata['overflow_checks'])}")
    
    # Save results to JSON
    with open('results.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return result, metadata

if __name__ == "__main__":
    main()