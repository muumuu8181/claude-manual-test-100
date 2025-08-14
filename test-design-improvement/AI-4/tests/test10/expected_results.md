# Test 10: Expected Results

## Step-by-Step Expected Outcomes

**Step 1:** Directory "data_workspace" created successfully
- Expected: New empty directory at ./data_workspace/

**Step 2:** CSV file created with employee data
- Expected: File at ./data_workspace/employees.csv containing:
```
id,name,department,salary
1,John Smith,Engineering,75000
2,Jane Doe,Marketing,65000
3,Bob Johnson,Sales,55000
```

**Step 3:** JSON file created with department data
- Expected: File at ./data_workspace/departments.json containing:
```json
{"Engineering": {"budget": 500000, "head": "Alice"}, "Marketing": {"budget": 300000, "head": "Charlie"}, "Sales": {"budget": 250000, "head": "Diana"}}
```

**Step 4:** Directory "processed" created
- Expected: New empty directory at ./data_workspace/processed/

**Step 5:** Directory "backup" created
- Expected: New empty directory at ./data_workspace/backup/

**Step 6:** File copied to backup
- Expected: File at ./data_workspace/backup/employees.csv with same content as original

**Step 7:** Employee count calculated and saved
- Expected: File at ./data_workspace/processed/employee_count.txt containing "3"

**Step 8:** High salary employees filtered
- Expected: File at ./data_workspace/processed/high_salary.csv containing:
```
id,name,salary
1,John Smith,75000
2,Jane Doe,65000
```

**Step 9:** Directory "json_output" created
- Expected: New empty directory at ./data_workspace/processed/json_output/

**Step 10:** Department names listed
- Expected: File at ./data_workspace/processed/json_output/department_list.txt containing:
```
Engineering
Marketing
Sales
```

**Step 11:** Total budget calculated
- Expected: File at ./data_workspace/processed/json_output/total_budget.txt containing "1050000"

**Step 12:** Department heads CSV created
- Expected: File at ./data_workspace/processed/json_output/department_heads.csv containing:
```
department,head
Engineering,Alice
Marketing,Charlie
Sales,Diana
```

**Step 13:** Directory "reports" created
- Expected: New empty directory at ./data_workspace/reports/

**Step 14:** High earners list created
- Expected: File at ./data_workspace/reports/high_earners.txt containing:
```
John Smith
Jane Doe
```

**Step 15:** Engineering data JSON created
- Expected: File at ./data_workspace/reports/engineering_data.json containing:
```json
{"department": "Engineering", "employees": 1, "avg_salary": 75000}
```

**Step 16:** Directory "temp" created
- Expected: New empty directory at ./data_workspace/temp/

**Step 17:** File moved from processed to temp
- Expected: File at ./data_workspace/temp/employee_count.txt containing "3"
- Original file at ./data_workspace/processed/employee_count.txt no longer exists

**Step 18:** Summary CSV created
- Expected: File at ./data_workspace/temp/summary.csv containing:
```
metric,value
total_employees,3
high_earners,2
departments,3
```

**Step 19:** Summary converted to JSON
- Expected: File at ./data_workspace/temp/metrics.json containing:
```json
{"total_employees": 3, "high_earners": 2, "departments": 3}
```

**Step 20:** Directory "final" created
- Expected: New empty directory at ./data_workspace/final/

**Step 21:** Department file copied and renamed
- Expected: File at ./data_workspace/final/original_departments.json with same content as departments.json

**Step 22:** Budget report created
- Expected: File at ./data_workspace/final/budget_report.txt containing:
```
Engineering: 500000
Marketing: 300000
Sales: 250000
```

**Step 23:** Employee summary JSON created
- Expected: File at ./data_workspace/final/employee_summary.json containing:
```json
{"total": 3, "by_department": {"Engineering": 1, "Marketing": 1, "Sales": 1}}
```

**Step 24:** High salary file moved
- Expected: File at ./data_workspace/final/high_salary.csv (moved from processed)
- Original file at ./data_workspace/processed/high_salary.csv no longer exists

**Step 25:** File renamed in final
- Expected: File at ./data_workspace/final/top_performers.csv
- File ./data_workspace/final/high_salary.csv no longer exists

**Step 26:** Directory "archive" created
- Expected: New empty directory at ./data_workspace/final/archive/

**Step 27:** Summary file moved to archive
- Expected: File at ./data_workspace/final/archive/summary.csv
- Original file at ./data_workspace/temp/summary.csv no longer exists

**Step 28:** Processing log created
- Expected: File at ./data_workspace/final/processing_log.txt containing:
```
Data processing completed successfully
Files processed: employees.csv, departments.json
Output files: 15
```

**Step 29:** Completion status JSON created
- Expected: File at ./data_workspace/final/completion_status.json containing:
```json
{"status": "completed", "files_processed": 2, "outputs_created": 15}
```

**Step 30:** Final report created
- Expected: File at ./data_workspace/final_report.txt containing "All data processing operations completed successfully"

## Final Directory Structure Verification

```
data_workspace/
├── final_report.txt
├── employees.csv (original)
├── departments.json (original)
├── backup/
│   └── employees.csv
├── processed/
│   └── json_output/
│       ├── department_list.txt
│       ├── total_budget.txt
│       └── department_heads.csv
├── reports/
│   ├── high_earners.txt
│   └── engineering_data.json
├── temp/
│   ├── employee_count.txt
│   └── metrics.json
└── final/
    ├── original_departments.json
    ├── budget_report.txt
    ├── employee_summary.json
    ├── top_performers.csv
    ├── processing_log.txt
    ├── completion_status.json
    └── archive/
        └── summary.csv
```

## Key Validation Points

1. All data transformations should be accurate (CSV to JSON, calculations, filtering)
2. File movements should be complete (source files removed)
3. File copies should preserve originals
4. Content calculations should be correct (counts, sums, filtering)
5. Format conversions should maintain data integrity
6. Total of 17 files across all directories