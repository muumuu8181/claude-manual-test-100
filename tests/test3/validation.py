#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
計算結果とJSONファイルの妥当性検証スクリプト
作成者: テストAI3
"""

import json
import math
import os

def validate_calculations():
    """全計算結果の正確性を検証"""
    # 変数定義
    p, q, r, s = 175, 82, 39, 16
    
    # 期待値計算
    expected_results = {
        'calc_1': (p + q) * r - s,  # 10007
        'calc_2': p**2 + q**2 - r**2,  # 35828
        'calc_3': round((p * q) / (r + s), 3),  # 260.909
        'calc_4': round(math.sqrt(p**2 - q**2) + r, 2),  # 193.62
        'calc_5': round((r**3 + s**3) / (p - q), 3),  # 681.881
        'calc_6': round(math.log10(p * q) - math.log10(r * s), 4)  # 1.3617
    }
    
    errors = []
    
    # 各フォルダの結果を検証
    for calc_name, expected in expected_results.items():
        try:
            output_path = f"{calc_name}/output.txt"
            with open(output_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                result_str = content.split(': ')[1]
                actual = float(result_str)
                
                if abs(actual - expected) > 1e-10:
                    errors.append(f"{calc_name}: 期待値 {expected}, 実際値 {actual}")
        except Exception as e:
            errors.append(f"{calc_name}: ファイル読み取りエラー - {e}")
    
    return errors

def validate_json_format():
    """JSONファイルの形式妥当性をチェック"""
    errors = []
    
    try:
        with open('results_summary.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 必要なキーの存在確認
        required_keys = ['timestamp', 'calculations', 'statistics']
        for key in required_keys:
            if key not in data:
                errors.append(f"JSONに必要なキー '{key}' が見つかりません")
        
        # calculations内の確認
        if 'calculations' in data:
            calc_keys = [f'calc_{i}' for i in range(1, 7)]
            for calc_key in calc_keys:
                if calc_key not in data['calculations']:
                    errors.append(f"calculations内に '{calc_key}' が見つかりません")
                else:
                    calc_data = data['calculations'][calc_key]
                    if 'formula' not in calc_data or 'result' not in calc_data:
                        errors.append(f"{calc_key}にformula/resultが見つかりません")
        
        # statistics内の確認
        if 'statistics' in data:
            stat_keys = ['max', 'min', 'average']
            for stat_key in stat_keys:
                if stat_key not in data['statistics']:
                    errors.append(f"statistics内に '{stat_key}' が見つかりません")
    
    except Exception as e:
        errors.append(f"JSONファイル読み取りエラー: {e}")
    
    return errors

def validate_statistics():
    """統計値の正しさを確認"""
    errors = []
    
    try:
        with open('results_summary.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if 'calculations' in data and 'statistics' in data:
            # 全結果値を取得
            results = [data['calculations'][f'calc_{i}']['result'] for i in range(1, 7)]
            
            # 統計値計算
            expected_max = max(results)
            expected_min = min(results)
            expected_avg = round(sum(results) / len(results), 2)
            
            # 検証
            stats = data['statistics']
            if stats['max'] != expected_max:
                errors.append(f"max値が不正: 期待値 {expected_max}, 実際値 {stats['max']}")
            if stats['min'] != expected_min:
                errors.append(f"min値が不正: 期待値 {expected_min}, 実際値 {stats['min']}")
            if abs(stats['average'] - expected_avg) > 0.01:
                errors.append(f"average値が不正: 期待値 {expected_avg}, 実際値 {stats['average']}")
    
    except Exception as e:
        errors.append(f"統計値検証エラー: {e}")
    
    return errors

def main():
    """メイン検証処理"""
    print("=== 計算結果検証開始 ===")
    
    all_errors = []
    
    # 計算結果検証
    print("1. 計算結果の正確性検証...")
    calc_errors = validate_calculations()
    all_errors.extend(calc_errors)
    
    # JSON形式検証
    print("2. JSONファイル形式検証...")
    json_errors = validate_json_format()
    all_errors.extend(json_errors)
    
    # 統計値検証
    print("3. 統計値の正しさ確認...")
    stat_errors = validate_statistics()
    all_errors.extend(stat_errors)
    
    # 結果出力
    if all_errors:
        print("\n=== エラーが見つかりました ===")
        for error in all_errors:
            print(f"- {error}")
    else:
        print("\nAll validations passed!")

if __name__ == "__main__":
    main()