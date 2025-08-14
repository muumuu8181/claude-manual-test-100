#!/usr/bin/env python3
"""
Linear Model Implementation
Created by: テストAI7
Implements: Linear Regression with gradient descent and analytical solution
"""

import numpy as np
import pandas as pd
import time
from typing import Tuple, Optional, List

class LinearRegression:
    """
    Linear Regression implementation with multiple solving methods
    """
    
    def __init__(self, learning_rate: float = 0.01, max_iterations: int = 1000, tolerance: float = 1e-6):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.weights = None
        self.bias = None
        self.training_history = []
        self.is_fitted = False
    
    def fit_analytical(self, X: np.ndarray, y: np.ndarray) -> 'LinearRegression':
        """
        Fit using analytical solution (Normal Equation): w = (X^T X)^-1 X^T y
        """
        start_time = time.time()
        
        # Add bias term (intercept) to features
        X_with_bias = np.column_stack([np.ones(X.shape[0]), X])
        
        try:
            # Normal equation: w = (X^T X)^-1 X^T y
            XtX = X_with_bias.T @ X_with_bias
            XtX_inv = np.linalg.inv(XtX)
            weights_with_bias = XtX_inv @ X_with_bias.T @ y
            
            self.bias = weights_with_bias[0]
            self.weights = weights_with_bias[1:]
            
        except np.linalg.LinAlgError:
            # Use pseudo-inverse if matrix is singular
            weights_with_bias = np.linalg.pinv(X_with_bias) @ y
            self.bias = weights_with_bias[0]
            self.weights = weights_with_bias[1:]
        
        end_time = time.time()
        self.training_time = (end_time - start_time) * 1000
        self.is_fitted = True
        
        return self
    
    def fit_gradient_descent(self, X: np.ndarray, y: np.ndarray) -> 'LinearRegression':
        """
        Fit using gradient descent optimization
        """
        start_time = time.time()
        
        # Initialize weights and bias
        n_features = X.shape[1]
        self.weights = np.random.normal(0, 0.01, n_features)
        self.bias = 0.0
        
        # Training loop
        for iteration in range(self.max_iterations):
            # Forward pass
            y_pred = self.predict(X)
            
            # Calculate loss (MSE)
            loss = np.mean((y - y_pred) ** 2)
            
            # Calculate gradients
            m = X.shape[0]
            dw = -(2/m) * X.T @ (y - y_pred)
            db = -(2/m) * np.sum(y - y_pred)
            
            # Update parameters
            old_weights = self.weights.copy()
            old_bias = self.bias
            
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
            # Record training history
            self.training_history.append({
                'iteration': iteration,
                'loss': loss,
                'weights': self.weights.copy(),
                'bias': self.bias
            })
            
            # Check convergence
            weight_change = np.linalg.norm(self.weights - old_weights)
            bias_change = abs(self.bias - old_bias)
            
            if weight_change < self.tolerance and bias_change < self.tolerance:
                break
        
        end_time = time.time()
        self.training_time = (end_time - start_time) * 1000
        self.is_fitted = True
        
        return self
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions on new data
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        return X @ self.weights + self.bias
    
    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate R² score
        """
        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        return r2
    
    def mean_squared_error(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate Mean Squared Error
        """
        y_pred = self.predict(X)
        return np.mean((y - y_pred) ** 2)
    
    def mean_absolute_error(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate Mean Absolute Error
        """
        y_pred = self.predict(X)
        return np.mean(np.abs(y - y_pred))

class PolynomialFeatures:
    """
    Generate polynomial features for linear regression
    """
    
    def __init__(self, degree: int = 2):
        self.degree = degree
        self.feature_names = []
    
    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        """
        Generate polynomial features up to specified degree
        """
        n_samples, n_features = X.shape
        
        # Start with original features
        poly_features = [X]
        self.feature_names = [f'x{i}' for i in range(n_features)]
        
        # Add polynomial terms
        for degree in range(2, self.degree + 1):
            for i in range(n_features):
                for j in range(i, n_features):
                    if degree == 2:
                        if i == j:
                            new_feature = (X[:, i] ** 2).reshape(-1, 1)
                            self.feature_names.append(f'x{i}^2')
                        else:
                            new_feature = (X[:, i] * X[:, j]).reshape(-1, 1)
                            self.feature_names.append(f'x{i}*x{j}')
                        poly_features.append(new_feature)
        
        return np.column_stack(poly_features)

def load_dataset(train_path: str, test_path: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Load training and test datasets
    """
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    
    # Extract features and targets
    feature_cols = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
    
    X_train = train_df[feature_cols].values
    y_train = train_df['target'].values
    X_test = test_df[feature_cols].values
    y_test = test_df['target'].values
    
    return X_train, y_train, X_test, y_test

def evaluate_models(X_train, y_train, X_test, y_test) -> dict:
    """
    Evaluate different linear model configurations
    """
    results = {}
    
    # Standard Linear Regression - Analytical
    lr_analytical = LinearRegression()
    lr_analytical.fit_analytical(X_train, y_train)
    
    results['linear_analytical'] = {
        'train_r2': lr_analytical.score(X_train, y_train),
        'test_r2': lr_analytical.score(X_test, y_test),
        'train_mse': lr_analytical.mean_squared_error(X_train, y_train),
        'test_mse': lr_analytical.mean_squared_error(X_test, y_test),
        'training_time_ms': lr_analytical.training_time,
        'method': 'analytical'
    }
    
    # Standard Linear Regression - Gradient Descent
    lr_gd = LinearRegression(learning_rate=0.01, max_iterations=1000)
    lr_gd.fit_gradient_descent(X_train, y_train)
    
    results['linear_gradient_descent'] = {
        'train_r2': lr_gd.score(X_train, y_train),
        'test_r2': lr_gd.score(X_test, y_test),
        'train_mse': lr_gd.mean_squared_error(X_train, y_train),
        'test_mse': lr_gd.mean_squared_error(X_test, y_test),
        'training_time_ms': lr_gd.training_time,
        'iterations': len(lr_gd.training_history),
        'method': 'gradient_descent'
    }
    
    # Polynomial Regression (degree 2)
    poly = PolynomialFeatures(degree=2)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.fit_transform(X_test)
    
    lr_poly = LinearRegression()
    lr_poly.fit_analytical(X_train_poly, y_train)
    
    results['polynomial_degree_2'] = {
        'train_r2': lr_poly.score(X_train_poly, y_train),
        'test_r2': lr_poly.score(X_test_poly, y_test),
        'train_mse': lr_poly.mean_squared_error(X_train_poly, y_train),
        'test_mse': lr_poly.mean_squared_error(X_test_poly, y_test),
        'training_time_ms': lr_poly.training_time,
        'n_features': X_train_poly.shape[1],
        'method': 'polynomial'
    }
    
    return results

if __name__ == "__main__":
    print("Linear Model Demo - Created by テストAI7")
    print("=" * 50)
    
    try:
        # Load datasets
        X_train, y_train, X_test, y_test = load_dataset(
            '../datasets/training_data.csv',
            '../datasets/test_data.csv'
        )
        
        print(f"Training data shape: {X_train.shape}")
        print(f"Test data shape: {X_test.shape}")
        
        # Evaluate models
        results = evaluate_models(X_train, y_train, X_test, y_test)
        
        print("\nModel Evaluation Results:")
        print("-" * 40)
        
        for model_name, metrics in results.items():
            print(f"\n{model_name.upper()}:")
            print(f"  Method: {metrics['method']}")
            print(f"  Train R²: {metrics['train_r2']:.6f}")
            print(f"  Test R²: {metrics['test_r2']:.6f}")
            print(f"  Train MSE: {metrics['train_mse']:.6f}")
            print(f"  Test MSE: {metrics['test_mse']:.6f}")
            print(f"  Training Time: {metrics['training_time_ms']:.3f} ms")
            if 'iterations' in metrics:
                print(f"  Iterations: {metrics['iterations']}")
            if 'n_features' in metrics:
                print(f"  Features: {metrics['n_features']}")
        
    except FileNotFoundError:
        print("Dataset files not found. Please ensure training_data.csv and test_data.csv exist in ../datasets/")
    except Exception as e:
        print(f"Error: {e}")