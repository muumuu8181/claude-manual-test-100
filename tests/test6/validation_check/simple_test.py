# シンプルな動作確認
import math
import json

# test6の基本パラメータ
alpha = 427
beta = 256
gamma = 198
delta = 87
epsilon = 64
zeta = 31

# 簡単な計算
result1 = math.sqrt(alpha * beta)
result2 = math.log(gamma) + math.exp(delta/100)
result3 = math.sin(epsilon * math.pi / 180)

print(f"計算1: sqrt({alpha} * {beta}) = {result1:.5f}")
print(f"計算2: log({gamma}) + exp({delta}/100) = {result2:.5f}")
print(f"計算3: sin({epsilon} * π/180) = {result3:.5f}")

# JSONファイル作成
output = {
    "test": "simple_validation",
    "results": {
        "calc1": result1,
        "calc2": result2,
        "calc3": result3
    },
    "status": "success"
}

with open("test_output.json", "w") as f:
    json.dump(output, f, indent=2)
    
print("\ntest_output.json created successfully!")
