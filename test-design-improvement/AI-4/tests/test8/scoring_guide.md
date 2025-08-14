# Test8 Scoring Guide

## Scoring Criteria: 1 Point Per Step (Total: 20 Points)

### Step 1 (1 point)
- **Requirement:** Create directory "workspace"
- **Full Credit (1 pt):** Directory "workspace" exists and is accessible
- **No Credit (0 pt):** Directory not created or wrong name

### Step 2 (1 point)
- **Requirement:** Create file "input.txt" with content "start"
- **Full Credit (1 pt):** File exists with exact content "start"
- **No Credit (0 pt):** File not created, wrong name, or wrong content

### Step 3 (1 point)
- **Requirement:** Create file "config.json" inside workspace directory
- **Full Credit (1 pt):** File "workspace/config.json" exists
- **No Credit (0 pt):** File not created, wrong name, or wrong location

### Step 4 (1 point)
- **Requirement:** Read input.txt and create "start_process.txt"
- **Full Credit (1 pt):** File "start_process.txt" exists (demonstrates reading and using "start")
- **No Credit (0 pt):** Wrong filename or file not created

### Step 5 (1 point)
- **Requirement:** Create directory "temp" inside workspace
- **Full Credit (1 pt):** Directory "workspace/temp" exists and is accessible
- **No Credit (0 pt):** Directory not created, wrong name, or wrong location

### Step 6 (1 point)
- **Requirement:** Move "start_process.txt" into workspace/temp
- **Full Credit (1 pt):** File "workspace/temp/start_process.txt" exists, no file in root
- **No Credit (0 pt):** File not moved or still exists in original location

### Step 7 (1 point)
- **Requirement:** Check for missing_file.txt (doesn't exist), create error_log.txt with "file_not_found"
- **Full Credit (1 pt):** File "error_log.txt" exists with content "file_not_found"
- **No Credit (0 pt):** File not created or wrong content (condition should trigger creation)

### Step 8 (1 point)
- **Requirement:** Create file "data.txt" with content "processing"
- **Full Credit (1 pt):** File exists with exact content "processing"
- **No Credit (0 pt):** File not created, wrong name, or wrong content

### Step 9 (1 point)
- **Requirement:** Read data.txt and create "processing_dir" directory
- **Full Credit (1 pt):** Directory "processing_dir" exists (demonstrates using "processing")
- **No Credit (0 pt):** Wrong directory name or directory not created

### Step 10 (1 point)
- **Requirement:** Create file "status.txt" inside processing_dir
- **Full Credit (1 pt):** File "processing_dir/status.txt" exists
- **No Credit (0 pt):** File not created, wrong name, or wrong location

### Step 11 (1 point)
- **Requirement:** Rename "config.json" in workspace to "settings.json"
- **Full Credit (1 pt):** File "workspace/settings.json" exists, no "workspace/config.json"
- **No Credit (0 pt):** Original file still exists or wrong new name

### Step 12 (1 point)
- **Requirement:** Copy error_log.txt into workspace (conditional on existence)
- **Full Credit (1 pt):** File "workspace/error_log.txt" exists (condition should be met from Step 7)
- **No Credit (0 pt):** File not copied or condition incorrectly handled

### Step 13 (1 point)
- **Requirement:** Create file "output.txt" with content "complete"
- **Full Credit (1 pt):** File exists with exact content "complete"
- **No Credit (0 pt):** File not created, wrong name, or wrong content

### Step 14 (1 point)
- **Requirement:** Check if workspace/settings.json exists, create validation_passed.txt
- **Full Credit (1 pt):** File "validation_passed.txt" exists (condition should be met from Step 11)
- **No Credit (0 pt):** File not created or condition incorrectly handled

### Step 15 (1 point)
- **Requirement:** Move "data.txt" into processing_dir
- **Full Credit (1 pt):** File "processing_dir/data.txt" exists, no file in root
- **No Credit (0 pt):** File not moved or still exists in original location

### Step 16 (1 point)
- **Requirement:** Rename "data.txt" in processing_dir to "processed_data.txt"
- **Full Credit (1 pt):** File "processing_dir/processed_data.txt" exists, no "processing_dir/data.txt"
- **No Credit (0 pt):** Original file still exists or wrong new name

### Step 17 (1 point)
- **Requirement:** Create directory "results" inside workspace
- **Full Credit (1 pt):** Directory "workspace/results" exists and is accessible
- **No Credit (0 pt):** Directory not created, wrong name, or wrong location

### Step 18 (1 point)
- **Requirement:** Move "output.txt" into workspace/results
- **Full Credit (1 pt):** File "workspace/results/output.txt" exists, no file in root
- **No Credit (0 pt):** File not moved or still exists in original location

### Step 19 (1 point)
- **Requirement:** Read output.txt in results and create "complete_summary.txt" in same directory
- **Full Credit (1 pt):** File "workspace/results/complete_summary.txt" exists (uses "complete")
- **No Credit (0 pt):** Wrong filename or file not created

### Step 20 (1 point)
- **Requirement:** Create "final_report.txt" in workspace with content "test_finished"
- **Full Credit (1 pt):** File "workspace/final_report.txt" exists with content "test_finished"
- **No Credit (0 pt):** File not created, wrong location, or wrong content

## Scoring Summary

- **Maximum Score:** 20 points
- **Pass Threshold:** 16 points (80%)
- **Evaluation Method:** Binary scoring (1 or 0) for each step
- **Conditional Steps:** Steps 7, 12, 14 depend on file existence conditions

## Common Deduction Reasons

1. **Conditional logic errors:** Not handling file existence checks correctly
2. **Content reading errors:** Not using file content correctly for naming
3. **Name tracking errors:** Using wrong names after rename operations
4. **Move/copy confusion:** Files existing in wrong locations
5. **Dependency violations:** Attempting operations before prerequisites
6. **Wrong content:** Files containing incorrect specified content

## Critical Conditional Operations

**Step 7:** Should create error_log.txt because missing_file.txt doesn't exist
**Step 12:** Should copy error_log.txt because it exists from Step 7
**Step 14:** Should create validation_passed.txt because settings.json exists from Step 11

## Content Dependencies

**Critical Content Dependencies:**
- Step 4: Uses "start" from input.txt
- Step 9: Uses "processing" from data.txt
- Step 19: Uses "complete" from output.txt

## Evaluation Notes

- All conditional operations should execute successfully in normal test conditions
- File existence checks must be performed correctly
- Content reading must be exact (no extra whitespace or characters)
- Multiple files may exist in different locations (originals + copies)
- Directory structure must be precisely as specified
- Move operations must be complete (file disappears from source)
- Rename operations must be complete (old name disappears)