# Test7 期待結果

## 最終的なディレクトリ構造

```
calculator_project/
├── execution_summary.txt
├── src/
│   ├── basic_math.py
│   ├── file_processor.py
│   └── calculator_main.py
├── data/
│   ├── input_A.txt
│   └── input_B.txt
└── results/
    ├── sum_a.txt
    ├── sum_b.txt
    ├── total_sum.txt
    ├── average_a.txt
    ├── average_b.txt
    └── product_averages.txt
```

## 各ファイルの期待内容

### src/basic_math.py
```python
def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

### src/file_processor.py
```python
def read_numbers_from_file(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

def write_result_to_file(filename, result):
    with open(filename, 'w') as f:
        f.write(str(result))
```

### src/calculator_main.py
```python
from basic_math import add_numbers, multiply_numbers, calculate_average
from file_processor import read_numbers_from_file, write_result_to_file

# データファイルを読み込み
numbers_a = read_numbers_from_file('../data/input_A.txt')
numbers_b = read_numbers_from_file('../data/input_B.txt')

# 計算実行
sum_a = sum(numbers_a)
sum_b = sum(numbers_b)
total_sum = add_numbers(sum_a, sum_b)
average_a = calculate_average(numbers_a)
average_b = calculate_average(numbers_b)
product_of_averages = multiply_numbers(average_a, average_b)

# 結果をファイルに保存
write_result_to_file('../results/sum_a.txt', sum_a)
write_result_to_file('../results/sum_b.txt', sum_b)
write_result_to_file('../results/total_sum.txt', total_sum)
write_result_to_file('../results/average_a.txt', average_a)
write_result_to_file('../results/average_b.txt', average_b)
write_result_to_file('../results/product_averages.txt', product_of_averages)

print("計算完了: 結果はresultsフォルダに保存されました")
```

### data/input_A.txt
```
15
25
35
45
55
```

### data/input_B.txt
```
10
20
30
40
50
```

### results/sum_a.txt
```
175
```

### results/sum_b.txt
```
150
```

### results/total_sum.txt
```
325
```

### results/average_a.txt
```
35.0
```

### results/average_b.txt
```
30.0
```

### results/product_averages.txt
```
1050.0
```

### execution_summary.txt
```
Calculation Summary
Input A Sum: 175
Input B Sum: 150
Total Sum: 325
Execution Status: Success
```

## 計算の検証
- Input A合計: 15+25+35+45+55 = 175
- Input B合計: 10+20+30+40+50 = 150
- 総合計: 175+150 = 325
- Input A平均: 175/5 = 35.0
- Input B平均: 150/5 = 30.0
- 平均の積: 35.0×30.0 = 1050.0