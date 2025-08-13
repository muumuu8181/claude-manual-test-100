#!/usr/bin/env python3
import math
import json
import time

def experiment_1_calculation():
    """
    計算: (x^3 + y^3) / (z^2 - w^2) + log2(v)
    パラメータ: x=312, y=189, z=147, w=78, v=33
    """
    start_time = time.time()
    
    # パラメータ設定
    x, y, z, w, v = 312, 189, 147, 78, 33
    
    # 計算実行
    x_cubed = x ** 3
    y_cubed = y ** 3
    z_squared = z ** 2
    w_squared = w ** 2
    
    # 分母が0でないことを確認
    denominator = z_squared - w_squared
    if denominator == 0:
        raise ValueError("Division by zero: z^2 - w^2 = 0")
    
    # メイン計算
    main_calculation = (x_cubed + y_cubed) / denominator
    log_term = math.log2(v)
    result = main_calculation + log_term
    
    # 小数点第5位まで
    result_rounded = round(result, 5)
    
    # 分類
    if result_rounded >= 1000:
        classification = "HIGH"
    elif 100 <= result_rounded < 1000:
        classification = "MEDIUM"
    else:
        classification = "LOW"
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # 結果をJSONで保存
    output_data = {
        "calculation_details": {
            "x_cubed": x_cubed,
            "y_cubed": y_cubed,
            "z_squared": z_squared,
            "w_squared": w_squared,
            "denominator": denominator,
            "main_calculation": main_calculation,
            "log_term": log_term
        },
        "result": result_rounded,
        "classification": classification,
        "execution_time_seconds": execution_time,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    
    with open('output_result.json', 'w') as f:
        json.dump(output_data, f, indent=2)
    
    # 検証結果
    validation_result = f"""実験1検証結果:
計算式: (x^3 + y^3) / (z^2 - w^2) + log2(v)
パラメータ: x={x}, y={y}, z={z}, w={w}, v={v}
計算結果: {result_rounded}
分類: {classification}
実行時間: {execution_time:.6f}秒
検証: 計算は正常に完了しました
"""
    
    with open('validation_check.txt', 'w', encoding='utf-8') as f:
        f.write(validation_result)
    
    return result_rounded, classification

if __name__ == "__main__":
    result, classification = experiment_1_calculation()
    print(f"実験1結果: {result} ({classification})")