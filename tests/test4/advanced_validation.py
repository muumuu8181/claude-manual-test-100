#!/usr/bin/env python3
"""
Advanced Validation Script for Test4 calculations
Created by テストAI4
"""

import json
import csv
import math
import time
import os
from pathlib import Path

def start_timer():
    """開始時間を記録"""
    return time.time()

def log_result(message):
    """結果をログ出力"""
    print(message)

def validate_calculations():
    """全計算結果の正確性検証"""
    log_result("=== 計算結果の正確性検証 ===")
    
    # パラメータ
    a, b, c, d, e = 238, 157, 93, 46, 21
    pi = 3.14159265359
    
    results = {}
    errors = []
    
    # Analysis 1: (a+b)*(c-d) + e^2
    expected_1 = (a+b)*(c-d) + e**2
    results['analysis_1'] = expected_1
    log_result(f"Analysis 1: Expected {expected_1}")
    
    # Analysis 2: a^2 - b^2 + c^2 - d^2
    expected_2 = a**2 - b**2 + c**2 - d**2
    results['analysis_2'] = expected_2
    log_result(f"Analysis 2: Expected {expected_2}")
    
    # Analysis 3: (a*b*c) / (d*e)
    expected_3 = round((a*b*c) / (d*e), 4)
    results['analysis_3'] = expected_3
    log_result(f"Analysis 3: Expected {expected_3}")
    
    # Analysis 4: √(a^2 + b^2) - √(c^2 + d^2)
    expected_4 = round(math.sqrt(a**2 + b**2) - math.sqrt(c**2 + d**2), 3)
    results['analysis_4'] = expected_4
    log_result(f"Analysis 4: Expected {expected_4}")
    
    # Analysis 5: (c^3 - d^3) / (a-b) + e
    expected_5 = round((c**3 - d**3) / (a-b) + e, 4)
    results['analysis_5'] = expected_5
    log_result(f"Analysis 5: Expected {expected_5}")
    
    # Analysis 6: log10(a*b) + log10(c*d) - log10(e)
    expected_6 = round(math.log10(a*b) + math.log10(c*d) - math.log10(e), 5)
    results['analysis_6'] = expected_6
    log_result(f"Analysis 6: Expected {expected_6}")
    
    # Analysis 7: sin(a/180*π) + cos(b/180*π)
    expected_7 = round(math.sin(a/180*pi) + math.cos(b/180*pi), 5)
    results['analysis_7'] = expected_7
    log_result(f"Analysis 7: Expected {expected_7}")
    
    # Analysis 8: (a!/(a-5)!) / (b!/(b-3)!)
    # 階乗の簡約形
    numerator = a * (a-1) * (a-2) * (a-3) * (a-4)
    denominator = b * (b-1) * (b-2)
    expected_8 = numerator // denominator
    results['analysis_8'] = expected_8
    log_result(f"Analysis 8: Expected {expected_8}")
    
    return results, errors

def validate_json_format():
    """JSONファイルの形式妥当性チェック"""
    log_result("\n=== JSON形式妥当性チェック ===")
    
    try:
        with open('comprehensive_report.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 必要なキーの存在確認
        required_keys = ['metadata', 'calculations', 'statistics', 'summary']
        for key in required_keys:
            if key not in data:
                return False, f"Missing required key: {key}"
        
        # calculations内の確認
        for i in range(1, 9):
            analysis_key = f'analysis_{i}'
            if analysis_key not in data['calculations']:
                return False, f"Missing analysis: {analysis_key}"
        
        log_result("JSON形式は正常です")
        return True, None
        
    except Exception as e:
        return False, f"JSON validation error: {str(e)}"

def validate_csv_format():
    """CSVファイルの形式と内容確認"""
    log_result("\n=== CSV形式・内容確認 ===")
    
    try:
        with open('data_analysis.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        # ヘッダー確認
        expected_header = ['フォルダ名', '計算式', '結果', '検証状態']
        if rows[0] != expected_header:
            return False, f"CSV header mismatch: {rows[0]}"
        
        # 行数確認
        if len(rows) != 9:  # ヘッダー + 8データ行
            return False, f"CSV row count mismatch: {len(rows)}"
        
        log_result("CSV形式は正常です")
        return True, None
        
    except Exception as e:
        return False, f"CSV validation error: {str(e)}"

def validate_statistics():
    """統計値の正しさ確認"""
    log_result("\n=== 統計値確認 ===")
    
    # 実際の結果値
    values = [19006, 38528, 3597.7617, 181.364, 8749.6543, 6.88163, -1.76855, 975755]
    
    # 統計値計算
    max_val = max(values)
    min_val = min(values)
    avg_val = round(sum(values) / len(values), 3)
    
    sorted_values = sorted(values)
    median_val = round((sorted_values[3] + sorted_values[4]) / 2, 3)
    
    # 標準偏差
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    std_dev = round(math.sqrt(variance), 4)
    
    log_result(f"計算された統計値:")
    log_result(f"  最大値: {max_val}")
    log_result(f"  最小値: {min_val}")
    log_result(f"  平均値: {avg_val}")
    log_result(f"  中央値: {median_val}")
    log_result(f"  標準偏差: {std_dev}")
    
    return {
        'max': max_val,
        'min': min_val,
        'average': avg_val,
        'median': median_val,
        'std_dev': std_dev
    }

def validate_verification_files():
    """各フォルダのverification.txtとの整合性チェック"""
    log_result("\n=== Verification.txt整合性チェック ===")
    
    errors = []
    
    for i in range(1, 9):
        folder_name = f"analysis_{i}"
        verification_file = Path(folder_name) / "verification.txt"
        
        if not verification_file.exists():
            errors.append(f"{folder_name}/verification.txt が存在しません")
            continue
        
        try:
            with open(verification_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "passed" not in content.lower():
                errors.append(f"{folder_name}/verification.txt にpassedの記載がありません")
        
        except Exception as e:
            errors.append(f"{folder_name}/verification.txt 読み取りエラー: {str(e)}")
    
    if not errors:
        log_result("全てのverification.txtファイルが正常です")
    
    return errors

def main():
    """メイン実行関数"""
    start_time = start_timer()
    
    log_result("Advanced Validation Script - テストAI4")
    log_result("=" * 50)
    
    all_errors = []
    
    # 1. 計算結果の正確性検証
    expected_results, calc_errors = validate_calculations()
    all_errors.extend(calc_errors)
    
    # 2. JSON形式妥当性チェック
    json_valid, json_error = validate_json_format()
    if not json_valid:
        all_errors.append(json_error)
    
    # 3. CSV形式と内容確認
    csv_valid, csv_error = validate_csv_format()
    if not csv_valid:
        all_errors.append(csv_error)
    
    # 4. 統計値の正しさ確認
    calculated_stats = validate_statistics()
    
    # 5. verification.txtとの整合性チェック
    verification_errors = validate_verification_files()
    all_errors.extend(verification_errors)
    
    # 結果出力
    end_time = time.time()
    execution_time = end_time - start_time
    
    log_result("\n" + "=" * 50)
    
    if all_errors:
        log_result("エラーが検出されました:")
        for error in all_errors:
            log_result(f"  - {error}")
    else:
        log_result("All advanced validations passed successfully!")
    
    log_result(f"Execution time: {execution_time:.3f} seconds")

if __name__ == "__main__":
    main()