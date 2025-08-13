#!/usr/bin/env python3
"""
Lab Environment 1 - Machine Learning Model
数値計算結果の学習と予測モデル
"""

import numpy as np
import pandas as pd
import json
import joblib
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import logging
import time
from typing import Dict, List, Tuple, Any

class Lab1MLModel:
    """Lab Environment 1用機械学習モデル"""
    
    def __init__(self):
        self.models = {}
        self.scalers = {}
        self.feature_names = [
            'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
            'series_terms', 'integration_points', 'convergence_iteration'
        ]
        self.target_names = ['series_sum', 'integration_result', 'computation_time']
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def generate_training_data(self, n_samples: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """訓練データの生成"""
        self.logger.info(f"訓練データ生成開始: {n_samples}サンプル")
        
        # パラメータの範囲を設定
        np.random.seed(42)
        
        # 特徴量生成
        features = []
        targets = []
        
        for i in range(n_samples):
            # パラメータのバリエーション
            alpha = np.random.uniform(300, 500)
            beta = np.random.uniform(200, 300)
            gamma = np.random.uniform(150, 250)
            delta = np.random.uniform(70, 100)
            epsilon = np.random.uniform(50, 80)
            zeta = np.random.uniform(20, 40)
            
            series_terms = np.random.randint(30, 50)
            integration_points = np.random.randint(5000, 15000)
            convergence_iteration = np.random.randint(5, 25)
            
            # 簡化された計算モデル（実際の計算の近似）
            series_sum = self._approximate_series_sum(alpha, beta, series_terms)
            integration_result = self._approximate_integration(gamma, delta)
            computation_time = self._estimate_computation_time(
                series_terms, integration_points, alpha, beta
            )
            
            features.append([
                alpha, beta, gamma, delta, epsilon, zeta,
                series_terms, integration_points, convergence_iteration
            ])
            targets.append([series_sum, integration_result, computation_time])
            
        return np.array(features), np.array(targets)
        
    def _approximate_series_sum(self, alpha: float, beta: float, terms: int) -> float:
        """無限級数の近似計算"""
        # 実際の計算の簡化版
        series_sum = 0
        for n in range(1, min(terms, 20)):  # 計算量削減のため20項まで
            try:
                term = (alpha ** n) / (np.math.factorial(n) * (beta ** (n/2)))
                if not np.isfinite(term):
                    break
                series_sum += term
            except (OverflowError, ZeroDivisionError):
                break
        return series_sum
        
    def _approximate_integration(self, gamma: float, delta: float) -> float:
        """数値積分の近似計算"""
        # 解析解の近似
        if gamma != delta and gamma + delta != 0:
            result = (
                np.sin((gamma - delta) * np.pi) / (2 * (gamma - delta)) +
                np.sin((gamma + delta) * np.pi) / (2 * (gamma + delta))
            )
        else:
            result = 0.0
        return result
        
    def _estimate_computation_time(self, series_terms: int, integration_points: int,
                                 alpha: float, beta: float) -> float:
        """計算時間の推定"""
        # 複雑度に基づく時間推定
        series_complexity = series_terms * np.log(alpha + beta)
        integration_complexity = integration_points * 0.001
        return series_complexity + integration_complexity + np.random.normal(0, 100)
        
    def train_models(self, X: np.ndarray, y: np.ndarray) -> Dict[str, Any]:
        """複数モデルの訓練"""
        self.logger.info("機械学習モデル訓練開始")
        training_results = {}
        
        # データ分割
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # 特徴量スケーリング
        self.scalers['features'] = StandardScaler()
        X_train_scaled = self.scalers['features'].fit_transform(X_train)
        X_test_scaled = self.scalers['features'].transform(X_test)
        
        # モデル定義
        model_configs = {
            'random_forest': RandomForestRegressor(
                n_estimators=100, max_depth=10, random_state=42
            ),
            'gradient_boosting': GradientBoostingRegressor(
                n_estimators=100, max_depth=6, random_state=42
            ),
            'neural_network': MLPRegressor(
                hidden_layer_sizes=(100, 50), max_iter=500, random_state=42
            )
        }
        
        # 各ターゲットについて各モデルを訓練
        for target_idx, target_name in enumerate(self.target_names):
            training_results[target_name] = {}
            
            for model_name, model in model_configs.items():
                start_time = time.time()
                
                # モデル訓練
                model.fit(X_train_scaled, y_train[:, target_idx])
                
                # 予測
                y_pred_train = model.predict(X_train_scaled)
                y_pred_test = model.predict(X_test_scaled)
                
                # 評価指標計算
                train_mse = mean_squared_error(y_train[:, target_idx], y_pred_train)
                test_mse = mean_squared_error(y_test[:, target_idx], y_pred_test)
                train_mae = mean_absolute_error(y_train[:, target_idx], y_pred_train)
                test_mae = mean_absolute_error(y_test[:, target_idx], y_pred_test)
                train_r2 = r2_score(y_train[:, target_idx], y_pred_train)
                test_r2 = r2_score(y_test[:, target_idx], y_pred_test)
                
                # クロスバリデーション
                cv_scores = cross_val_score(
                    model, X_train_scaled, y_train[:, target_idx], 
                    cv=5, scoring='neg_mean_squared_error'
                )
                
                training_time = time.time() - start_time
                
                # 結果保存
                training_results[target_name][model_name] = {
                    'train_mse': train_mse,
                    'test_mse': test_mse,
                    'train_mae': train_mae,
                    'test_mae': test_mae,
                    'train_r2': train_r2,
                    'test_r2': test_r2,
                    'cv_mse_mean': -cv_scores.mean(),
                    'cv_mse_std': cv_scores.std(),
                    'training_time': training_time,
                    'model_params': model.get_params()
                }
                
                # モデル保存
                model_key = f"{target_name}_{model_name}"
                self.models[model_key] = model
                
                self.logger.info(
                    f"{target_name}-{model_name}: "
                    f"Test R2={test_r2:.4f}, MSE={test_mse:.4f}"
                )
        
        # 特徴量重要度分析（Random Forestのみ）
        feature_importance = {}
        for target_name in self.target_names:
            rf_model = self.models[f"{target_name}_random_forest"]
            if hasattr(rf_model, 'feature_importances_'):
                feature_importance[target_name] = {
                    feature: importance 
                    for feature, importance in zip(
                        self.feature_names, rf_model.feature_importances_
                    )
                }
        
        training_results['feature_importance'] = feature_importance
        training_results['model_summary'] = {
            'total_models': len(self.models),
            'feature_count': len(self.feature_names),
            'target_count': len(self.target_names),
            'training_samples': len(X_train),
            'test_samples': len(X_test)
        }
        
        self.logger.info("機械学習モデル訓練完了")
        return training_results
        
    def predict(self, features: np.ndarray, model_type: str = 'random_forest') -> Dict[str, float]:
        """予測実行"""
        if not self.models:
            raise ValueError("モデルが訓練されていません")
            
        # 特徴量スケーリング
        features_scaled = self.scalers['features'].transform(features.reshape(1, -1))
        
        predictions = {}
        for target_name in self.target_names:
            model_key = f"{target_name}_{model_type}"
            if model_key in self.models:
                pred = self.models[model_key].predict(features_scaled)[0]
                predictions[target_name] = pred
                
        return predictions
        
    def save_models(self, filepath_prefix: str = 'lab1_model'):
        """モデル保存"""
        model_data = {
            'models': self.models,
            'scalers': self.scalers,
            'feature_names': self.feature_names,
            'target_names': self.target_names
        }
        joblib.dump(model_data, f"{filepath_prefix}.pkl")
        self.logger.info(f"モデル保存完了: {filepath_prefix}.pkl")
        
    def load_models(self, filepath: str):
        """モデル読み込み"""
        model_data = joblib.load(filepath)
        self.models = model_data['models']
        self.scalers = model_data['scalers']
        self.feature_names = model_data['feature_names']
        self.target_names = model_data['target_names']
        self.logger.info(f"モデル読み込み完了: {filepath}")

def main():
    """メイン実行関数"""
    ml_model = Lab1MLModel()
    
    try:
        # 訓練データ生成
        X, y = ml_model.generate_training_data(1000)
        
        # モデル訓練
        training_results = ml_model.train_models(X, y)
        
        # 結果保存
        with open('ml_training_results.json', 'w', encoding='utf-8') as f:
            json.dump(training_results, f, indent=2, ensure_ascii=False, default=str)
            
        # モデル保存
        ml_model.save_models('lab1_ml_model')
        
        # サンプル予測
        sample_features = np.array([427, 256, 198, 87, 64, 31, 50, 10000, 15])
        predictions = ml_model.predict(sample_features)
        
        print("機械学習モデル訓練完了")
        print("サンプル予測結果:")
        for target, pred in predictions.items():
            print(f"  {target}: {pred:.6f}")
            
    except Exception as e:
        logging.error(f"機械学習実行中にエラー: {e}")
        raise

if __name__ == "__main__":
    main()