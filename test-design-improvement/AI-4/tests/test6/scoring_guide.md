# Test6 Scoring Guide

## Scoring Criteria: 1 Point Per Step (Total: 15 Points)

### Step 1 (1 point)
- **Requirement:** Create file "base_info.txt" with content "alpha"
- **Full Credit (1 pt):** File exists with exact content "alpha"
- **No Credit (0 pt):** File not created, wrong name, or wrong content

### Step 2 (1 point)
- **Requirement:** Create file "config_data.txt" with content "beta"
- **Full Credit (1 pt):** File exists with exact content "beta"
- **No Credit (0 pt):** File not created, wrong name, or wrong content

### Step 3 (1 point)
- **Requirement:** Create file "settings.txt" with content "gamma"
- **Full Credit (1 pt):** File exists with exact content "gamma"
- **No Credit (0 pt):** File not created, wrong name, or wrong content

### Step 4 (1 point)
- **Requirement:** Read base_info.txt and create "alpha_log.txt"
- **Full Credit (1 pt):** File "alpha_log.txt" exists (demonstrates reading and using content)
- **No Credit (0 pt):** Wrong filename or file not created

### Step 5 (1 point)
- **Requirement:** Read config_data.txt and create "beta_settings.txt"
- **Full Credit (1 pt):** File "beta_settings.txt" exists
- **No Credit (0 pt):** Wrong filename or file not created

### Step 6 (1 point)
- **Requirement:** Read settings.txt and create "gamma_backup.txt"
- **Full Credit (1 pt):** File "gamma_backup.txt" exists
- **No Credit (0 pt):** Wrong filename or file not created

### Step 7 (1 point)
- **Requirement:** Create file "name_list.txt" with content "delta"
- **Full Credit (1 pt):** File exists with exact content "delta"
- **No Credit (0 pt):** File not created, wrong name, or wrong content

### Step 8 (1 point)
- **Requirement:** Create file "project_code.txt" with content "epsilon"
- **Full Credit (1 pt):** File exists with exact content "epsilon"
- **No Credit (0 pt):** File not created, wrong name, or wrong content

### Step 9 (1 point)
- **Requirement:** Read name_list.txt and create "delta_report.txt"
- **Full Credit (1 pt):** File "delta_report.txt" exists
- **No Credit (0 pt):** Wrong filename or file not created

### Step 10 (1 point)
- **Requirement:** Read project_code.txt and create "epsilon_data.txt"
- **Full Credit (1 pt):** File "epsilon_data.txt" exists
- **No Credit (0 pt):** Wrong filename or file not created

### Step 11 (1 point)
- **Requirement:** Create file "final_key.txt" with content "omega"
- **Full Credit (1 pt):** File exists with exact content "omega"
- **No Credit (0 pt):** File not created, wrong name, or wrong content

### Step 12 (1 point)
- **Requirement:** Read final_key.txt and create "omega_summary.txt"
- **Full Credit (1 pt):** File "omega_summary.txt" exists
- **No Credit (0 pt):** Wrong filename or file not created

### Step 13 (1 point)
- **Requirement:** Create directory "results"
- **Full Credit (1 pt):** Directory "results" exists and is accessible
- **No Credit (0 pt):** Directory not created or wrong name

### Step 14 (1 point)
- **Requirement:** Read base_info.txt and create "alpha_final.txt" in results directory
- **Full Credit (1 pt):** File "results/alpha_final.txt" exists
- **No Credit (0 pt):** Wrong filename, wrong location, or file not created

### Step 15 (1 point)
- **Requirement:** Read final_key.txt and create "omega_archive.txt" in results directory
- **Full Credit (1 pt):** File "results/omega_archive.txt" exists
- **No Credit (0 pt):** Wrong filename, wrong location, or file not created

## Scoring Summary

- **Maximum Score:** 15 points
- **Pass Threshold:** 12 points (80%)
- **Evaluation Method:** Binary scoring (1 or 0) for each step
- **Critical Dependencies:** Content-reading steps depend on successful creation and exact content of source files

## Common Deduction Reasons

1. **Incorrect content:** Source files contain wrong text (affects downstream naming)
2. **Wrong filename derivation:** Not reading content correctly or using wrong content for naming
3. **Missing files:** Not creating required files or directories
4. **Content reading errors:** Not properly reading file content before using it for naming
5. **Path errors:** Creating files in wrong directories (especially Steps 14-15)
6. **Case sensitivity:** Using wrong case in filenames or content

## Content Dependencies

**Critical Content Dependencies:**
- Steps 4, 14: Depend on "alpha" from base_info.txt
- Step 5: Depends on "beta" from config_data.txt
- Step 6: Depends on "gamma" from settings.txt
- Step 9: Depends on "delta" from name_list.txt
- Step 10: Depends on "epsilon" from project_code.txt
- Steps 12, 15: Depend on "omega" from final_key.txt

## Evaluation Notes

- Content must be exact (no extra spaces, newlines, or characters)
- File reading operations are critical for success
- Steps 14-15 require both content reading AND correct directory placement
- Empty derived files are acceptable (content not specified for them)