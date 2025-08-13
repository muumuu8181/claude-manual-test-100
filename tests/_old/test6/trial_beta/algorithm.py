#!/usr/bin/env python3
"""
trial_beta Algorithm Implementation
===================================

Calculation: 3D matrix eigenvalue decomposition and maximum eigenvalue computation
Matrix M[10x10x10] with elements: (i+j+k) * sin((i*j*k)*π/100)
Final result: max_eigenvalue / (a*b*c*d*e*f) to 9 decimal places

Parameters: a=523, b=318, c=267, d=194, e=89, f=41
"""

import numpy as np
import math
import json
from typing import Tuple, Dict, Any, List
import warnings

# Suppress numpy warnings for cleaner output
warnings.filterwarnings('ignore')

class TrialBetaCalculator:
    def __init__(self):
        self.a = 523
        self.b = 318
        self.c = 267
        self.d = 194
        self.e = 89
        self.f = 41
        
        # Matrix dimensions
        self.matrix_size = 10
        
        # Calculation stages
        self.stages = []
        self.eigenvalue_details = []
        
    def create_3d_matrix(self) -> np.ndarray:
        """Create 3D matrix M[10x10x10] with specified elements"""
        print("Creating 3D matrix M[10x10x10]")
        
        matrix_3d = np.zeros((self.matrix_size, self.matrix_size, self.matrix_size))
        
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                for k in range(self.matrix_size):
                    # Element formula: (i+j+k) * sin((i*j*k)*π/100)
                    element_value = (i + j + k) * math.sin((i * j * k) * math.pi / 100)
                    matrix_3d[i, j, k] = element_value
        
        self.stages.append(f"3D matrix created with dimensions {self.matrix_size}x{self.matrix_size}x{self.matrix_size}")
        return matrix_3d
    
    def convert_to_2d_for_eigendecomposition(self, matrix_3d: np.ndarray) -> np.ndarray:
        """Convert 3D matrix to 2D matrix suitable for eigenvalue decomposition"""
        print("Converting 3D matrix to 2D for eigenvalue decomposition")
        
        # Method 1: Flatten and reshape to square matrix
        flattened = matrix_3d.flatten()
        total_elements = len(flattened)
        
        # Find the largest square matrix size
        square_size = int(math.sqrt(total_elements))
        
        # Take first square_size^2 elements and reshape
        matrix_2d = flattened[:square_size**2].reshape(square_size, square_size)
        
        # Make it symmetric for real eigenvalues
        matrix_2d = (matrix_2d + matrix_2d.T) / 2
        
        self.stages.append(f"3D matrix converted to 2D matrix {square_size}x{square_size}")
        return matrix_2d
    
    def compute_eigenvalues(self, matrix_2d: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Compute eigenvalues and eigenvectors"""
        print("Computing eigenvalue decomposition")
        
        try:
            eigenvalues, eigenvectors = np.linalg.eig(matrix_2d)
            
            # Separate real and imaginary parts
            real_parts = np.real(eigenvalues)
            imag_parts = np.imag(eigenvalues)
            
            # Record eigenvalue details
            for i, (real, imag) in enumerate(zip(real_parts, imag_parts)):
                self.eigenvalue_details.append({
                    'index': i,
                    'real_part': float(real),
                    'imaginary_part': float(imag),
                    'magnitude': float(np.abs(eigenvalues[i]))
                })
            
            self.stages.append(f"Eigenvalue decomposition completed: {len(eigenvalues)} eigenvalues computed")
            return eigenvalues, eigenvectors
            
        except np.linalg.LinAlgError as e:
            print(f"Eigenvalue computation failed: {e}")
            # Fallback: use singular value decomposition
            u, s, vt = np.linalg.svd(matrix_2d)
            eigenvalues = s  # Singular values as proxy for eigenvalues
            eigenvectors = vt
            
            self.stages.append("Fallback to SVD due to eigenvalue computation issues")
            return eigenvalues, eigenvectors
    
    def find_maximum_eigenvalue(self, eigenvalues: np.ndarray) -> complex:
        """Find the maximum eigenvalue by magnitude"""
        print("Finding maximum eigenvalue")
        
        # Calculate magnitude of each eigenvalue
        magnitudes = np.abs(eigenvalues)
        max_index = np.argmax(magnitudes)
        max_eigenvalue = eigenvalues[max_index]
        
        print(f"Maximum eigenvalue: {max_eigenvalue}")
        print(f"Real part: {np.real(max_eigenvalue):.10f}")
        print(f"Imaginary part: {np.imag(max_eigenvalue):.10f}")
        print(f"Magnitude: {np.abs(max_eigenvalue):.10f}")
        
        self.stages.append(f"Maximum eigenvalue found: magnitude={np.abs(max_eigenvalue):.10f}")
        return max_eigenvalue
    
    def calculate_final_result(self) -> Tuple[float, Dict[str, Any]]:
        """Calculate final result: max_eigenvalue / (a*b*c*d*e*f)"""
        print("Starting trial_beta calculation")
        
        # Create 3D matrix
        matrix_3d = self.create_3d_matrix()
        
        # Convert to 2D for eigenvalue decomposition
        matrix_2d = self.convert_to_2d_for_eigendecomposition(matrix_3d)
        
        # Compute eigenvalues
        eigenvalues, eigenvectors = self.compute_eigenvalues(matrix_2d)
        
        # Find maximum eigenvalue
        max_eigenvalue = self.find_maximum_eigenvalue(eigenvalues)
        
        # Calculate denominator
        denominator = self.a * self.b * self.c * self.d * self.e * self.f
        print(f"Denominator (a*b*c*d*e*f): {denominator}")
        
        # Calculate final result using the magnitude of max eigenvalue
        max_eigenvalue_magnitude = np.abs(max_eigenvalue)
        final_result = max_eigenvalue_magnitude / denominator
        
        # Round to 9 decimal places
        final_rounded = round(final_result, 9)
        
        metadata = {
            'max_eigenvalue_real': float(np.real(max_eigenvalue)),
            'max_eigenvalue_imag': float(np.imag(max_eigenvalue)),
            'max_eigenvalue_magnitude': float(max_eigenvalue_magnitude),
            'denominator': denominator,
            'final_result': final_rounded,
            'parameters': {
                'a': self.a, 'b': self.b, 'c': self.c,
                'd': self.d, 'e': self.e, 'f': self.f
            },
            'matrix_info': {
                'original_size': f"{self.matrix_size}x{self.matrix_size}x{self.matrix_size}",
                'converted_size': f"{matrix_2d.shape[0]}x{matrix_2d.shape[1]}",
                'total_eigenvalues': len(eigenvalues)
            },
            'stages': self.stages,
            'eigenvalue_details': self.eigenvalue_details[:10],  # First 10 for brevity
            'precision': 9
        }
        
        print(f"Final result: {final_rounded}")
        return final_rounded, metadata

def main():
    """Main execution function"""
    calculator = TrialBetaCalculator()
    result, metadata = calculator.calculate_final_result()
    
    print(f"\\nTrial Beta Final Result: {result}")
    print(f"Max Eigenvalue Magnitude: {metadata['max_eigenvalue_magnitude']:.10f}")
    print(f"Denominator: {metadata['denominator']}")
    print(f"Matrix Size: {metadata['matrix_info']['original_size']} -> {metadata['matrix_info']['converted_size']}")
    
    # Save results to JSON
    with open('results.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return result, metadata

if __name__ == "__main__":
    main()