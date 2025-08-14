# Test9 期待結果

## 最終的なディレクトリ構造

```
customer_database/
├── system_documentation.txt
├── data/
│   ├── customers.csv
│   ├── customers_corrected.csv
│   └── test_recovery.txt
├── backup/
│   └── [タイムスタンプ]_customers.csv
│   └── [タイムスタンプ]_test_recovery.txt
├── logs/
│   ├── validation_errors.txt
│   ├── validation_summary.txt
│   ├── recovery_test_log.txt
│   ├── system_status.txt
│   └── backup_inventory.txt
├── scripts/
│   ├── data_validator.py
│   ├── backup_manager.py
│   └── recovery_test.py
└── validation/
    ├── valid_customers.csv
    ├── invalid_customers.csv
    ├── data_quality_report.txt
    └── statistics.txt
```

## 各ファイルの期待内容

### data/customers.csv (元データ)
```
ID,Name,Email,Age,City
001,Tanaka Taro,tanaka@email.com,25,Tokyo
002,Suzuki Hanako,invalid-email,30,Osaka
003,Sato Ichiro,sato@email.com,-5,Kyoto
004,,yamada@email.com,35,Nagoya
005,Kimura Jiro,kimura@email.com,40,Fukuoka
```

### data/customers_corrected.csv
```
ID,Name,Email,Age,City
001,Tanaka Taro,tanaka@email.com,25,Tokyo
002,Suzuki Hanako,suzuki@email.com,30,Osaka
003,Sato Ichiro,sato@email.com,30,Kyoto
004,Yamada Saburo,yamada@email.com,35,Nagoya
005,Kimura Jiro,kimura@email.com,40,Fukuoka
```

### validation/valid_customers.csv
```
ID,Name,Email,Age,City
001,Tanaka Taro,tanaka@email.com,25,Tokyo
005,Kimura Jiro,kimura@email.com,40,Fukuoka
```

### validation/invalid_customers.csv
```
ID,Name,Email,Age,City
002,Suzuki Hanako,invalid-email,30,Osaka
003,Sato Ichiro,sato@email.com,-5,Kyoto
004,,yamada@email.com,35,Nagoya
```

### logs/validation_errors.txt
```
Invalid email in row 3
Invalid age in row 4
Invalid name in row 5
```

### logs/validation_summary.txt
```
Validation Summary
Total Records: 5
Valid Records: 2
Invalid Records: 3
Validation Date: [実行時の日時]
```

### validation/data_quality_report.txt
```
Data Quality Report

Total Records Processed: 5
Valid Records: 2
Invalid Records: 3

Validation Issues:
- Email format errors: 1
- Invalid age values: 1  
- Missing name fields: 1

Valid Records Rate: 40%
Data Quality Score: Poor
```

### logs/recovery_test_log.txt
```
Recovery test completed
```

### logs/system_status.txt
```
System Status Report
Data Validation: Complete
Backup Creation: Complete
Recovery Test: Complete
Overall Status: Success
```

### validation/statistics.txt
```
Valid Customer Statistics
Total Valid Customers: 2
Average Age: 32.5
Age Range: 25-40
```

### logs/backup_inventory.txt
```
Backup Files Created:
- [タイムスタンプ]_customers.csv
- [タイムスタンプ]_test_recovery.txt

Total Backup Files: 2
```

### system_documentation.txt
```
Customer Database Management System

System Components:
- Data validation with error handling
- Automatic backup creation
- Recovery testing functionality
- Comprehensive logging

Processing Results:
- Original records: 5
- Valid records after validation: 2
- Invalid records requiring correction: 3
- Backup files created: 2
- All systems functioning correctly

Error Handling:
- Invalid email formats detected and logged
- Invalid age values caught and reported
- Missing name fields identified
- All errors properly handled without system failure
```