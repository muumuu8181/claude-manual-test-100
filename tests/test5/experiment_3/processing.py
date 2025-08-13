#!/usr/bin/env python3
import math
import json
import time

def experiment_3_calculation():
    """
    計算: exp(x/100) * sin(y*π/180) * cos(z*π/180) / tan(w*π/180)
    パラメータ: x=312, y=189, z=147, w=78, v=33
    条件: tan(w*π/180)が0に近い場合（±0.001以内）はエラー処理
    """
    start_time = time.time()
    
    # パラメータ設定
    x, y, z, w, v = 312, 189, 147, 78, 33
    
    # 角度をラジアンに変換
    y_radians = y * math.pi / 180
    z_radians = z * math.pi / 180
    w_radians = w * math.pi / 180
    
    # 各計算要素
    exp_term = math.exp(x / 100)
    sin_term = math.sin(y_radians)
    cos_term = math.cos(z_radians)
    tan_term = math.tan(w_radians)
    
    # tan(w*π/180)が0に近いかチェック
    if abs(tan_term) <= 0.001:
        error_msg = f"Error: tan({w}*π/180) = {tan_term:.6f} is within ±0.001 of zero"
        result_rounded = None
        status = "ERROR"
    else:
        # メイン計算
        result = exp_term * sin_term * cos_term / tan_term
        result_rounded = round(result, 6)
        error_msg = None
        status = "SUCCESS"
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # 結果をJSONで保存
    output_data = {
        "calculation_details": {
            "exp_x_over_100": exp_term,
            "sin_y_radians": sin_term,
            "cos_z_radians": cos_term,
            "tan_w_radians": tan_term,
            "y_degrees": y,
            "z_degrees": z,
            "w_degrees": w,
            "y_radians": y_radians,
            "z_radians": z_radians,
            "w_radians": w_radians
        },
        "result": result_rounded,
        "status": status,
        "error_message": error_msg,
        "execution_time_seconds": execution_time,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    
    with open('output_result.json', 'w') as f:
        json.dump(output_data, f, indent=2)
    
    # 検証結果
    if status == "ERROR":
        validation_result = f"""実験3検証結果:
計算式: exp(x/100) * sin(y*π/180) * cos(z*π/180) / tan(w*π/180)
パラメータ: x={x}, y={y}, z={z}, w={w}, v={v}
ステータス: {status}
エラーメッセージ: {error_msg}
実行時間: {execution_time:.6f}秒
検証: エラー条件により計算を中止
"""
    else:
        validation_result = f"""実験3検証結果:
計算式: exp(x/100) * sin(y*π/180) * cos(z*π/180) / tan(w*π/180)
パラメータ: x={x}, y={y}, z={z}, w={w}, v={v}
計算結果: {result_rounded}
ステータス: {status}
実行時間: {execution_time:.6f}秒
検証: 三角関数計算は正常に完了しました
"""
    
    with open('validation_check.txt', 'w', encoding='utf-8') as f:
        f.write(validation_result)
    
    return result_rounded, status

if __name__ == "__main__":
    result, status = experiment_3_calculation()
    if status == "SUCCESS":
        print(f"実験3結果: {result}")
    else:
        print(f"実験3エラー: {status}")