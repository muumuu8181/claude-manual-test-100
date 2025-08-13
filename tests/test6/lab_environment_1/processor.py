#!/usr/bin/env python3
"""
Lab Environment 1 - Data Processor
高精度数値計算実装：無限級数とフレネル積分
"""

import math
import time
import json
import csv
from decimal import Decimal, getcontext
from typing import Dict, List, Tuple, Any
import numpy as np
from scipy import integrate
import logging

# 高精度計算設定
getcontext().prec = 50

class LabEnvironment1Processor:
    """Lab Environment 1の数値計算プロセッサ"""
    
    def __init__(self):
        self.alpha = 427
        self.beta = 256
        self.gamma = 198
        self.delta = 87
        self.epsilon = 64
        self.zeta = 31
        
        # ログ設定
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def infinite_series_calculation(self) -> Dict[str, Any]:
        """
        計算: Σ(n=1 to 50) [α^n / (n! * β^(n/2))]
        収束判定（誤差10^-8以下）を実装
        """
        self.logger.info("無限級数計算開始")
        start_time = time.perf_counter_ns()
        
        series_sum = Decimal(0)
        previous_sum = Decimal(0)
        convergence_achieved = False
        convergence_iteration = 0
        
        terms_data = []
        
        for n in range(1, 51):
            # α^n の計算
            alpha_power = Decimal(self.alpha) ** n
            
            # n! の計算
            factorial = Decimal(math.factorial(n))
            
            # β^(n/2) の計算
            beta_power = Decimal(self.beta) ** (Decimal(n) / Decimal(2))
            
            # 項の計算
            term = alpha_power / (factorial * beta_power)
            series_sum += term
            
            # 収束判定
            if n > 1:
                error = abs(series_sum - previous_sum)
                if error < Decimal('1e-8') and not convergence_achieved:
                    convergence_achieved = True
                    convergence_iteration = n
                    
            terms_data.append({
                'n': n,
                'term_value': float(term),
                'partial_sum': float(series_sum),
                'alpha_power': float(alpha_power),
                'factorial': float(factorial),
                'beta_power': float(beta_power)
            })
            
            previous_sum = series_sum
            
        end_time = time.perf_counter_ns()
        computation_time_us = (end_time - start_time) / 1000
        
        result = {
            'final_sum': float(series_sum),
            'precision_digits': 7,
            'computation_time_microseconds': computation_time_us,
            'convergence_achieved': convergence_achieved,
            'convergence_iteration': convergence_iteration,
            'total_terms': 50,
            'terms_data': terms_data[:10],  # 最初の10項のみ保存
            'error_estimate': float(abs(series_sum - previous_sum)) if len(terms_data) > 1 else 0.0
        }
        
        self.logger.info(f"無限級数計算完了: 結果={result['final_sum']:.7f}")
        return result
        
    def numerical_integration(self) -> Dict[str, Any]:
        """
        計算: ∫(0 to π) sin(γx) * cos(δx) dx の数値積分
        """
        self.logger.info("数値積分計算開始")
        start_time = time.perf_counter_ns()
        
        def integrand(x):
            return math.sin(self.gamma * x) * math.cos(self.delta * x)
        
        # 複数の積分手法で計算
        results = {}
        
        # scipy.integrate.quad による適応的数値積分
        integral_result, error_estimate = integrate.quad(
            integrand, 0, math.pi, epsabs=1e-10, epsrel=1e-10
        )
        
        # 台形則による数値積分（比較用）
        n_points = 10000
        x_points = np.linspace(0, math.pi, n_points)
        y_points = [integrand(x) for x in x_points]
        trapezoidal_result = np.trapz(y_points, x_points)
        
        # シンプソン則による数値積分（比較用）
        simpson_result = integrate.simpson(y_points, x_points)
        
        end_time = time.perf_counter_ns()
        computation_time_us = (end_time - start_time) / 1000
        
        # 解析解の計算（検証用）
        # ∫sin(γx)cos(δx)dx = [sin((γ-δ)x)/(2(γ-δ)) + sin((γ+δ)x)/(2(γ+δ))]
        gamma_minus_delta = self.gamma - self.delta
        gamma_plus_delta = self.gamma + self.delta
        
        if gamma_minus_delta != 0 and gamma_plus_delta != 0:
            analytical_result = (
                (math.sin(gamma_minus_delta * math.pi) / (2 * gamma_minus_delta)) +
                (math.sin(gamma_plus_delta * math.pi) / (2 * gamma_plus_delta))
            )
        else:
            analytical_result = None
            
        result = {
            'adaptive_quadrature': round(integral_result, 7),
            'trapezoidal_rule': round(trapezoidal_result, 7),
            'simpson_rule': round(simpson_result, 7),
            'analytical_solution': round(analytical_result, 7) if analytical_result else None,
            'error_estimate': error_estimate,
            'computation_time_microseconds': computation_time_us,
            'integration_bounds': [0.0, math.pi],
            'function_parameters': {
                'gamma': self.gamma,
                'delta': self.delta
            },
            'numerical_points': n_points,
            'precision_achieved': error_estimate < 1e-8
        }
        
        self.logger.info(f"数値積分計算完了: 結果={result['adaptive_quadrature']:.7f}")
        return result
        
    def run_full_computation(self) -> Dict[str, Any]:
        """完全な計算実行"""
        self.logger.info("Lab Environment 1 完全計算開始")
        
        # 無限級数計算
        series_result = self.infinite_series_calculation()
        
        # 数値積分計算
        integration_result = self.numerical_integration()
        
        # 結果統合
        full_result = {
            'environment': 'lab_environment_1',
            'parameters': {
                'alpha': self.alpha,
                'beta': self.beta,
                'gamma': self.gamma,
                'delta': self.delta,
                'epsilon': self.epsilon,
                'zeta': self.zeta
            },
            'series_calculation': series_result,
            'numerical_integration': integration_result,
            'total_computation_time': (
                series_result['computation_time_microseconds'] + 
                integration_result['computation_time_microseconds']
            ),
            'overall_precision': min(
                7,  # 小数点第7位
                -int(math.log10(max(
                    series_result.get('error_estimate', 1e-7),
                    integration_result.get('error_estimate', 1e-7)
                )))
            )
        }
        
        self.logger.info("Lab Environment 1 完全計算完了")
        return full_result

def main():
    """メイン実行関数"""
    processor = LabEnvironment1Processor()
    
    try:
        # 計算実行
        results = processor.run_full_computation()
        
        # 結果保存
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
            
        # メトリクス保存
        metrics_data = [
            ['metric_name', 'value', 'unit', 'timestamp'],
            ['series_sum', results['series_calculation']['final_sum'], 'numeric', time.time()],
            ['integration_result', results['numerical_integration']['adaptive_quadrature'], 'numeric', time.time()],
            ['total_time', results['total_computation_time'], 'microseconds', time.time()],
            ['precision_digits', results['overall_precision'], 'digits', time.time()],
            ['convergence', results['series_calculation']['convergence_achieved'], 'boolean', time.time()]
        ]
        
        with open('metrics.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(metrics_data)
            
        print("計算完了。結果はresults.jsonとmetrics.csvに保存されました。")
        print(f"無限級数の和: {results['series_calculation']['final_sum']:.7f}")
        print(f"数値積分の結果: {results['numerical_integration']['adaptive_quadrature']:.7f}")
        
    except Exception as e:
        logging.error(f"計算実行中にエラー: {e}")
        raise

if __name__ == "__main__":
    main()