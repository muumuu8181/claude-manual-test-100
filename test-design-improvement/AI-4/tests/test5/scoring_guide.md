# Test5 Scoring Guide

## Scoring Criteria: 1 Point Per Step (Total: 12 Points)

### Step 1 (1 point)
- **Requirement:** Create directory "projects"
- **Full Credit (1 pt):** Directory "projects" exists and is accessible
- **No Credit (0 pt):** Directory not created or wrong name

### Step 2 (1 point)
- **Requirement:** Create directory "documents" inside "projects"
- **Full Credit (1 pt):** Directory "projects/documents" exists and is accessible
- **No Credit (0 pt):** Directory not created, wrong location, or wrong name

### Step 3 (1 point)
- **Requirement:** Create directory "reports" inside "projects"
- **Full Credit (1 pt):** Directory "projects/reports" exists and is accessible
- **No Credit (0 pt):** Directory not created, wrong location, or wrong name

### Step 4 (1 point)
- **Requirement:** Create directory "archive" inside "documents"
- **Full Credit (1 pt):** Directory "projects/documents/archive" exists and is accessible
- **No Credit (0 pt):** Directory not created, wrong location, or wrong name

### Step 5 (1 point)
- **Requirement:** Create directory "templates" inside "documents"
- **Full Credit (1 pt):** Directory "projects/documents/templates" exists and is accessible
- **No Credit (0 pt):** Directory not created, wrong location, or wrong name

### Step 6 (1 point)
- **Requirement:** Create file "readme.txt" inside "projects"
- **Full Credit (1 pt):** File "projects/readme.txt" exists
- **No Credit (0 pt):** File not created, wrong location, or wrong name

### Step 7 (1 point)
- **Requirement:** Create file "project_list.txt" inside "documents"
- **Full Credit (1 pt):** File "projects/documents/project_list.txt" exists
- **No Credit (0 pt):** File not created, wrong location, or wrong name

### Step 8 (1 point)
- **Requirement:** Create file "monthly_report.txt" inside "reports"
- **Full Credit (1 pt):** File "projects/reports/monthly_report.txt" exists
- **No Credit (0 pt):** File not created, wrong location, or wrong name

### Step 9 (1 point)
- **Requirement:** Create file "old_data.txt" inside "archive"
- **Full Credit (1 pt):** File "projects/documents/archive/old_data.txt" exists
- **No Credit (0 pt):** File not created, wrong location, or wrong name

### Step 10 (1 point)
- **Requirement:** Create file "template_basic.txt" inside "templates"
- **Full Credit (1 pt):** File "projects/documents/templates/template_basic.txt" exists
- **No Credit (0 pt):** File not created, wrong location, or wrong name

### Step 11 (1 point)
- **Requirement:** Create file "summary.txt" inside "reports"
- **Full Credit (1 pt):** File "projects/reports/summary.txt" exists
- **No Credit (0 pt):** File not created, wrong location, or wrong name

### Step 12 (1 point)
- **Requirement:** Create file "backup_info.txt" inside "archive"
- **Full Credit (1 pt):** File "projects/documents/archive/backup_info.txt" exists
- **No Credit (0 pt):** File not created, wrong location, or wrong name

## Scoring Summary

- **Maximum Score:** 12 points
- **Pass Threshold:** 10 points (83.3%)
- **Evaluation Method:** Binary scoring (1 or 0) for each step
- **Dependency Considerations:** Later steps depend on earlier directory creation steps

## Common Deduction Reasons

1. **Wrong naming:** Case sensitivity, typos, extra characters
2. **Wrong location:** Files/directories created in incorrect parent directories
3. **Missing dependencies:** Attempting to create items in non-existent parent directories
4. **Incomplete execution:** Stopping before completing all 12 steps
5. **Path errors:** Using incorrect relative or absolute paths

## Evaluation Notes

- Each step must be completed in sequence
- Dependencies between steps are critical for success
- File content is not evaluated (empty files are acceptable)
- Directory and file names must match exactly as specified