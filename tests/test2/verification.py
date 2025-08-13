#!/usr/bin/env python3
"""
計算結果検証スクリプト
a=142, b=89, c=23 の計算結果を検証します
"""

import math
import os

def verify_calculations():
    """全ての計算結果を検証"""
    a = 142
    b = 89
    c = 23
    
    # 期待される計算結果
    expected_results = {
        'data_1': {
            'formula': '(a+b)*c',
            'expected': (a + b) * c,
            'file': 'data_1/result_1.txt'
        },
        'data_2': {
            'formula': 'a^2 - b^2',
            'expected': a**2 - b**2,
            'file': 'data_2/result_2.txt'
        },
        'data_3': {
            'formula': '(a*b)/c',
            'expected': round((a * b) / c, 2),
            'file': 'data_3/result_3.txt'
        },
        'data_4': {
            'formula': 'c^3 + b^2 - a',
            'expected': c**3 + b**2 - a,
            'file': 'data_4/result_4.txt'
        },
        'data_5': {
            'formula': '√(a^2 + b^2)',
            'expected': round(math.sqrt(a**2 + b**2), 2),
            'file': 'data_5/result_5.txt'
        }
    }
    
    print(f"検証開始: a={a}, b={b}, c={c}")
    print("-" * 50)
    
    all_correct = True
    
    for folder, data in expected_results.items():
        file_path = data['file']
        
        if not os.path.exists(file_path):
            print(f"❌ {folder}: ファイル {file_path} が存在しません")
            all_correct = False
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            actual_result = f.read().strip()
            
        try:
            # 浮動小数点数として読み込み
            actual_value = float(actual_result)
            expected_value = float(data['expected'])
            
            # 浮動小数点数の比較（誤差を考慮）
            if abs(actual_value - expected_value) < 0.01:
                print(f"✅ {folder}: {data['formula']} = {actual_result} (正解)")
            else:
                print(f"❌ {folder}: {data['formula']}")
                print(f"   期待値: {expected_value}")
                print(f"   実際値: {actual_value}")
                all_correct = False
                
        except ValueError as e:
            print(f"❌ {folder}: 結果の解析エラー - {e}")
            all_correct = False
    
    print("-" * 50)
    
    if all_correct:
        print("✅ 全ての計算結果が正しいことを確認しました！")
    else:
        print("❌ 一部の計算結果に誤りがあります")
    
    return all_correct

if __name__ == "__main__":
    result = verify_calculations()
    exit(0 if result else 1)