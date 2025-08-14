#!/usr/bin/env python3
"""
Neural Network Implementation
Created by: テストAI7
Implements: Simple feedforward neural network with backpropagation
"""

import numpy as np
import pandas as pd
import time
from typing import List, Tuple, Callable, Optional

class ActivationFunctions:
    """
    Collection of activation functions and their derivatives
    """
    
    @staticmethod
    def sigmoid(x):
        # Clip to prevent overflow
        x = np.clip(x, -500, 500)
        return 1 / (1 + np.exp(-x))
    
    @staticmethod
    def sigmoid_derivative(x):
        s = ActivationFunctions.sigmoid(x)
        return s * (1 - s)
    
    @staticmethod
    def tanh(x):
        return np.tanh(x)
    
    @staticmethod
    def tanh_derivative(x):
        return 1 - np.tanh(x) ** 2
    
    @staticmethod
    def relu(x):
        return np.maximum(0, x)
    
    @staticmethod
    def relu_derivative(x):
        return (x > 0).astype(float)
    
    @staticmethod
    def leaky_relu(x, alpha=0.01):
        return np.where(x > 0, x, alpha * x)
    
    @staticmethod
    def leaky_relu_derivative(x, alpha=0.01):
        return np.where(x > 0, 1, alpha)

class NeuralNetwork:
    """
    Simple feedforward neural network implementation
    """
    
    def __init__(self, layers: List[int], activation: str = 'sigmoid', learning_rate: float = 0.01):
        self.layers = layers
        self.learning_rate = learning_rate
        self.weights = []
        self.biases = []
        self.training_history = []
        
        # Set activation function
        if activation == 'sigmoid':
            self.activation = ActivationFunctions.sigmoid
            self.activation_derivative = ActivationFunctions.sigmoid_derivative
        elif activation == 'tanh':
            self.activation = ActivationFunctions.tanh
            self.activation_derivative = ActivationFunctions.tanh_derivative
        elif activation == 'relu':
            self.activation = ActivationFunctions.relu
            self.activation_derivative = ActivationFunctions.relu_derivative
        elif activation == 'leaky_relu':
            self.activation = ActivationFunctions.leaky_relu
            self.activation_derivative = ActivationFunctions.leaky_relu_derivative
        else:
            raise ValueError(f"Unsupported activation function: {activation}")
        
        self._initialize_parameters()
    
    def _initialize_parameters(self):
        """
        Initialize weights and biases using Xavier initialization
        """
        for i in range(len(self.layers) - 1):
            # Xavier initialization
            limit = np.sqrt(6 / (self.layers[i] + self.layers[i + 1]))
            weight = np.random.uniform(-limit, limit, (self.layers[i], self.layers[i + 1]))
            bias = np.zeros((1, self.layers[i + 1]))
            
            self.weights.append(weight)
            self.biases.append(bias)
    
    def forward_propagation(self, X: np.ndarray) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        """
        Forward propagation through the network
        Returns activations and z-values for each layer
        """
        activations = [X]
        z_values = []
        
        current_input = X
        
        for i in range(len(self.weights)):
            z = current_input @ self.weights[i] + self.biases[i]
            z_values.append(z)
            
            if i == len(self.weights) - 1:  # Output layer (linear activation)
                activation = z
            else:  # Hidden layers
                activation = self.activation(z)
            
            activations.append(activation)
            current_input = activation
        
        return activations, z_values
    
    def backward_propagation(self, X: np.ndarray, y: np.ndarray, activations: List[np.ndarray], z_values: List[np.ndarray]):
        """
        Backward propagation to compute gradients
        """
        m = X.shape[0]
        weight_gradients = []
        bias_gradients = []
        
        # Initialize error for output layer
        delta = activations[-1] - y.reshape(-1, 1)
        
        # Backpropagate through layers
        for i in reversed(range(len(self.weights))):
            # Compute gradients
            dW = activations[i].T @ delta / m
            db = np.mean(delta, axis=0, keepdims=True)
            
            weight_gradients.insert(0, dW)
            bias_gradients.insert(0, db)
            
            # Propagate error to previous layer (except for input layer)
            if i > 0:
                delta = (delta @ self.weights[i].T) * self.activation_derivative(z_values[i-1])
        
        return weight_gradients, bias_gradients
    
    def fit(self, X: np.ndarray, y: np.ndarray, epochs: int = 1000, batch_size: Optional[int] = None, validation_data: Optional[Tuple] = None):
        """
        Train the neural network
        """
        if batch_size is None:
            batch_size = X.shape[0]
        
        start_time = time.time()
        
        for epoch in range(epochs):
            # Shuffle data
            indices = np.random.permutation(X.shape[0])
            X_shuffled = X[indices]
            y_shuffled = y[indices]
            
            epoch_loss = 0
            
            # Mini-batch training
            for i in range(0, X.shape[0], batch_size):
                batch_X = X_shuffled[i:i + batch_size]
                batch_y = y_shuffled[i:i + batch_size]
                
                # Forward propagation
                activations, z_values = self.forward_propagation(batch_X)
                
                # Compute loss
                batch_loss = np.mean((activations[-1].flatten() - batch_y) ** 2)
                epoch_loss += batch_loss
                
                # Backward propagation
                weight_gradients, bias_gradients = self.backward_propagation(batch_X, batch_y, activations, z_values)
                
                # Update parameters
                for j in range(len(self.weights)):
                    self.weights[j] -= self.learning_rate * weight_gradients[j]
                    self.biases[j] -= self.learning_rate * bias_gradients[j]
            
            # Record training history
            epoch_loss /= (X.shape[0] // batch_size)
            
            history_entry = {
                'epoch': epoch,
                'loss': epoch_loss
            }
            
            # Add validation metrics if provided
            if validation_data is not None:
                X_val, y_val = validation_data
                val_predictions = self.predict(X_val)
                val_loss = np.mean((val_predictions - y_val) ** 2)
                history_entry['val_loss'] = val_loss
            
            self.training_history.append(history_entry)
            
            # Print progress
            if epoch % 100 == 0 or epoch == epochs - 1:
                if validation_data is not None:
                    print(f"Epoch {epoch}: Loss = {epoch_loss:.6f}, Val Loss = {val_loss:.6f}")
                else:
                    print(f"Epoch {epoch}: Loss = {epoch_loss:.6f}")
        
        end_time = time.time()
        self.training_time = (end_time - start_time) * 1000
        
        return self
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions on new data
        """
        activations, _ = self.forward_propagation(X)
        return activations[-1].flatten()
    
    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate R² score
        """
        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        return r2

def normalize_features(X_train: np.ndarray, X_test: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Normalize features using z-score normalization
    """
    mean = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    
    X_train_norm = (X_train - mean) / (std + 1e-8)
    X_test_norm = (X_test - mean) / (std + 1e-8)
    
    return X_train_norm, X_test_norm

def evaluate_neural_networks(X_train, y_train, X_test, y_test) -> dict:
    """
    Evaluate different neural network configurations
    """
    results = {}
    
    # Normalize features
    X_train_norm, X_test_norm = normalize_features(X_train, X_test)
    
    # Configuration 1: Simple network
    nn1 = NeuralNetwork([5, 10, 1], activation='sigmoid', learning_rate=0.01)
    nn1.fit(X_train_norm, y_train, epochs=500, batch_size=32, validation_data=(X_test_norm, y_test))
    
    results['simple_network'] = {
        'architecture': [5, 10, 1],
        'activation': 'sigmoid',
        'train_r2': nn1.score(X_train_norm, y_train),
        'test_r2': nn1.score(X_test_norm, y_test),
        'train_mse': np.mean((nn1.predict(X_train_norm) - y_train) ** 2),
        'test_mse': np.mean((nn1.predict(X_test_norm) - y_test) ** 2),
        'training_time_ms': nn1.training_time,
        'epochs': len(nn1.training_history)
    }
    
    # Configuration 2: Deeper network
    nn2 = NeuralNetwork([5, 20, 10, 1], activation='relu', learning_rate=0.001)
    nn2.fit(X_train_norm, y_train, epochs=500, batch_size=16, validation_data=(X_test_norm, y_test))
    
    results['deep_network'] = {
        'architecture': [5, 20, 10, 1],
        'activation': 'relu',
        'train_r2': nn2.score(X_train_norm, y_train),
        'test_r2': nn2.score(X_test_norm, y_test),
        'train_mse': np.mean((nn2.predict(X_train_norm) - y_train) ** 2),
        'test_mse': np.mean((nn2.predict(X_test_norm) - y_test) ** 2),
        'training_time_ms': nn2.training_time,
        'epochs': len(nn2.training_history)
    }
    
    # Configuration 3: Wide network
    nn3 = NeuralNetwork([5, 50, 1], activation='tanh', learning_rate=0.005)
    nn3.fit(X_train_norm, y_train, epochs=300, batch_size=64, validation_data=(X_test_norm, y_test))
    
    results['wide_network'] = {
        'architecture': [5, 50, 1],
        'activation': 'tanh',
        'train_r2': nn3.score(X_train_norm, y_train),
        'test_r2': nn3.score(X_test_norm, y_test),
        'train_mse': np.mean((nn3.predict(X_train_norm) - y_train) ** 2),
        'test_mse': np.mean((nn3.predict(X_test_norm) - y_test) ** 2),
        'training_time_ms': nn3.training_time,
        'epochs': len(nn3.training_history)
    }
    
    return results

if __name__ == "__main__":
    print("Neural Network Demo - Created by テストAI7")
    print("=" * 50)
    
    try:
        # Load datasets
        train_df = pd.read_csv('../datasets/training_data.csv')
        test_df = pd.read_csv('../datasets/test_data.csv')
        
        feature_cols = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
        X_train = train_df[feature_cols].values
        y_train = train_df['target'].values
        X_test = test_df[feature_cols].values
        y_test = test_df['target'].values
        
        print(f"Training data shape: {X_train.shape}")
        print(f"Test data shape: {X_test.shape}")
        
        # Evaluate neural networks
        results = evaluate_neural_networks(X_train, y_train, X_test, y_test)
        
        print("\nNeural Network Evaluation Results:")
        print("-" * 45)
        
        for model_name, metrics in results.items():
            print(f"\n{model_name.upper()}:")
            print(f"  Architecture: {metrics['architecture']}")
            print(f"  Activation: {metrics['activation']}")
            print(f"  Train R²: {metrics['train_r2']:.6f}")
            print(f"  Test R²: {metrics['test_r2']:.6f}")
            print(f"  Train MSE: {metrics['train_mse']:.6f}")
            print(f"  Test MSE: {metrics['test_mse']:.6f}")
            print(f"  Training Time: {metrics['training_time_ms']:.1f} ms")
            print(f"  Epochs: {metrics['epochs']}")
        
    except FileNotFoundError:
        print("Dataset files not found. Please ensure training_data.csv and test_data.csv exist in ../datasets/")
    except Exception as e:
        print(f"Error: {e}")