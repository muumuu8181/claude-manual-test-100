# Test 12: Scoring Guide

**Total Points: 40 (1 point per step)**

## Scoring Criteria

### Step 1: Create complex_workspace directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect name

### Step 2: Create state_tracking directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/state_tracking" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 3: Create initial system_state.json (1 point)
- **Full Credit (1 pt):** File exists with valid JSON containing all required fields with correct initial values
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or missing/incorrect fields

### Step 4: Create operations directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/operations" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 5: Create data_processing directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/operations/data_processing" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 6: Create input_data.csv (1 point)
- **Full Credit (1 pt):** File exists with exact CSV content including header and 4 data rows
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing/wrong data

### Step 7: Update system_state.json after data loading (1 point)
- **Full Credit (1 pt):** JSON updated with operations_completed: 1 and phase: "data_loaded"
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 8: Create transformations directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/operations/transformations" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 9: Create active_records.csv (1 point)
- **Full Credit (1 pt):** File exists with correct CSV format containing exactly 3 active records
- **No Credit (0 pts):** File not created, wrong location, incorrect filtering, or wrong format

### Step 10: Create value_summary.json (1 point)
- **Full Credit (1 pt):** File exists with valid JSON containing correct calculations (total_value: 525, etc.)
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect calculations

### Step 11: Update system_state.json with processing phase (1 point)
- **Full Credit (1 pt):** JSON updated with incremented operations_completed, phase: "processing", and milestones array with "data_transformed"
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 12: Create validation directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/operations/validation" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 13: Create validation_passed.txt (conditional) (1 point)
- **Full Credit (1 pt):** File created in validation directory with exact content (since active_records.csv exists)
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 14: Create calculation_verified.txt (conditional) (1 point)
- **Full Credit (1 pt):** File created with exact content (since value_summary.json exists with correct total_value)
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 15: Create backup_system directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/backup_system" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 16: Copy and rename system_state.json (1 point)
- **Full Credit (1 pt):** File "state_backup_checkpoint1.json" exists in backup_system with same content as system_state.json
- **No Credit (0 pts):** Copy not created, wrong name/location, or content doesn't match

### Step 17: Copy input_data.csv to backup (1 point)
- **Full Credit (1 pt):** File exists in backup_system with identical content to original
- **No Credit (0 pts):** Copy not created, wrong location, or content doesn't match

