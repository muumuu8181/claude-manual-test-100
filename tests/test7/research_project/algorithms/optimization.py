#!/usr/bin/env python3
"""
Optimization Algorithms Implementation
Created by: テストAI7
Implements: Gradient Descent, Genetic Algorithm, Simulated Annealing
"""

import math
import random
import time
from typing import Callable, List, Tuple, Any
import numpy as np

class GradientDescent:
    """
    Gradient Descent optimization algorithm implementation
    """
    
    def __init__(self, learning_rate: float = 0.01, max_iterations: int = 1000, tolerance: float = 1e-6):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.history = []
    
    def optimize(self, func: Callable, gradient_func: Callable, initial_point: List[float]) -> Tuple[List[float], float]:
        """
        Optimize function using gradient descent
        """
        x = initial_point.copy()
        self.history = []
        
        for iteration in range(self.max_iterations):
            gradient = gradient_func(x)
            old_x = x.copy()
            
            # Update parameters
            for i in range(len(x)):
                x[i] -= self.learning_rate * gradient[i]
            
            current_value = func(x)
            self.history.append({'iteration': iteration, 'x': x.copy(), 'value': current_value})
            
            # Check convergence
            if self._euclidean_distance(old_x, x) < self.tolerance:
                break
        
        return x, func(x)
    
    def _euclidean_distance(self, a: List[float], b: List[float]) -> float:
        return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))

class GeneticAlgorithm:
    """
    Genetic Algorithm optimization implementation
    """
    
    def __init__(self, population_size: int = 100, generations: int = 100, mutation_rate: float = 0.1, crossover_rate: float = 0.8):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.history = []
    
    def optimize(self, fitness_func: Callable, bounds: List[Tuple[float, float]], maximize: bool = False) -> Tuple[List[float], float]:
        """
        Optimize function using genetic algorithm
        """
        dimensions = len(bounds)
        population = self._initialize_population(dimensions, bounds)
        
        for generation in range(self.generations):
            # Evaluate fitness
            fitness_scores = [fitness_func(individual) for individual in population]
            
            # Record best individual
            if maximize:
                best_idx = fitness_scores.index(max(fitness_scores))
            else:
                best_idx = fitness_scores.index(min(fitness_scores))
            
            best_individual = population[best_idx].copy()
            best_fitness = fitness_scores[best_idx]
            
            self.history.append({
                'generation': generation,
                'best_individual': best_individual,
                'best_fitness': best_fitness,
                'average_fitness': sum(fitness_scores) / len(fitness_scores)
            })
            
            # Selection, crossover, and mutation
            new_population = []
            
            for _ in range(self.population_size // 2):
                parent1 = self._tournament_selection(population, fitness_scores, maximize)
                parent2 = self._tournament_selection(population, fitness_scores, maximize)
                
                if random.random() < self.crossover_rate:
                    child1, child2 = self._crossover(parent1, parent2)
                else:
                    child1, child2 = parent1.copy(), parent2.copy()
                
                child1 = self._mutate(child1, bounds)
                child2 = self._mutate(child2, bounds)
                
                new_population.extend([child1, child2])
            
            population = new_population[:self.population_size]
        
        # Return best solution
        final_fitness = [fitness_func(individual) for individual in population]
        if maximize:
            best_idx = final_fitness.index(max(final_fitness))
        else:
            best_idx = final_fitness.index(min(final_fitness))
        
        return population[best_idx], final_fitness[best_idx]
    
    def _initialize_population(self, dimensions: int, bounds: List[Tuple[float, float]]) -> List[List[float]]:
        population = []
        for _ in range(self.population_size):
            individual = []
            for i in range(dimensions):
                value = random.uniform(bounds[i][0], bounds[i][1])
                individual.append(value)
            population.append(individual)
        return population
    
    def _tournament_selection(self, population: List[List[float]], fitness_scores: List[float], maximize: bool) -> List[float]:
        tournament_size = 3
        tournament_indices = random.sample(range(len(population)), min(tournament_size, len(population)))
        
        if maximize:
            best_idx = max(tournament_indices, key=lambda i: fitness_scores[i])
        else:
            best_idx = min(tournament_indices, key=lambda i: fitness_scores[i])
        
        return population[best_idx].copy()
    
    def _crossover(self, parent1: List[float], parent2: List[float]) -> Tuple[List[float], List[float]]:
        # Single-point crossover
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2
    
    def _mutate(self, individual: List[float], bounds: List[Tuple[float, float]]) -> List[float]:
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = random.uniform(bounds[i][0], bounds[i][1])
        return individual

class SimulatedAnnealing:
    """
    Simulated Annealing optimization algorithm implementation
    """
    
    def __init__(self, initial_temperature: float = 1000, cooling_rate: float = 0.95, min_temperature: float = 1e-3):
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.min_temperature = min_temperature
        self.history = []
    
    def optimize(self, func: Callable, bounds: List[Tuple[float, float]], initial_solution: List[float] = None) -> Tuple[List[float], float]:
        """
        Optimize function using simulated annealing
        """
        # Initialize solution
        if initial_solution is None:
            current_solution = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(len(bounds))]
        else:
            current_solution = initial_solution.copy()
        
        current_value = func(current_solution)
        best_solution = current_solution.copy()
        best_value = current_value
        
        temperature = self.initial_temperature
        iteration = 0
        
        while temperature > self.min_temperature:
            # Generate neighbor solution
            neighbor_solution = self._get_neighbor(current_solution, bounds, temperature)
            neighbor_value = func(neighbor_solution)
            
            # Accept or reject the neighbor
            if neighbor_value < current_value or random.random() < math.exp(-(neighbor_value - current_value) / temperature):
                current_solution = neighbor_solution
                current_value = neighbor_value
                
                # Update best solution
                if current_value < best_value:
                    best_solution = current_solution.copy()
                    best_value = current_value
            
            self.history.append({
                'iteration': iteration,
                'temperature': temperature,
                'current_solution': current_solution.copy(),
                'current_value': current_value,
                'best_value': best_value
            })
            
            temperature *= self.cooling_rate
            iteration += 1
        
        return best_solution, best_value
    
    def _get_neighbor(self, solution: List[float], bounds: List[Tuple[float, float]], temperature: float) -> List[float]:
        neighbor = solution.copy()
        for i in range(len(neighbor)):
            # Add random perturbation scaled by temperature
            perturbation = random.gauss(0, temperature / self.initial_temperature * 0.1)
            neighbor[i] += perturbation
            # Keep within bounds
            neighbor[i] = max(bounds[i][0], min(bounds[i][1], neighbor[i]))
        return neighbor

