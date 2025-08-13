#!/usr/bin/env python3
"""
Performance Analysis Script
テストAI4によるパフォーマンス分析スクリプト
"""

import math
import time
import json
import random
import psutil
import os
import gc
from pathlib import Path

def fibonacci(n):
    """フィボナッチ数列のn番目を計算"""
    if n <= 2:
        return 1
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n-1]

def measure_execution_time(func, *args, **kwargs):
    """実行時間を測定する関数"""
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # ミリ秒に変換
    return result, execution_time

def estimate_memory_usage(func, *args, **kwargs):
    """メモリ使用量を推定する関数"""
    gc.collect()  # ガベージコレクション実行
    process = psutil.Process()
    memory_before = process.memory_info().rss
    
    result = func(*args, **kwargs)
    
    gc.collect()
    memory_after = process.memory_info().rss
    memory_used = memory_after - memory_before
    
    return result, memory_used

def analysis_1():
    """Analysis 1: ((a+b)*c - d*e) / (a-b)"""
    a, b, c, d, e = 213, 97, 45, 28, 11
    return ((a + b) * c - d * e) / (a - b)

def analysis_2():
    """Analysis 2: a^3 - b^2 + c^2 - d^2 + e^3"""
    a, b, c, d, e = 213, 97, 45, 28, 11
    return a**3 - b**2 + c**2 - d**2 + e**3

def analysis_3():
    """Analysis 3: √(a^2 + b^2) * sin(c°)"""
    a, b, c, d, e = 213, 97, 45, 28, 11
    return math.sqrt(a**2 + b**2) * math.sin(math.radians(c))

def analysis_4():
    """Analysis 4: log(a*b) + ln(c*d) - log2(e)"""
    a, b, c, d, e = 213, 97, 45, 28, 11
    return math.log10(a*b) + math.log(c*d) - math.log2(e)

def analysis_5():
    """Analysis 5: Σ(i=1 to e) [a/(b+i*c)]"""
    a, b, c, d, e = 213, 97, 45, 28, 11
    return sum(a / (b + i * c) for i in range(1, e + 1))

def analysis_6():
    """Analysis 6: F(d) + e!"""
    a, b, c, d, e = 213, 97, 45, 28, 11
    fib_d = fibonacci(d)
    fact_e = math.factorial(e)
    return fib_d + fact_e

def analysis_7():
    """Analysis 7: (a mod b) * (c mod d) + (d mod e)"""
    a, b, c, d, e = 213, 97, 45, 28, 11
    return (a % b) * (c % d) + (d % e)

def analysis_8():
    """Analysis 8: モンテカルロ法でπ推定"""
    random.seed(42)  # 再現性のため
    trials = 10000
    inside_circle = 0
    for _ in range(trials):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside_circle += 1
    return 4 * inside_circle / trials

def run_performance_analysis():
    """全分析のパフォーマンス測定を実行"""
    print("=== パフォーマンス分析開始 ===")
    
    analyses = [
        ("analysis_1", "((a+b)*c - d*e) / (a-b)", analysis_1),
        ("analysis_2", "a^3 - b^2 + c^2 - d^2 + e^3", analysis_2),
        ("analysis_3", "√(a^2 + b^2) * sin(c°)", analysis_3),
        ("analysis_4", "log(a*b) + ln(c*d) - log2(e)", analysis_4),
        ("analysis_5", "Σ(i=1 to e) [a/(b+i*c)]", analysis_5),
        ("analysis_6", "F(d) + e!", analysis_6),
        ("analysis_7", "(a mod b) * (c mod d) + (d mod e)", analysis_7),
        ("analysis_8", "Monte Carlo π estimation", analysis_8)
    ]
    
    performance_data = []
    total_time = 0
    total_memory = 0
    
    for name, formula, func in analyses:
        print(f"\n--- {name}: {formula} ---")
        
        # 実行時間測定（複数回実行して平均を取る）
        times = []
        for _ in range(5):
            result, exec_time = measure_execution_time(func)
            times.append(exec_time)
        
        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)
        
        # メモリ使用量推定
        try:
            result, memory_used = estimate_memory_usage(func)
        except:
            memory_used = 0  # メモリ測定できない場合
        
        performance_data.append({
            "analysis": name,
            "formula": formula,
            "result": result,
            "avg_execution_time_ms": round(avg_time, 3),
            "min_execution_time_ms": round(min_time, 3),
            "max_execution_time_ms": round(max_time, 3),
            "memory_usage_bytes": memory_used,
            "complexity_estimate": estimate_complexity(name, avg_time)
        })
        
        total_time += avg_time
        total_memory += memory_used
        
        print(f"  結果: {result}")
        print(f"  平均実行時間: {avg_time:.3f}ms")
        print(f"  実行時間範囲: {min_time:.3f}ms - {max_time:.3f}ms")
        print(f"  メモリ使用量: {memory_used:,} bytes")
    
    # 最も時間のかかった計算を特定
    slowest = max(performance_data, key=lambda x: x["avg_execution_time_ms"])
    fastest = min(performance_data, key=lambda x: x["avg_execution_time_ms"])
    
    # 統計情報
    statistics = {
        "total_analyses": len(analyses),
        "total_execution_time_ms": round(total_time, 3),
        "average_execution_time_ms": round(total_time / len(analyses), 3),
        "total_memory_usage_bytes": total_memory,
        "slowest_analysis": {
            "name": slowest["analysis"],
            "time_ms": slowest["avg_execution_time_ms"],
            "formula": slowest["formula"]
        },
        "fastest_analysis": {
            "name": fastest["analysis"],
            "time_ms": fastest["avg_execution_time_ms"],
            "formula": fastest["formula"]
        }
    }
    
    return performance_data, statistics

