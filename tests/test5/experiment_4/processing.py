#!/usr/bin/env python3
import json
import time

def fibonacci_memoized(n, memo={}):
    """
    メモ化を使用したフィボナッチ数列の計算
    """
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

def experiment_4_calculation():
    """
    計算: F(30) / (x*y*z*w*v)
    パラメータ: x=312, y=189, z=147, w=78, v=33
    条件: メモ化を使用して効率化
    """
    start_time = time.time()
    
    # パラメータ設定
    x, y, z, w, v = 312, 189, 147, 78, 33
    n = 30
    
    # フィボナッチ数列F(30)の計算（メモ化使用）
    fibonacci_30 = fibonacci_memoized(n)
    
    # 分母の計算
    denominator = x * y * z * w * v
    
    # メイン計算
    result = fibonacci_30 / denominator
    
    # 小数点第8位まで
    result_rounded = round(result, 8)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # 結果をJSONで保存
    output_data = {
        "calculation_details": {
            "fibonacci_n": n,
            "fibonacci_result": fibonacci_30,
            "denominator_components": {
                "x": x,
                "y": y,
                "z": z,
                "w": w,
                "v": v
            },
            "denominator_product": denominator
        },
        "result": result_rounded,
        "execution_time_seconds": execution_time,
        "optimization": "Memoization used",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    
    with open('output_result.json', 'w') as f:
        json.dump(output_data, f, indent=2)
    
    # 検証結果
    validation_result = f"""実験4検証結果:
計算式: F(30) / (x*y*z*w*v)
パラメータ: x={x}, y={y}, z={z}, w={w}, v={v}
フィボナッチF(30): {fibonacci_30}
分母: {denominator}
計算結果: {result_rounded}
実行時間: {execution_time:.6f}秒
最適化: メモ化使用
検証: フィボナッチ計算は正常に完了しました
"""
    
    with open('validation_check.txt', 'w', encoding='utf-8') as f:
        f.write(validation_result)
    
    return result_rounded

if __name__ == "__main__":
    result = experiment_4_calculation()
    print(f"実験4結果: {result}")