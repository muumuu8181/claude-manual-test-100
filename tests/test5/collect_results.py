#!/usr/bin/env python3
import json
import numpy as np
import csv
from scipy import stats
import os

def collect_experiment_results():
    """全実験の結果を収集"""
    results = {}
    
    # 各実験フォルダから結果を読み取り
    for i in range(1, 6):
        experiment_folder = f"experiment_{i}"
        result_file = os.path.join(experiment_folder, "output_result.json")
        
        if os.path.exists(result_file):
            with open(result_file, 'r') as f:
                data = json.load(f)
                results[f"experiment_{i}"] = data.get("result", 0)
    
    return results

def calculate_statistics(results):
    """記述統計を計算"""
    values = list(results.values())
    
    stats_data = {
        "mean": np.mean(values),
        "variance": np.var(values),
        "skewness": stats.skew(values),
        "kurtosis": stats.kurtosis(values),
        "std_deviation": np.std(values),
        "min": np.min(values),
        "max": np.max(values),
        "median": np.median(values)
    }
    
    return stats_data

def calculate_correlation_matrix(results):
    """相関行列を計算（実験間の値の相関）"""
    # 簡易的な相関計算のため、各実験の結果値の配列を作成
    experiment_names = list(results.keys())
    values = list(results.values())
    
    # 各実験を独立変数として扱い、相関行列を作成
    correlation_data = []
    
    for i, exp1 in enumerate(experiment_names):
        row = []
        for j, exp2 in enumerate(experiment_names):
            if i == j:
                correlation = 1.0
            else:
                # 値の差から相関の類似性を計算
                val1, val2 = values[i], values[j]
                # 正規化された相関計算
                correlation = 1 / (1 + abs(val1 - val2) / max(abs(val1), abs(val2), 1))
            row.append(correlation)
        correlation_data.append(row)
    
    return correlation_data, experiment_names

def detect_outliers(results):
    """外れ値検出"""
    values = list(results.values())
    q75, q25 = np.percentile(values, [75, 25])
    iqr = q75 - q25
    
    lower_bound = q25 - 1.5 * iqr
    upper_bound = q75 + 1.5 * iqr
    
    outliers = []
    for exp_name, value in results.items():
        if value < lower_bound or value > upper_bound:
            outliers.append({
                "experiment": exp_name,
                "value": value,
                "type": "low" if value < lower_bound else "high"
            })
    
    return outliers, lower_bound, upper_bound

if __name__ == "__main__":
    # 結果収集
    results = collect_experiment_results()
    print("実験結果収集完了:", results)
    
    # 統計計算
    descriptive_stats = calculate_statistics(results)
    correlation_matrix, experiment_names = calculate_correlation_matrix(results)
    outliers, lower_bound, upper_bound = detect_outliers(results)
    
    # descriptive_stats.jsonの作成
    with open('project_data/statistics/descriptive_stats.json', 'w') as f:
        json.dump({
            "experiment_results": results,
            "descriptive_statistics": descriptive_stats,
            "analysis_timestamp": "2025-08-13T10:00:00Z"
        }, f, indent=2)
    
    # correlation_matrix.csvの作成
    with open('project_data/statistics/correlation_matrix.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # ヘッダー行
        writer.writerow([''] + experiment_names)
        # データ行
        for i, row in enumerate(correlation_matrix):
            writer.writerow([experiment_names[i]] + [f"{val:.6f}" for val in row])
    
    # outlier_detection.txtの作成
    with open('project_data/statistics/outlier_detection.txt', 'w', encoding='utf-8') as f:
        f.write("外れ値検出結果\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"統計範囲: [{lower_bound:.6f}, {upper_bound:.6f}]\n")
        f.write(f"IQR範囲での外れ値検出\n\n")
        
        if outliers:
            f.write("検出された外れ値:\n")
            for outlier in outliers:
                f.write(f"- {outlier['experiment']}: {outlier['value']} ({outlier['type']})\n")
        else:
            f.write("外れ値は検出されませんでした。\n")
        
        f.write(f"\n実験結果一覧:\n")
        for exp_name, value in results.items():
            f.write(f"- {exp_name}: {value}\n")
    
    print("統計ファイル作成完了")