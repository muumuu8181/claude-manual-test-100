#!/usr/bin/env python3
import random
import math
import json
import time

def estimate_pi_monte_carlo(iterations=10000):
    """
    モンテカルロ法でπを推定
    """
    inside_circle = 0
    
    for _ in range(iterations):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # 単位円内にあるかチェック
        if x*x + y*y <= 1:
            inside_circle += 1
    
    # π ≈ 4 * (円内の点の数 / 全体の点の数)
    pi_estimated = 4 * inside_circle / iterations
    return pi_estimated

def experiment_5_calculation():
    """
    計算: モンテカルロ法でπを推定し、(x+y+z)*π推定値を計算
    パラメータ: x=312, y=189, z=147, w=78, v=33
    条件: πの推定誤差も記録
    """
    start_time = time.time()
    
    # パラメータ設定
    x, y, z, w, v = 312, 189, 147, 78, 33
    iterations = 10000
    
    # モンテカルロ法でπを推定
    pi_estimated = estimate_pi_monte_carlo(iterations)
    
    # 実際のπとの誤差
    actual_pi = math.pi
    pi_error = abs(pi_estimated - actual_pi)
    pi_error_percentage = (pi_error / actual_pi) * 100
    
    # メイン計算: (x+y+z)*π推定値
    sum_xyz = x + y + z
    result = sum_xyz * pi_estimated
    
    # 小数点第5位まで
    result_rounded = round(result, 5)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # 結果をJSONで保存
    output_data = {
        "calculation_details": {
            "monte_carlo_iterations": iterations,
            "pi_estimated": pi_estimated,
            "pi_actual": actual_pi,
            "pi_error": pi_error,
            "pi_error_percentage": pi_error_percentage,
            "sum_xyz": sum_xyz
        },
        "result": result_rounded,
        "execution_time_seconds": execution_time,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    
    with open('output_result.json', 'w') as f:
        json.dump(output_data, f, indent=2)
    
    # 検証結果
    validation_result = f"""実験5検証結果:
計算式: (x+y+z) * π推定値
パラメータ: x={x}, y={y}, z={z}, w={w}, v={v}
モンテカルロ試行回数: {iterations}
π推定値: {pi_estimated:.6f}
π実際値: {actual_pi:.6f}
π推定誤差: {pi_error:.6f} ({pi_error_percentage:.3f}%)
x+y+z: {sum_xyz}
計算結果: {result_rounded}
実行時間: {execution_time:.6f}秒
検証: モンテカルロ法による計算は正常に完了しました
"""
    
    with open('validation_check.txt', 'w', encoding='utf-8') as f:
        f.write(validation_result)
    
    return result_rounded, pi_estimated, pi_error

if __name__ == "__main__":
    result, pi_est, pi_err = experiment_5_calculation()
    print(f"実験5結果: {result} (π推定: {pi_est:.6f}, 誤差: {pi_err:.6f})")