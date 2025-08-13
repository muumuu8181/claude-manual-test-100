#!/usr/bin/env python3
import json
import random
import numpy as np
import csv
from scipy import stats
import time

def run_monte_carlo_simulations(iterations=1000):
    """1000回のモンテカルロシミュレーション"""
    results = []
    
    # 基本パラメータ
    x, y, z, w, v = 312, 189, 147, 78, 33
    
    for i in range(iterations):
        # わずかにパラメータを変動させてシミュレーション
        x_sim = x + random.uniform(-5, 5)
        y_sim = y + random.uniform(-5, 5)
        z_sim = z + random.uniform(-5, 5)
        
        # experiment_1タイプの計算を実行
        try:
            result = (x_sim**3 + y_sim**3) / (z_sim**2 - w**2) + np.log2(v)
            results.append(result)
        except:
            results.append(0)  # エラー時は0
    
    return results

def analyze_distribution(data):
    """分布分析"""
    mean = np.mean(data)
    std = np.std(data)
    skew = stats.skew(data)
    kurt = stats.kurtosis(data)
    
    # 正規性検定
    shapiro_stat, shapiro_p = stats.shapiro(data[:5000] if len(data) > 5000 else data)
    
    analysis = {
        "mean": mean,
        "standard_deviation": std,
        "skewness": skew,
        "kurtosis": kurt,
        "normality_test": {
            "shapiro_statistic": shapiro_stat,
            "shapiro_p_value": shapiro_p,
            "is_normal": shapiro_p > 0.05
        },
        "percentiles": {
            "5th": np.percentile(data, 5),
            "25th": np.percentile(data, 25),
            "50th": np.percentile(data, 50),
            "75th": np.percentile(data, 75),
            "95th": np.percentile(data, 95)
        }
    }
    
    return analysis

def calculate_confidence_intervals(data, confidence_levels=[0.90, 0.95, 0.99]):
    """信頼区間の計算"""
    intervals = {}
    
    for confidence in confidence_levels:
        alpha = 1 - confidence
        mean = np.mean(data)
        sem = stats.sem(data)  # 標準誤差
        
        # t分布を使用
        t_critical = stats.t.ppf(1 - alpha/2, len(data) - 1)
        margin_error = t_critical * sem
        
        intervals[f"{confidence*100:.0f}%"] = {
            "lower_bound": mean - margin_error,
            "upper_bound": mean + margin_error,
            "margin_of_error": margin_error
        }
    
    return intervals

if __name__ == "__main__":
    start_time = time.time()
    
    # 1000回のシミュレーション実行
    print("モンテカルロシミュレーション開始...")
    simulation_results = run_monte_carlo_simulations(1000)
    
    # 分布分析
    distribution_analysis = analyze_distribution(simulation_results)
    
    # 信頼区間計算
    confidence_intervals = calculate_confidence_intervals(simulation_results)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # monte_carlo_results.jsonの作成
    with open('project_data/simulation/monte_carlo_results.json', 'w') as f:
        json.dump({
            "simulation_parameters": {
                "iterations": 1000,
                "base_parameters": {"x": 312, "y": 189, "z": 147, "w": 78, "v": 33},
                "parameter_variation": "±5 for x, y, z"
            },
            "results": simulation_results,
            "execution_time_seconds": execution_time,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }, f, indent=2)
    
    # distribution_analysis.txtの作成
    with open('project_data/simulation/distribution_analysis.txt', 'w', encoding='utf-8') as f:
        f.write("シミュレーション結果の分布分析\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"サンプル数: {len(simulation_results)}\n")
        f.write(f"平均値: {distribution_analysis['mean']:.6f}\n")
        f.write(f"標準偏差: {distribution_analysis['standard_deviation']:.6f}\n")
        f.write(f"歪度: {distribution_analysis['skewness']:.6f}\n")
        f.write(f"尖度: {distribution_analysis['kurtosis']:.6f}\n\n")
        
        f.write("正規性検定 (Shapiro-Wilk):\n")
        f.write(f"  統計量: {distribution_analysis['normality_test']['shapiro_statistic']:.6f}\n")
        f.write(f"  p値: {distribution_analysis['normality_test']['shapiro_p_value']:.6f}\n")
        f.write(f"  正規分布判定: {'Yes' if distribution_analysis['normality_test']['is_normal'] else 'No'}\n\n")
        
        f.write("パーセンタイル:\n")
        for percentile, value in distribution_analysis['percentiles'].items():
            f.write(f"  {percentile}: {value:.6f}\n")
    
    # confidence_intervals.csvの作成
    with open('project_data/simulation/confidence_intervals.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['信頼水準', '下限', '上限', '誤差範囲'])
        
        for level, interval in confidence_intervals.items():
            writer.writerow([
                level,
                f"{interval['lower_bound']:.6f}",
                f"{interval['upper_bound']:.6f}",
                f"{interval['margin_of_error']:.6f}"
            ])
    
    print(f"シミュレーションファイル作成完了 ({execution_time:.2f}秒)")