# Test6 期待結果

## 最終的なディレクトリ構造

```
grade_management/
├── analysis_report.txt
├── raw_data/
│   ├── students_math.csv
│   ├── students_english.csv
│   ├── students_science.csv
│   ├── math_top_student.txt
│   ├── english_lowest_student.txt
│   ├── subject_averages.txt
│   └── data_inventory.txt
└── processed_data/
    ├── student_totals.csv
    ├── overall_top_student.txt
    ├── high_performers.txt
    ├── need_improvement.txt
    └── grade_summary.json
```

## 各ファイルの期待内容

### raw_data/students_math.csv
```
Name,Score
Alice,85
Bob,92
Charlie,78
Diana,96
Eve,89
```

### raw_data/students_english.csv
```
Name,Score
Alice,88
Bob,76
Charlie,94
Diana,82
Eve,91
```

### raw_data/students_science.csv
```
Name,Score
Alice,90
Bob,84
Charlie,87
Diana,93
Eve,86
```

### raw_data/math_top_student.txt
```
Top Math Student: Diana
```

### raw_data/english_lowest_student.txt
```
Lowest English Student: Bob
```

### raw_data/subject_averages.txt
```
Math Average: 88.0
English Average: 86.2
Science Average: 88.0
```

### raw_data/data_inventory.txt
```
students_math.csv: 5 records
students_english.csv: 5 records
students_science.csv: 5 records
```

### processed_data/student_totals.csv
```
Name,Total
Alice,263
Bob,252
Charlie,259
Diana,271
Eve,266
```

### processed_data/overall_top_student.txt
```
Overall Top Student: Diana - Total: 271
```

### processed_data/high_performers.txt
```
Alice
Bob
Charlie
Diana
Eve
```

### processed_data/need_improvement.txt
```
（空ファイル - 該当学生なし）
```

### processed_data/grade_summary.json
```json
{"total_students": 5, "subjects": ["Math", "English", "Science"], "highest_total": 271, "lowest_total": 252}
```

### analysis_report.txt
```
Grade Analysis Report
Total Students: 5
Subjects Analyzed: 3
Highest Individual Score: 96 (Math)
Lowest Individual Score: 76 (English)
```