def estimate_complexity(analysis_name, execution_time):
    """計算複雑度を推定"""
    if execution_time < 1.0:
        return "Very Low"
    elif execution_time < 10.0:
        return "Low"
    elif execution_time < 50.0:
        return "Medium"
    elif execution_time < 200.0:
        return "High"
    else:
        return "Very High"

def generate_performance_report():
    """パフォーマンスレポートを生成"""
    print("パフォーマンス分析を実行中...")
    
    performance_data, statistics = run_performance_analysis()
    
    # システム情報の取得
    system_info = {
        "cpu_count": psutil.cpu_count(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_total": psutil.virtual_memory().total,
        "memory_available": psutil.virtual_memory().available,
        "python_version": f"{os.sys.version_info.major}.{os.sys.version_info.minor}.{os.sys.version_info.micro}"
    }
    
    # レポート作成
    report = {
        "metadata": {
            "script_name": "performance_analysis.py",
            "created_by": "テストAI4",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "analysis_count": len(performance_data)
        },
        "system_info": system_info,
        "performance_data": performance_data,
        "statistics": statistics,
        "recommendations": generate_recommendations(performance_data, statistics)
    }
    
    # JSONファイルに出力
    with open("performance_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # コンソール出力
    print("\n=== パフォーマンス分析結果 ===")
    print(f"総実行時間: {statistics['total_execution_time_ms']}ms")
    print(f"平均実行時間: {statistics['average_execution_time_ms']}ms")
    print(f"最も時間のかかった計算: {statistics['slowest_analysis']['name']} ({statistics['slowest_analysis']['time_ms']}ms)")
    print(f"最も高速な計算: {statistics['fastest_analysis']['name']} ({statistics['fastest_analysis']['time_ms']}ms)")
    print(f"総メモリ使用量: {statistics['total_memory_usage_bytes']:,} bytes")
    
    print(f"\nレポートをperformance_report.jsonに保存しました")
    
    return report

def generate_recommendations(performance_data, statistics):
    """パフォーマンス改善の推奨事項を生成"""
    recommendations = []
    
    # 実行時間の分析
    slowest = statistics["slowest_analysis"]
    if slowest["time_ms"] > 100:
        recommendations.append(f"{slowest['name']}の計算を最適化することを推奨します（現在{slowest['time_ms']}ms）")
    
    # メモリ使用量の分析
    high_memory_analyses = [p for p in performance_data if p["memory_usage_bytes"] > 1000000]  # 1MB以上
    if high_memory_analyses:
        recommendations.append("高メモリ使用量の計算でメモリ効率化を検討してください")
    
    # 複雑度の分析
    complex_analyses = [p for p in performance_data if p["complexity_estimate"] in ["High", "Very High"]]
    if complex_analyses:
        recommendations.append("高複雑度の計算でアルゴリズム最適化を検討してください")
    
    if not recommendations:
        recommendations.append("現在のパフォーマンスは良好です")
    
    return recommendations

if __name__ == "__main__":
    try:
        generate_performance_report()
    except ImportError as e:
        print(f"必要なライブラリがインストールされていません: {e}")
        print("pip install psutil を実行してください")
    except Exception as e:
        print(f"エラーが発生しました: {e}")