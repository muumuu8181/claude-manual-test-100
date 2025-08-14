# Test 10: Scoring Guide

**Total Points: 30 (1 point per step)**

## Scoring Criteria

### Step 1: Create data_workspace directory (1 point)
- **Full Credit (1 pt):** Directory "data_workspace" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect name

### Step 2: Create employees.csv file (1 point)
- **Full Credit (1 pt):** File exists with exact CSV content including header and 3 data rows
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing data

### Step 3: Create departments.json file (1 point)
- **Full Credit (1 pt):** File exists with valid JSON containing all 3 departments with budget and head data
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or missing data

### Step 4: Create processed directory (1 point)
- **Full Credit (1 pt):** Directory "data_workspace/processed" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 5: Create backup directory (1 point)
- **Full Credit (1 pt):** Directory "data_workspace/backup" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 6: Copy employees.csv to backup (1 point)
- **Full Credit (1 pt):** File "data_workspace/backup/employees.csv" exists with identical content to original
- **No Credit (0 pts):** Copy not created, wrong location, or content doesn't match original

### Step 7: Create employee count file (1 point)
- **Full Credit (1 pt):** File "data_workspace/processed/employee_count.txt" contains "3"
- **No Credit (0 pts):** File not created, wrong location, or incorrect count

### Step 8: Create high salary CSV (1 point)
- **Full Credit (1 pt):** File "data_workspace/processed/high_salary.csv" contains header and 2 employees with salary >= 65000
- **No Credit (0 pts):** File not created, wrong location, incorrect filtering, or wrong format

### Step 9: Create json_output directory (1 point)
- **Full Credit (1 pt):** Directory "data_workspace/processed/json_output" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 10: Create department list file (1 point)
- **Full Credit (1 pt):** File contains all 3 department names, one per line
- **No Credit (0 pts):** File not created, wrong location, missing departments, or incorrect format

### Step 11: Create total budget file (1 point)
- **Full Credit (1 pt):** File contains "1050000" (sum of all department budgets)
- **No Credit (0 pts):** File not created, wrong location, or incorrect calculation

### Step 12: Create department heads CSV (1 point)
- **Full Credit (1 pt):** File contains CSV with header and all 3 department-head pairs
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing data

### Step 13: Create reports directory (1 point)
- **Full Credit (1 pt):** Directory "data_workspace/reports" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 14: Create high earners list (1 point)
- **Full Credit (1 pt):** File contains "John Smith" and "Jane Doe" on separate lines
- **No Credit (0 pts):** File not created, wrong location, missing names, or incorrect format

### Step 15: Create engineering data JSON (1 point)
- **Full Credit (1 pt):** File contains valid JSON with correct department, employee count, and salary data
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect data

### Step 16: Create temp directory (1 point)
- **Full Credit (1 pt):** Directory "data_workspace/temp" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 17: Move employee count file (1 point)
- **Full Credit (1 pt):** File exists in temp directory AND no longer exists in processed directory
- **No Credit (0 pts):** File not moved, copied instead of moved, or wrong location

### Step 18: Create summary CSV (1 point)
- **Full Credit (1 pt):** File contains CSV with header and correct metric values
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or wrong values

### Step 19: Create metrics JSON (1 point)
- **Full Credit (1 pt):** File contains valid JSON with correct metric key-value pairs
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect values

### Step 20: Create final directory (1 point)
- **Full Credit (1 pt):** Directory "data_workspace/final" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 21: Copy and rename departments file (1 point)
- **Full Credit (1 pt):** File "original_departments.json" exists in final with correct content
- **No Credit (0 pts):** File not created, wrong name/location, or incorrect content

### Step 22: Create budget report (1 point)
- **Full Credit (1 pt):** File contains all departments with correct budget format
- **No Credit (0 pts):** File not created, wrong location, missing data, or incorrect format

### Step 23: Create employee summary JSON (1 point)
- **Full Credit (1 pt):** File contains valid JSON with total and by_department data
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect data

### Step 24: Move high salary file (1 point)
- **Full Credit (1 pt):** File exists in final directory AND no longer exists in processed directory
- **No Credit (0 pts):** File not moved, copied instead of moved, or wrong location

### Step 25: Rename to top performers (1 point)
- **Full Credit (1 pt):** File "top_performers.csv" exists AND "high_salary.csv" no longer exists in final
- **No Credit (0 pts):** Rename not completed, wrong name, or old file still exists

### Step 26: Create archive directory (1 point)
- **Full Credit (1 pt):** Directory "data_workspace/final/archive" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 27: Move summary to archive (1 point)
- **Full Credit (1 pt):** File exists in archive AND no longer exists in temp directory
- **No Credit (0 pts):** File not moved, copied instead of moved, or wrong location

### Step 28: Create processing log (1 point)
- **Full Credit (1 pt):** File contains all specified log content with correct information
- **No Credit (0 pts):** File not created, wrong location, or incorrect/missing content

### Step 29: Create completion status JSON (1 point)
- **Full Credit (1 pt):** File contains valid JSON with correct status and count values
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect values

### Step 30: Create final report (1 point)
- **Full Credit (1 pt):** File "final_report.txt" exists in data_workspace with specified content
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

## Scoring Summary

- **Perfect Score:** 30/30 points
- **Excellent Performance:** 26-29 points (87-97%)
- **Good Performance:** 21-25 points (70-83%)
- **Acceptable Performance:** 18-20 points (60-67%)
- **Needs Improvement:** Below 18 points (<60%)

## Common Deduction Scenarios

1. **Data processing errors:** Deduct full point for incorrect calculations, filtering, or transformations
2. **Format conversion failures:** Deduct full point for invalid JSON, incorrect CSV format, or data loss
3. **File operation failures:** Deduct full point for incomplete moves, failed copies, or wrong locations
4. **Content accuracy:** Deduct full point for files with incorrect or missing content
5. **Dependency failures:** If step fails due to missing prerequisite, deduct point for failed step only

## Critical Validation Points

1. **CSV parsing accuracy:** Employee data correctly processed and filtered
2. **JSON handling:** Valid JSON creation and parsing without syntax errors
3. **Mathematical operations:** Correct counts, sums, and aggregations
4. **File operations:** Proper moves vs copies, correct renaming
5. **Data integrity:** No data loss during transformations

## Validation Commands

To verify data processing accuracy:
```bash
# Check CSV structure
head -1 data_workspace/processed/high_salary.csv
wc -l data_workspace/processed/high_salary.csv

# Validate JSON files
python -m json.tool data_workspace/departments.json
python -m json.tool data_workspace/final/completion_status.json

# Verify calculations
cat data_workspace/processed/json_output/total_budget.txt
cat data_workspace/temp/employee_count.txt
```

Expected final count:
- Directories: 8 total
- Files: 17 total
- JSON files: 5 (all must be valid)
- CSV files: 5 (all must have proper format)