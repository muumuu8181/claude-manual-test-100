# Test 11: Scoring Guide

**Total Points: 35 (1 point per step)**

## Scoring Criteria

### Step 1: Create script_workspace directory (1 point)
- **Full Credit (1 pt):** Directory "script_workspace" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect name

### Step 2: Create scripts directory (1 point)
- **Full Credit (1 pt):** Directory "script_workspace/scripts" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 3: Create logs directory (1 point)
- **Full Credit (1 pt):** Directory "script_workspace/logs" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 4: Create setup.sh script (1 point)
- **Full Credit (1 pt):** File exists with exact bash script content including shebang and all commands
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 5: Create process_data.py script (1 point)
- **Full Credit (1 pt):** File exists with exact Python code including imports and conditional logic
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 6: Create cleanup.bat script (1 point)
- **Full Credit (1 pt):** File exists with exact batch script content including all commands
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 7: Create validation.js script (1 point)
- **Full Credit (1 pt):** File exists with exact JavaScript code including require and conditional logic
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 8: Create temp_data directory (1 point)
- **Full Credit (1 pt):** Directory "script_workspace/temp_data" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 9: Create data.txt file (1 point)
- **Full Credit (1 pt):** File exists in temp_data with exact content "sample_data_content"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 10: Create config.json file (1 point)
- **Full Credit (1 pt):** File exists with valid JSON containing all specified fields
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or missing fields

### Step 11: Conditional error log creation (1 point)
- **Full Credit (1 pt):** File "error_log.txt" created in logs directory with specified error message
- **No Credit (0 pts):** File not created (missing_script.py should not exist), wrong location, or incorrect content

### Step 12: Create backup_scripts directory (1 point)
- **Full Credit (1 pt):** Directory "script_workspace/backup_scripts" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 13: Copy setup.sh to backup (1 point)
- **Full Credit (1 pt):** File exists in backup_scripts with identical content to original
- **No Credit (0 pts):** Copy not created, wrong location, or content doesn't match

### Step 14: Copy process_data.py to backup (1 point)
- **Full Credit (1 pt):** File exists in backup_scripts with identical content to original
- **No Credit (0 pts):** Copy not created, wrong location, or content doesn't match

### Step 15: Create monitor.py script (1 point)
- **Full Credit (1 pt):** File exists with exact Python code including try/except logic
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 16: Create status.txt (monitor logic simulation) (1 point)
- **Full Credit (1 pt):** File "status.txt" created in script_workspace with content "initialized"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 17: Create error_recovery directory (1 point)
- **Full Credit (1 pt):** Directory "script_workspace/error_recovery" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 18: Create recovery.sh script (1 point)
- **Full Credit (1 pt):** File exists with exact bash script including conditional logic
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 19: Create status_backup.txt (1 point)
- **Full Credit (1 pt):** File created in logs with content matching status.txt ("initialized")
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 20: Create test_runner.py script (1 point)
- **Full Credit (1 pt):** File exists with exact Python code including imports and loop logic
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 21: Create test_results.txt (test runner simulation) (1 point)
- **Full Credit (1 pt):** File created in logs showing "FOUND" for both setup.sh and process_data.py
- **No Credit (0 pts):** File not created, wrong location, or incorrect results

### Step 22: Create validation_scripts directory (1 point)
- **Full Credit (1 pt):** Directory "script_workspace/validation_scripts" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 23: Move validation.js (1 point)
- **Full Credit (1 pt):** File exists in validation_scripts AND no longer exists in scripts directory
- **No Credit (0 pts):** File not moved, copied instead of moved, or wrong location

### Step 24: Create validate_all.py script (1 point)
- **Full Credit (1 pt):** File exists with exact Python code including file checking logic
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 25: Create validation_results.txt (validation simulation) (1 point)
- **Full Credit (1 pt):** File created in logs showing "VALID" for both required files
- **No Credit (0 pts):** File not created, wrong location, or incorrect results

### Step 26: Create error_handler.py script (1 point)
- **Full Credit (1 pt):** File exists with exact Python code including file existence checking
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 27: Create recovery_actions.txt (error handler simulation) (1 point)
- **Full Credit (1 pt):** File created in error_recovery with content "Action: Recreate missing files"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 28: Create final_scripts directory (1 point)
- **Full Credit (1 pt):** Directory "script_workspace/final_scripts" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 29: Copy monitor.py to final (1 point)
- **Full Credit (1 pt):** File exists in final_scripts with identical content to original
- **No Credit (0 pts):** Copy not created, wrong location, or content doesn't match

### Step 30: Copy test_runner.py to final (1 point)
- **Full Credit (1 pt):** File exists in final_scripts with identical content to original
- **No Credit (0 pts):** Copy not created, wrong location, or content doesn't match

### Step 31: Create deployment.sh script (1 point)
- **Full Credit (1 pt):** File exists with exact bash script including prerequisite checking
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 32: Create deployment_log.txt (deployment simulation) (1 point)
- **Full Credit (1 pt):** File created in logs with "Prerequisites met - Deployment successful"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 33: Create cleanup_all.py script (1 point)
- **Full Credit (1 pt):** File exists with exact Python code including directory checking logic
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 34: Create final_report.txt (1 point)
- **Full Credit (1 pt):** File exists in logs with exact report content including all statistics
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 35: Create test_summary.json (1 point)
- **Full Credit (1 pt):** File exists with valid JSON containing all specified fields and values
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect data

## Scoring Summary

- **Perfect Score:** 35/35 points
- **Excellent Performance:** 30-34 points (86-97%)
- **Good Performance:** 26-29 points (74-83%)
- **Acceptable Performance:** 21-25 points (60-71%)
- **Needs Improvement:** Below 21 points (<60%)

## Common Deduction Scenarios

1. **Script content errors:** Deduct full point for incorrect syntax, missing imports, or wrong logic
2. **Conditional logic failures:** Deduct full point if error handling scenarios don't execute properly
3. **File operation failures:** Deduct full point for incomplete moves, failed copies, or wrong locations
4. **Simulation logic errors:** Deduct full point if simulated script behavior produces wrong outputs
5. **Content accuracy:** Deduct full point for files with incorrect or missing content

## Critical Validation Points

1. **Script syntax accuracy:** All scripts should have correct syntax for their language
2. **Error handling implementation:** Conditional operations should execute based on file existence
3. **File operations:** Proper distinction between moves and copies
4. **Simulation accuracy:** Logic simulation should produce correct outputs based on file states
5. **JSON validity:** All JSON files must be syntactically correct

## Validation Commands

To verify script creation and error handling:
```bash
# Check script file counts by type
find script_workspace -name "*.py" | wc -l    # Should be 7
find script_workspace -name "*.sh" | wc -l    # Should be 3
find script_workspace -name "*.js" | wc -l    # Should be 1
find script_workspace -name "*.bat" | wc -l   # Should be 1

# Validate JSON files
python -m json.tool script_workspace/temp_data/config.json
python -m json.tool script_workspace/test_summary.json

# Check conditional file creation
ls script_workspace/logs/error_log.txt          # Should exist
ls script_workspace/error_recovery/recovery_actions.txt  # Should exist
```

Expected final count:
- Directories: 8 total
- Files: 21 total  
- Script files: 12 (Python: 7, Bash: 3, JavaScript: 1, Batch: 1)
- Log files: 6
- Data files: 3
- All conditional files should be created based on specified logic