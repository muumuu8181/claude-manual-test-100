#!/usr/bin/env python3
"""
Lab Environment 2 - ML Model for Matrix Analysis
行列演算結果の機械学習による予測・分析
"""

import numpy as np
import pandas as pd
import json
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import logging
import time

class Lab2MatrixMLModel:
    """行列演算結果予測モデル"""
    
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def generate_synthetic_data(self, n_samples=1000):
        """合成データ生成"""
        np.random.seed(42)
        
        # 特徴量: 行列パラメータ
        features = []
        targets = []
        
        for i in range(n_samples):
            alpha = np.random.uniform(300, 500)
            beta = np.random.uniform(200, 300)
            gamma = np.random.uniform(150, 250)
            delta = np.random.uniform(70, 100)
            epsilon = np.random.uniform(50, 80)
            zeta = np.random.uniform(20, 40)
            
            # 予測対象: 条件数、計算時間、再構成誤差
            condition_number = alpha * beta / (delta * epsilon) + np.random.normal(0, 10)
            computation_time = (alpha + beta + gamma) * 0.1 + np.random.normal(0, 5)
            reconstruction_error = 1e-12 * np.random.exponential(1)
            
            features.append([alpha, beta, gamma, delta, epsilon, zeta])
            targets.append([condition_number, computation_time, reconstruction_error])
            
        return np.array(features), np.array(targets)
        
    def train_model(self):
        """モデル訓練"""
        X, y = self.generate_synthetic_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # 条件数予測モデル
        self.model.fit(X_train_scaled, y_train[:, 0])
        y_pred = self.model.predict(X_test_scaled)
        
        mse = mean_squared_error(y_test[:, 0], y_pred)
        r2 = r2_score(y_test[:, 0], y_pred)
        
        return {
            'mse': mse,
            'r2_score': r2,
            'feature_importance': self.model.feature_importances_.tolist()
        }
        
def main():
    model = Lab2MatrixMLModel()
    results = model.train_model()
    
    with open('ml_training_results.json', 'w') as f:
        json.dump(results, f, indent=2)
        
    print(f"モデル訓練完了: R2={results['r2_score']:.4f}")

if __name__ == "__main__":
    main()