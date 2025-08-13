#!/usr/bin/env python3
"""
trial_delta Algorithm Implementation
====================================

Calculation: Lorenz Attractor using Runge-Kutta method
Position at t=100: (x,y,z) to 10 decimal places
Parameters: σ=a/50, ρ=b/10, β=c/100, initial=(1,1,1)

Base parameters: a=523, b=318, c=267, d=194, e=89, f=41
"""

import math
import json
from typing import Tuple, Dict, Any, List

class TrialDeltaCalculator:
    def __init__(self):
        self.a = 523
        self.b = 318
        self.c = 267
        self.d = 194
        self.e = 89
        self.f = 41
        
        # Lorenz parameters
        self.sigma = self.a / 50  # σ = 523/50 = 10.46
        self.rho = self.b / 10    # ρ = 318/10 = 31.8
        self.beta = self.c / 100  # β = 267/100 = 2.67
        
        # Initial conditions
        self.x0, self.y0, self.z0 = 1.0, 1.0, 1.0
        
        # Integration parameters
        self.dt = 0.01  # Time step
        self.t_final = 100.0
        
        # Tracking
        self.trajectory = []
        self.stages = []
        
    def lorenz_system(self, x: float, y: float, z: float) -> Tuple[float, float, float]:
        """Lorenz equations: dx/dt, dy/dt, dz/dt"""
        dx_dt = self.sigma * (y - x)
        dy_dt = x * (self.rho - z) - y
        dz_dt = x * y - self.beta * z
        return dx_dt, dy_dt, dz_dt
    
    def runge_kutta_step(self, x: float, y: float, z: float, dt: float) -> Tuple[float, float, float]:
        """Fourth-order Runge-Kutta step"""
        # k1
        k1x, k1y, k1z = self.lorenz_system(x, y, z)
        
        # k2
        k2x, k2y, k2z = self.lorenz_system(
            x + 0.5 * dt * k1x,
            y + 0.5 * dt * k1y,
            z + 0.5 * dt * k1z
        )
        
        # k3
        k3x, k3y, k3z = self.lorenz_system(
            x + 0.5 * dt * k2x,
            y + 0.5 * dt * k2y,
            z + 0.5 * dt * k2z
        )
        
        # k4
        k4x, k4y, k4z = self.lorenz_system(
            x + dt * k3x,
            y + dt * k3y,
            z + dt * k3z
        )
        
        # Update
        x_new = x + (dt / 6.0) * (k1x + 2*k2x + 2*k3x + k4x)
        y_new = y + (dt / 6.0) * (k1y + 2*k2y + 2*k3y + k4y)
        z_new = z + (dt / 6.0) * (k1z + 2*k2z + 2*k3z + k4z)
        
        return x_new, y_new, z_new
    
    def calculate_lyapunov_exponent(self, trajectory: List[Tuple[float, float, float]]) -> float:
        """Estimate largest Lyapunov exponent"""
        if len(trajectory) < 1000:
            return 0.0
        
        # Simple estimation using nearby trajectories
        # This is a simplified version for demonstration
        perturbation = 1e-8
        sum_log_divergence = 0.0
        count = 0
        
        for i in range(100, len(trajectory) - 100, 100):
            x, y, z = trajectory[i]
            
            # Perturbed trajectory
            x_pert = x + perturbation
            y_pert, z_pert = y, z
            
            # Evolve both for a short time
            for _ in range(10):
                x, y, z = self.runge_kutta_step(x, y, z, self.dt)
                x_pert, y_pert, z_pert = self.runge_kutta_step(x_pert, y_pert, z_pert, self.dt)
            
            # Calculate divergence
            divergence = math.sqrt((x - x_pert)**2 + (y - y_pert)**2 + (z - z_pert)**2)
            if divergence > 0:
                sum_log_divergence += math.log(divergence / perturbation)
                count += 1
        
        return sum_log_divergence / (count * 10 * self.dt) if count > 0 else 0.0
    
    def integrate_lorenz(self) -> Tuple[float, float, float]:
        """Integrate Lorenz system to t=100"""
        print("Starting Lorenz attractor integration")
        
        x, y, z = self.x0, self.y0, self.z0
        t = 0.0
        step_count = 0
        
        # Store initial condition
        self.trajectory.append((x, y, z))
        
        while t < self.t_final:
            # Runge-Kutta step
            x, y, z = self.runge_kutta_step(x, y, z, self.dt)
            t += self.dt
            step_count += 1
            
            # Store trajectory points (every 100 steps for memory efficiency)
            if step_count % 100 == 0:
                self.trajectory.append((x, y, z))
                
            # Progress reporting
            if step_count % 1000 == 0:
                print(f"t={t:.2f}: ({x:.6f}, {y:.6f}, {z:.6f})")
        
        self.stages.append(f"Integration completed: {step_count} steps, t={t:.2f}")
        return x, y, z
    
    def calculate_final_result(self) -> Tuple[Tuple[float, float, float], Dict[str, Any]]:
        """Calculate final position at t=100"""
        print("Starting trial_delta calculation")
        
        # Integrate system
        final_x, final_y, final_z = self.integrate_lorenz()
        
        # Calculate Lyapunov exponent
        lyapunov = self.calculate_lyapunov_exponent(self.trajectory)
        
        # Round to 10 decimal places
        x_rounded = round(final_x, 10)
        y_rounded = round(final_y, 10)
        z_rounded = round(final_z, 10)
        
        metadata = {
            'final_position': {
                'x': x_rounded,
                'y': y_rounded,
                'z': z_rounded
            },
            'lorenz_parameters': {
                'sigma': self.sigma,
                'rho': self.rho,
                'beta': self.beta
            },
            'initial_conditions': {
                'x0': self.x0,
                'y0': self.y0,
                'z0': self.z0
            },
            'integration_info': {
                'time_final': self.t_final,
                'time_step': self.dt,
                'total_steps': int(self.t_final / self.dt),
                'method': 'runge_kutta_4th_order'
            },
            'lyapunov_exponent': round(lyapunov, 6),
            'trajectory_points': len(self.trajectory),
            'stages': self.stages,
            'precision': 10
        }
        
        print(f"Final position at t=100: ({x_rounded}, {y_rounded}, {z_rounded})")
        return (x_rounded, y_rounded, z_rounded), metadata

def main():
    """Main execution function"""
    calculator = TrialDeltaCalculator()
    result, metadata = calculator.calculate_final_result()
    
    x, y, z = result
    print(f"\\nTrial Delta Final Result: ({x}, {y}, {z})")
    print(f"Lorenz parameters: σ={metadata['lorenz_parameters']['sigma']:.3f}, ρ={metadata['lorenz_parameters']['rho']:.3f}, β={metadata['lorenz_parameters']['beta']:.3f}")
    print(f"Lyapunov exponent: {metadata['lyapunov_exponent']}")
    
    # Save results to JSON
    with open('results.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return result, metadata

if __name__ == "__main__":
    main()