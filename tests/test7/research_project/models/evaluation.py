#!/usr/bin/env python3
"""
Model Evaluation Framework
Created by: テストAI7
Comprehensive evaluation and comparison of machine learning models
"""

import numpy as np
import pandas as pd
import time
import json
from typing import Dict, List, Tuple, Any, Optional
from linear_model import LinearRegression, PolynomialFeatures
from neural_network import NeuralNetwork, normalize_features

class ModelEvaluator:
    """
    Comprehensive model evaluation framework
    """
    
    def __init__(self):
        self.results = {}
        self.evaluation_time = None
        self.models = {}
    
    def load_data(self, train_path: str, test_path: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Load and prepare data for evaluation
        """
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)
        
        feature_cols = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
        
        X_train = train_df[feature_cols].values
        y_train = train_df['target'].values
        X_test = test_df[feature_cols].values
        y_test = test_df['target'].values
        
        return X_train, y_train, X_test, y_test
    
    def calculate_metrics(self, y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
        """
        Calculate comprehensive evaluation metrics
        """
        mse = np.mean((y_true - y_pred) ** 2)
        rmse = np.sqrt(mse)
        mae = np.mean(np.abs(y_true - y_pred))
        
        # R² Score
        ss_res = np.sum((y_true - y_pred) ** 2)
        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        
        # Adjusted R² (requires number of features)
        n = len(y_true)
        p = 5  # number of features
        adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - p - 1))
        
        # Mean Absolute Percentage Error
        mape = np.mean(np.abs((y_true - y_pred) / (y_true + 1e-8))) * 100
        
        # Explained Variance Score
        var_y = np.var(y_true)
        var_residual = np.var(y_true - y_pred)
        explained_variance = 1 - (var_residual / var_y)
        
        return {
            'mse': mse,
            'rmse': rmse,
            'mae': mae,
            'r2': r2,
            'adjusted_r2': adj_r2,
            'mape': mape,
            'explained_variance': explained_variance
        }
    
    def evaluate_linear_models(self, X_train, y_train, X_test, y_test) -> Dict:
        """
        Evaluate linear regression models
        """
        linear_results = {}
        
        # 1. Standard Linear Regression (Analytical)
        start_time = time.time()
        lr_analytical = LinearRegression()
        lr_analytical.fit_analytical(X_train, y_train)
        
        train_pred = lr_analytical.predict(X_train)
        test_pred = lr_analytical.predict(X_test)
        
        linear_results['linear_analytical'] = {
            'model_type': 'Linear Regression (Analytical)',
            'train_metrics': self.calculate_metrics(y_train, train_pred),
            'test_metrics': self.calculate_metrics(y_test, test_pred),
            'training_time_ms': lr_analytical.training_time,
            'prediction_time_ms': (time.time() - start_time) * 1000,
            'parameters': {
                'weights': lr_analytical.weights.tolist(),
                'bias': float(lr_analytical.bias)
            }
        }
        
        # 2. Linear Regression (Gradient Descent)
        lr_gd = LinearRegression(learning_rate=0.01, max_iterations=1000)
        lr_gd.fit_gradient_descent(X_train, y_train)
        
        train_pred_gd = lr_gd.predict(X_train)
        test_pred_gd = lr_gd.predict(X_test)
        
        linear_results['linear_gradient_descent'] = {
            'model_type': 'Linear Regression (Gradient Descent)',
            'train_metrics': self.calculate_metrics(y_train, train_pred_gd),
            'test_metrics': self.calculate_metrics(y_test, test_pred_gd),
            'training_time_ms': lr_gd.training_time,
            'iterations': len(lr_gd.training_history),
            'convergence': lr_gd.training_history[-1]['loss'] if lr_gd.training_history else None
        }
        
        # 3. Polynomial Regression
        poly = PolynomialFeatures(degree=2)
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.fit_transform(X_test)
        
        lr_poly = LinearRegression()
        lr_poly.fit_analytical(X_train_poly, y_train)
        
        train_pred_poly = lr_poly.predict(X_train_poly)
        test_pred_poly = lr_poly.predict(X_test_poly)
        
        linear_results['polynomial_regression'] = {
            'model_type': 'Polynomial Regression (Degree 2)',
            'train_metrics': self.calculate_metrics(y_train, train_pred_poly),
            'test_metrics': self.calculate_metrics(y_test, test_pred_poly),
            'training_time_ms': lr_poly.training_time,
            'n_features': X_train_poly.shape[1],
            'feature_names': poly.feature_names
        }
        
        self.models['linear'] = {
            'analytical': lr_analytical,
            'gradient_descent': lr_gd,
            'polynomial': lr_poly
        }
        
        return linear_results
    
    def evaluate_neural_networks(self, X_train, y_train, X_test, y_test) -> Dict:
        """
        Evaluate neural network models
        """
        nn_results = {}
        
        # Normalize features for neural networks
        X_train_norm, X_test_norm = normalize_features(X_train, X_test)
        
        # Neural Network configurations
        configs = [
            {'name': 'simple_nn', 'layers': [5, 10, 1], 'activation': 'sigmoid', 'lr': 0.01, 'epochs': 300},
            {'name': 'deep_nn', 'layers': [5, 20, 10, 1], 'activation': 'relu', 'lr': 0.001, 'epochs': 400},
            {'name': 'wide_nn', 'layers': [5, 50, 1], 'activation': 'tanh', 'lr': 0.005, 'epochs': 250}
        ]
        
        for config in configs:
            print(f"Training {config['name']}...")
            
            nn = NeuralNetwork(
                layers=config['layers'],
                activation=config['activation'],
                learning_rate=config['lr']
            )
            
            nn.fit(
                X_train_norm, y_train,
                epochs=config['epochs'],
                batch_size=32,
                validation_data=(X_test_norm, y_test)
            )
            
            train_pred = nn.predict(X_train_norm)
            test_pred = nn.predict(X_test_norm)
            
            nn_results[config['name']] = {
                'model_type': f"Neural Network {config['layers']}",
                'activation': config['activation'],
                'train_metrics': self.calculate_metrics(y_train, train_pred),
                'test_metrics': self.calculate_metrics(y_test, test_pred),
                'training_time_ms': nn.training_time,
                'epochs_trained': len(nn.training_history),
                'final_loss': nn.training_history[-1]['loss'] if nn.training_history else None,
                'architecture': config['layers']
            }
            
            # Store model
            if 'neural_networks' not in self.models:
                self.models['neural_networks'] = {}
            self.models['neural_networks'][config['name']] = nn
        
        return nn_results
    
    def cross_validation_simulation(self, X, y, model_class, n_folds: int = 5) -> Dict:
        """
        Simulate k-fold cross validation (simplified version)
        """
        fold_size = len(X) // n_folds
        cv_scores = []
        
        for fold in range(n_folds):
            # Create train/validation split
            start_idx = fold * fold_size
            end_idx = start_idx + fold_size
            
            X_val_fold = X[start_idx:end_idx]
            y_val_fold = y[start_idx:end_idx]
            
            X_train_fold = np.concatenate([X[:start_idx], X[end_idx:]])
            y_train_fold = np.concatenate([y[:start_idx], y[end_idx:]])
            
            # Train model
            if model_class == 'linear':
                model = LinearRegression()
                model.fit_analytical(X_train_fold, y_train_fold)
            elif model_class == 'neural':
                X_train_fold_norm, X_val_fold_norm = normalize_features(X_train_fold, X_val_fold)
                model = NeuralNetwork([5, 10, 1], learning_rate=0.01)
                model.fit(X_train_fold_norm, y_train_fold, epochs=200)
                X_val_fold = X_val_fold_norm
            
            # Evaluate
            val_pred = model.predict(X_val_fold)
            fold_score = model.score(X_val_fold, y_val_fold) if hasattr(model, 'score') else self.calculate_metrics(y_val_fold, val_pred)['r2']
            cv_scores.append(fold_score)
        
        return {
            'cv_scores': cv_scores,
            'mean_cv_score': np.mean(cv_scores),
            'std_cv_score': np.std(cv_scores)
        }
    
    def generate_comparison_report(self) -> Dict:
        """
        Generate comprehensive comparison report
        """
        if not self.results:
            raise ValueError("No evaluation results available. Run evaluate_all() first.")
        
        # Collect all model results
        all_models = {}
        
        if 'linear_models' in self.results:
            all_models.update(self.results['linear_models'])
        
        if 'neural_networks' in self.results:
            all_models.update(self.results['neural_networks'])
        
        # Best model selection
        best_test_r2 = -float('inf')
        best_model = None
        
        performance_ranking = []
        
        for model_name, model_results in all_models.items():
            test_r2 = model_results['test_metrics']['r2']
            test_mse = model_results['test_metrics']['mse']
            train_r2 = model_results['train_metrics']['r2']
            
            # Calculate overfitting score
            overfitting_score = train_r2 - test_r2
            
            performance_ranking.append({
                'model': model_name,
                'test_r2': test_r2,
                'test_mse': test_mse,
                'train_r2': train_r2,
                'overfitting_score': overfitting_score,
                'model_type': model_results['model_type']
            })
            
            if test_r2 > best_test_r2:
                best_test_r2 = test_r2
                best_model = model_name
        
        # Sort by test R²
        performance_ranking.sort(key=lambda x: x['test_r2'], reverse=True)
        
        return {
            'best_model': {
                'name': best_model,
                'test_r2': best_test_r2,
                'details': all_models[best_model] if best_model else None
            },
            'performance_ranking': performance_ranking,
            'model_comparison': all_models,
            'evaluation_summary': {
                'total_models_evaluated': len(all_models),
                'evaluation_time_ms': self.evaluation_time,
                'best_test_r2': best_test_r2,
                'evaluation_date': time.strftime('%Y-%m-%d %H:%M:%S')
            }
        }
    
    def evaluate_all(self, train_path: str, test_path: str) -> Dict:
        """
        Run comprehensive evaluation of all models
        """
        start_time = time.time()
        
        # Load data
        X_train, y_train, X_test, y_test = self.load_data(train_path, test_path)
        
        print("Evaluating Linear Models...")
        linear_results = self.evaluate_linear_models(X_train, y_train, X_test, y_test)
        
        print("Evaluating Neural Networks...")
        nn_results = self.evaluate_neural_networks(X_train, y_train, X_test, y_test)
        
        # Cross-validation
        print("Running Cross-Validation...")
        cv_linear = self.cross_validation_simulation(X_train, y_train, 'linear')
        cv_neural = self.cross_validation_simulation(X_train, y_train, 'neural')
        
        end_time = time.time()
        self.evaluation_time = (end_time - start_time) * 1000
        
        self.results = {
            'linear_models': linear_results,
            'neural_networks': nn_results,
            'cross_validation': {
                'linear': cv_linear,
                'neural': cv_neural
            },
            'data_info': {
                'train_samples': X_train.shape[0],
                'test_samples': X_test.shape[0],
                'features': X_train.shape[1],
                'target_range': {
                    'min': float(np.min(y_train)),
                    'max': float(np.max(y_train)),
                    'mean': float(np.mean(y_train)),
                    'std': float(np.std(y_train))
                }
            }
        }
        
        return self.results
    
    def save_results(self, filepath: str):
        """
        Save evaluation results to JSON file
        """
        if not self.results:
            raise ValueError("No results to save. Run evaluate_all() first.")
        
        # Generate comparison report
        comparison_report = self.generate_comparison_report()
        
        # Combine all results
        full_results = {
            'evaluation_results': self.results,
            'comparison_report': comparison_report
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(full_results, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    print("Model Evaluation Framework - Created by テストAI7")
    print("=" * 60)
    
    try:
        evaluator = ModelEvaluator()
        
        # Run comprehensive evaluation
        results = evaluator.evaluate_all(
            '../datasets/training_data.csv',
            '../datasets/test_data.csv'
        )
        
        # Generate and display comparison report
        comparison = evaluator.generate_comparison_report()
        
        print("\nEVALUATION COMPLETED!")
        print("=" * 40)
        print(f"Total models evaluated: {comparison['evaluation_summary']['total_models_evaluated']}")
        print(f"Evaluation time: {comparison['evaluation_summary']['evaluation_time_ms']:.1f} ms")
        print(f"Best model: {comparison['best_model']['name']}")
        print(f"Best test R²: {comparison['best_model']['test_r2']:.6f}")
        
        print("\nPERFORMANCE RANKING:")
        print("-" * 30)
        for i, model in enumerate(comparison['performance_ranking'][:5]):  # Top 5
            print(f"{i+1}. {model['model']} (R² = {model['test_r2']:.6f})")
        
        # Save results
        evaluator.save_results('evaluation_results.json')
        print("\nResults saved to evaluation_results.json")
        
    except FileNotFoundError:
        print("Dataset files not found. Please ensure datasets exist in ../datasets/")
    except Exception as e:
        print(f"Error during evaluation: {e}")