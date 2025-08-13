#!/usr/bin/env python3
"""
trial_alpha Algorithm Implementation
=====================================

Calculation: Σ(k=1 to 50) [a^k / (k! * (b+c*k))] + ∫(0 to π) sin(d*x)*cos(e*x)dx
Precision: 7 decimal places
Integration: Simpson's method with 1000 divisions
Overflow check: Enabled

Parameters: a=523, b=318, c=267, d=194, e=89, f=41
"""

import math
import decimal
import numpy as np
import warnings
import logging
from typing import Tuple, Dict, Any

# High precision arithmetic
decimal.getcontext().prec = 50

class TrialAlphaCalculator:
    def __init__(self):
        self.a = 523
        self.b = 318
        self.c = 267
        self.d = 194
        self.e = 89
        self.f = 41
        
        # Logging setup
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Calculation stages
        self.stages = []
        self.overflow_checks = []
        
    def factorial_safe(self, n: int) -> decimal.Decimal:
        """Safe factorial calculation with overflow check"""
        if n < 0:
            raise ValueError("Factorial undefined for negative numbers")
        if n > 170:  # Factorial overflow threshold
            self.overflow_checks.append(f"Factorial overflow risk at n={n}")
            return decimal.Decimal('inf')
        
        result = decimal.Decimal(1)
        for i in range(1, n + 1):
            result *= decimal.Decimal(i)
        return result
    
    def power_safe(self, base: decimal.Decimal, exp: int) -> decimal.Decimal:
        """Safe power calculation with overflow check"""
        try:
            result = base ** exp
            if result > decimal.Decimal('1e100'):
                self.overflow_checks.append(f"Power overflow: {base}^{exp}")
                return decimal.Decimal('inf')
            return result
        except decimal.Overflow:
            self.overflow_checks.append(f"Decimal overflow: {base}^{exp}")
            return decimal.Decimal('inf')
    
    def calculate_series_sum(self) -> decimal.Decimal:
        """Calculate Σ(k=1 to 50) [a^k / (k! * (b+c*k))]"""
        self.logger.info("Starting series sum calculation")
        series_sum = decimal.Decimal(0)
        
        for k in range(1, 51):
            # Calculate a^k with overflow check
            a_power_k = self.power_safe(decimal.Decimal(self.a), k)
            
            # Calculate k!
            k_factorial = self.factorial_safe(k)
            
            # Calculate denominator
            denominator = k_factorial * decimal.Decimal(self.b + self.c * k)
            
            # Check for division by zero
            if denominator == 0:
                self.overflow_checks.append(f"Division by zero at k={k}")
                continue
            
            # Calculate term
            if a_power_k == decimal.Decimal('inf') or k_factorial == decimal.Decimal('inf'):
                term = decimal.Decimal(0)  # Treat overflow as negligible
            else:
                term = a_power_k / denominator
            
            series_sum += term
            
            # Log progress
            if k % 10 == 0:
                self.logger.info(f"Series calculation progress: k={k}, current_sum={float(series_sum):.10f}")
        
        self.stages.append(f"Series sum calculated: {float(series_sum):.10f}")
        return series_sum
    
    def simpson_integration(self, func, a: float, b: float, n: int = 1000) -> decimal.Decimal:
        """Simpson's rule numerical integration"""
        if n % 2 == 1:
            n += 1  # Ensure even number of intervals
        
        h = decimal.Decimal(b - a) / decimal.Decimal(n)
        x = decimal.Decimal(a)
        
        # First and last terms
        integration_sum = func(float(x)) + func(float(a + n * float(h)))
        
        # Odd terms (coefficient 4)
        for i in range(1, n, 2):
            x = decimal.Decimal(a) + decimal.Decimal(i) * h
            integration_sum += 4 * func(float(x))
        
        # Even terms (coefficient 2)
        for i in range(2, n, 2):
            x = decimal.Decimal(a) + decimal.Decimal(i) * h
            integration_sum += 2 * func(float(x))
        
        result = integration_sum * h / decimal.Decimal(3)
        return result
    
    def integrand_function(self, x: float) -> float:
        """Function to integrate: sin(d*x)*cos(e*x)"""
        return math.sin(self.d * x) * math.cos(self.e * x)
    
    def calculate_integral(self) -> decimal.Decimal:
        """Calculate ∫(0 to π) sin(d*x)*cos(e*x)dx using Simpson's method"""
        self.logger.info("Starting numerical integration")
        
        integral_result = self.simpson_integration(
            self.integrand_function, 
            0, 
            math.pi, 
            1000
        )
        
        self.stages.append(f"Integral calculated: {float(integral_result):.10f}")
        return integral_result
    
    def calculate_final_result(self) -> Tuple[decimal.Decimal, Dict[str, Any]]:
        """Calculate final result and return metadata"""
        self.logger.info("Starting trial_alpha calculation")
        
        # Calculate series sum
        series_sum = self.calculate_series_sum()
        
        # Calculate integral
        integral_result = self.calculate_integral()
        
        # Final sum
        final_result = series_sum + integral_result
        
        # Round to 7 decimal places
        final_rounded = round(float(final_result), 7)
        
        metadata = {
            'series_sum': float(series_sum),
            'integral_result': float(integral_result),
            'final_result': final_rounded,
            'parameters': {
                'a': self.a, 'b': self.b, 'c': self.c,
                'd': self.d, 'e': self.e, 'f': self.f
            },
            'stages': self.stages,
            'overflow_checks': self.overflow_checks,
            'precision': 7
        }
        
        self.logger.info(f"Final result: {final_rounded}")
        return decimal.Decimal(str(final_rounded)), metadata

def main():
    """Main execution function"""
    calculator = TrialAlphaCalculator()
    result, metadata = calculator.calculate_final_result()
    
    print(f"Trial Alpha Final Result: {result}")
    print(f"Series Sum: {metadata['series_sum']:.10f}")
    print(f"Integral: {metadata['integral_result']:.10f}")
    print(f"Overflow Checks: {len(metadata['overflow_checks'])}")
    
    return result, metadata

if __name__ == "__main__":
    main()