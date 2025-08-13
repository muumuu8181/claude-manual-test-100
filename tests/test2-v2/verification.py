import math
import os

# 定数の定義
a = 142
b = 89
c = 23

# 期待される計算結果
expected_results = {
    'data_1': (a+b)*c,
    'data_2': a**2 - b**2,
    'data_3': round((a*b) / c, 2),
    'data_4': c**3 + b**2 - a,
    'data_5': round(math.sqrt(a**2 + b**2), 2)
}

# 各フォルダの結果ファイルを検証
verification_results = []
all_correct = True

for folder, expected_value in expected_results.items():
    result_file = os.path.join(folder, f'result_{folder[-1]}.txt')
    
    if os.path.exists(result_file):
        with open(result_file, 'r') as f:
            actual_value = f.read().strip()
            
        try:
            actual_value = float(actual_value)
            is_correct = actual_value == expected_value
            verification_results.append(f"{folder}: {'✓' if is_correct else '✗'} (期待値: {expected_value}, 実際: {actual_value})")
            if not is_correct:
                all_correct = False
        except ValueError:
            verification_results.append(f"{folder}: ✗ (数値の変換エラー)")
            all_correct = False
    else:
        verification_results.append(f"{folder}: ✗ (ファイルが存在しません)")
        all_correct = False

# 結果の表示
print("=" * 50)
print("計算結果の検証")
print("=" * 50)
for result in verification_results:
    print(result)
print("=" * 50)

if all_correct:
    print("✅ すべての計算結果が正しいです！")
else:
    print("❌ 一部の計算結果に誤りがあります")

# CSVファイルの存在確認
if os.path.exists('calculation_summary.csv'):
    print("\n✓ calculation_summary.csv が存在します")
else:
    print("\n✗ calculation_summary.csv が存在しません")