#!/usr/bin/env python3
import json
import time

def experiment_2_calculation():
    """
    計算: Σ(i=1 to 10) [(x*i + y)/(z-w*i)]
    パラメータ: x=312, y=189, z=147, w=78, v=33
    条件: 各項が負になる場合は0として扱う
    """
    start_time = time.time()
    
    # パラメータ設定
    x, y, z, w, v = 312, 189, 147, 78, 33
    
    total_sum = 0
    calculation_details = []
    
    # 総和計算
    for i in range(1, 11):
        numerator = x * i + y
        denominator = z - w * i
        
        # 分母が0でないことを確認
        if denominator == 0:
            term_value = 0
            note = "Division by zero, treated as 0"
        else:
            term_value = numerator / denominator
            # 負の場合は0として扱う
            if term_value < 0:
                original_value = term_value
                term_value = 0
                note = f"Negative value {original_value:.6f} treated as 0"
            else:
                note = "Normal calculation"
        
        total_sum += term_value
        
        calculation_details.append({
            "i": i,
            "numerator": numerator,
            "denominator": denominator,
            "term_value": term_value,
            "note": note
        })
    
    # 小数点第4位まで
    result_rounded = round(total_sum, 4)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # 結果をJSONで保存
    output_data = {
        "calculation_details": calculation_details,
        "total_sum": result_rounded,
        "execution_time_seconds": execution_time,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    
    with open('output_result.json', 'w') as f:
        json.dump(output_data, f, indent=2)
    
    # 検証結果
    validation_result = f"""実験2検証結果:
計算式: Σ(i=1 to 10) [(x*i + y)/(z-w*i)]
パラメータ: x={x}, y={y}, z={z}, w={w}, v={v}
計算結果: {result_rounded}
実行時間: {execution_time:.6f}秒
検証: 総和計算は正常に完了しました
条件: 負の項は0として処理済み
"""
    
    with open('validation_check.txt', 'w', encoding='utf-8') as f:
        f.write(validation_result)
    
    return result_rounded

if __name__ == "__main__":
    result = experiment_2_calculation()
    print(f"実験2結果: {result}")