### Step 18: Update system_state.json with backup milestone (1 point)
- **Full Credit (1 pt):** JSON updated with incremented operations_completed, "backup_created" added to milestones, last_checkpoint: "checkpoint1"
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 19: Create error_simulation directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/error_simulation" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 20: Create error_trigger.txt (1 point)
- **Full Credit (1 pt):** File exists in error_simulation with exact content "simulated_error_scenario"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 21: Create error_log.json (conditional) (1 point)
- **Full Credit (1 pt):** File created in state_tracking with valid JSON containing error details (since missing_dependency.txt doesn't exist)
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect content

### Step 22: Update system_state.json with error detection (1 point)
- **Full Credit (1 pt):** JSON updated with "error_detected" in errors array and phase: "error_recovery"
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 23: Create recovery_operations directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/recovery_operations" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 24: Create missing_dependency.txt (1 point)
- **Full Credit (1 pt):** File exists in error_simulation with content "dependency_restored"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 25: Update error_log.json to resolved (1 point)
- **Full Credit (1 pt):** JSON updated with "resolved": true
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect value

### Step 26: Update system_state.json with recovery completion (1 point)
- **Full Credit (1 pt):** JSON updated with "error_detected" removed from errors, phase: "recovery_complete", "error_resolved" added to milestones
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 27: Create advanced_processing directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/operations/advanced_processing" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 28: Create high_value_records.csv (1 point)
- **Full Credit (1 pt):** File exists with correct CSV containing exactly 2 records with value >= 100
- **No Credit (0 pts):** File not created, wrong location, incorrect filtering, or wrong format

### Step 29: Create analytics directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/operations/advanced_processing/analytics" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 30: Create analytics_report.json (1 point)
- **Full Credit (1 pt):** File exists with valid JSON containing correct count and average for high-value records
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect calculations

### Step 31: Create final_outputs directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/final_outputs" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 32: Move active_records.csv to final_outputs (1 point)
- **Full Credit (1 pt):** File exists in final_outputs AND no longer exists in transformations directory
- **No Credit (0 pts):** File not moved, copied instead of moved, or wrong location

### Step 33: Move high_value_records.csv to final_outputs (1 point)
- **Full Credit (1 pt):** File exists in final_outputs AND no longer exists in advanced_processing directory
- **No Credit (0 pts):** File not moved, copied instead of moved, or wrong location

### Step 34: Create metadata directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/final_outputs/metadata" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 35: Copy and rename system_state.json to final_state.json (1 point)
- **Full Credit (1 pt):** File "final_state.json" exists in metadata with same content as current system_state.json
- **No Credit (0 pts):** Copy not created, wrong name/location, or content doesn't match

### Step 36: Update system_state.json to completed (1 point)
- **Full Credit (1 pt):** JSON updated with phase: "completed", "outputs_finalized" added to milestones, last_checkpoint: "final"
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 37: Create operation_summary.txt (1 point)
- **Full Credit (1 pt):** File exists in final_outputs with exact summary content including all statistics
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 38: Create execution_report.json (1 point)
- **Full Credit (1 pt):** File exists with valid JSON containing operations summary and milestones from final_state.json
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect content

### Step 39: Create archive directory (1 point)
- **Full Credit (1 pt):** Directory "complex_workspace/archive" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 40: Create test_completion_certificate.txt (1 point)
- **Full Credit (1 pt):** File exists in complex_workspace with exact certificate content
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

## Scoring Summary

- **Perfect Score:** 40/40 points (100%)
- **Excellent Performance:** 36-39 points (90-98%)
- **Good Performance:** 32-35 points (80-88%)
- **Acceptable Performance:** 24-31 points (60-78%)
- **Needs Improvement:** Below 24 points (<60%)

## Common Deduction Scenarios

1. **State tracking failures:** Deduct full point for incorrect JSON updates, missing fields, or wrong state progression
2. **Calculation errors:** Deduct full point for incorrect mathematical operations (sums, averages, counts)
3. **Conditional logic failures:** Deduct full point if conditional operations don't execute based on proper file/content checks
4. **File operation failures:** Deduct full point for incomplete moves, failed copies, or wrong locations
5. **JSON validity:** Deduct full point for any syntactically invalid JSON files
6. **Content accuracy:** Deduct full point for files with incorrect or missing content

## Critical Validation Points

1. **State consistency:** system_state.json should accurately track all operations and phase transitions
2. **Error handling:** Error simulation and recovery should execute correctly with proper state updates
3. **Data processing:** All CSV filtering and JSON calculations must be accurate
4. **File operations:** Proper distinction between moves and copies, with source files removed after moves
5. **Conditional execution:** All conditional steps should execute based on correct file existence/content checks
6. **Milestone tracking:** All milestones should be properly added to the milestones array
7. **Phase progression:** States should follow: setup → data_loaded → processing → error_recovery → recovery_complete → completed

## Validation Commands

To verify state tracking and complex operations:
```bash
# Check final state progression
cat complex_workspace/state_tracking/system_state.json | grep -E '"phase"|"operations_completed"|"milestones"'

# Verify all JSON files are valid
find complex_workspace -name "*.json" -exec python -m json.tool {} \;

# Check file movements completed
ls complex_workspace/final_outputs/active_records.csv  # Should exist
ls complex_workspace/operations/transformations/active_records.csv  # Should NOT exist
ls complex_workspace/final_outputs/high_value_records.csv  # Should exist
ls complex_workspace/operations/advanced_processing/high_value_records.csv  # Should NOT exist

# Verify calculations
cat complex_workspace/operations/transformations/value_summary.json  # total_value should be 525
cat complex_workspace/operations/advanced_processing/analytics/analytics_report.json  # average should be 125.0
```

Expected final count:
- Directories: 11 total (2 empty: recovery_operations, archive)
- Files: 17 total
- JSON files: 6 (all must be syntactically valid)
- CSV files: 4 (all must have proper format and correct data)
- State progression: 6 distinct phases
- Milestones achieved: 4 total