# Test functions for optimization
def sphere_function(x: List[float]) -> float:
    """Sphere function: f(x) = sum(xi^2)"""
    return sum(xi ** 2 for xi in x)

def rosenbrock_function(x: List[float]) -> float:
    """Rosenbrock function: f(x) = sum(100*(x[i+1] - xi^2)^2 + (1 - xi)^2)"""
    total = 0
    for i in range(len(x) - 1):
        total += 100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
    return total

def sphere_gradient(x: List[float]) -> List[float]:
    """Gradient of sphere function"""
    return [2 * xi for xi in x]

def benchmark_optimization_algorithms() -> dict:
    """
    Benchmark all optimization algorithms on test functions
    """
    results = {}
    
    # Test parameters
    dimensions = 2
    bounds = [(-5.0, 5.0)] * dimensions
    
    # Test Gradient Descent on sphere function
    gd = GradientDescent(learning_rate=0.1, max_iterations=1000)
    start_time = time.time()
    gd_solution, gd_value = gd.optimize(sphere_function, sphere_gradient, [3.0, 4.0])
    gd_time = (time.time() - start_time) * 1000
    
    # Test Genetic Algorithm on Rosenbrock function
    ga = GeneticAlgorithm(population_size=50, generations=100)
    start_time = time.time()
    ga_solution, ga_value = ga.optimize(rosenbrock_function, bounds)
    ga_time = (time.time() - start_time) * 1000
    
    # Test Simulated Annealing on sphere function
    sa = SimulatedAnnealing(initial_temperature=100, cooling_rate=0.95)
    start_time = time.time()
    sa_solution, sa_value = sa.optimize(sphere_function, bounds)
    sa_time = (time.time() - start_time) * 1000
    
    results = {
        'gradient_descent': {
            'solution': gd_solution,
            'value': gd_value,
            'time_ms': round(gd_time, 3),
            'iterations': len(gd.history),
            'function': 'sphere'
        },
        'genetic_algorithm': {
            'solution': ga_solution,
            'value': ga_value,
            'time_ms': round(ga_time, 3),
            'generations': len(ga.history),
            'function': 'rosenbrock'
        },
        'simulated_annealing': {
            'solution': sa_solution,
            'value': sa_value,
            'time_ms': round(sa_time, 3),
            'iterations': len(sa.history),
            'function': 'sphere'
        }
    }
    
    return results

if __name__ == "__main__":
    print("Optimization Algorithms Demo - Created by テストAI7")
    print("=" * 60)
    
    # Run benchmarks
    results = benchmark_optimization_algorithms()
    
    for algorithm, result in results.items():
        print(f"\n{algorithm.upper()}:")
        print(f"  Function: {result['function']}")
        print(f"  Solution: {[round(x, 6) for x in result['solution']]}")
        print(f"  Value: {result['value']:.8f}")
        print(f"  Time: {result['time_ms']} ms")
        if 'iterations' in result:
            print(f"  Iterations: {result['iterations']}")
        if 'generations' in result:
            print(f"  Generations: {result['generations']}")
    
    print("\nOptimal solutions:")
    print("  Sphere function: [0.0, 0.0] with value 0.0")
    print("  Rosenbrock function: [1.0, 1.0] with value 0.0")