# Test7 Scoring Guide

## Scoring Criteria: 1 Point Per Step (Total: 18 Points)

### Step 1 (1 point)
- **Requirement:** Create file "original_file.txt"
- **Full Credit (1 pt):** File "original_file.txt" exists
- **No Credit (0 pt):** File not created or wrong name

### Step 2 (1 point)
- **Requirement:** Create file "temp_data.txt"
- **Full Credit (1 pt):** File "temp_data.txt" exists
- **No Credit (0 pt):** File not created or wrong name

### Step 3 (1 point)
- **Requirement:** Create file "backup_file.txt"
- **Full Credit (1 pt):** File "backup_file.txt" exists
- **No Credit (0 pt):** File not created or wrong name

### Step 4 (1 point)
- **Requirement:** Rename "original_file.txt" to "renamed_file.txt"
- **Full Credit (1 pt):** File "renamed_file.txt" exists and "original_file.txt" does not exist
- **No Credit (0 pt):** Original file still exists or wrong new name

### Step 5 (1 point)
- **Requirement:** Create directory "storage"
- **Full Credit (1 pt):** Directory "storage" exists and is accessible
- **No Credit (0 pt):** Directory not created or wrong name

### Step 6 (1 point)
- **Requirement:** Move "renamed_file.txt" into "storage" directory
- **Full Credit (1 pt):** File "storage/renamed_file.txt" exists and no "renamed_file.txt" in root
- **No Credit (0 pt):** File not moved or still exists in original location

### Step 7 (1 point)
- **Requirement:** Create file "config.txt" inside "storage" directory
- **Full Credit (1 pt):** File "storage/config.txt" exists
- **No Credit (0 pt):** File not created, wrong name, or wrong location

### Step 8 (1 point)
- **Requirement:** Rename "temp_data.txt" to "processed_data.txt"
- **Full Credit (1 pt):** File "processed_data.txt" exists and "temp_data.txt" does not exist
- **No Credit (0 pt):** Original file still exists or wrong new name

### Step 9 (1 point)
- **Requirement:** Create directory "archive"
- **Full Credit (1 pt):** Directory "archive" exists and is accessible
- **No Credit (0 pt):** Directory not created or wrong name

### Step 10 (1 point)
- **Requirement:** Move "backup_file.txt" into "archive" directory
- **Full Credit (1 pt):** File "archive/backup_file.txt" exists and no "backup_file.txt" in root
- **No Credit (0 pt):** File not moved or still exists in original location

### Step 11 (1 point)
- **Requirement:** Rename "backup_file.txt" in archive to "old_backup.txt"
- **Full Credit (1 pt):** File "archive/old_backup.txt" exists and "archive/backup_file.txt" does not exist
- **No Credit (0 pt):** Original file still exists or wrong new name

### Step 12 (1 point)
- **Requirement:** Create file "index.txt" inside "archive" directory
- **Full Credit (1 pt):** File "archive/index.txt" exists
- **No Credit (0 pt):** File not created, wrong name, or wrong location

### Step 13 (1 point)
- **Requirement:** Move "processed_data.txt" into "storage" directory
- **Full Credit (1 pt):** File "storage/processed_data.txt" exists and no "processed_data.txt" in root
- **No Credit (0 pt):** File not moved or still exists in original location

### Step 14 (1 point)
- **Requirement:** Rename "processed_data.txt" in storage to "final_data.txt"
- **Full Credit (1 pt):** File "storage/final_data.txt" exists and "storage/processed_data.txt" does not exist
- **No Credit (0 pt):** Original file still exists or wrong new name

### Step 15 (1 point)
- **Requirement:** Create file "log.txt" inside "storage" directory
- **Full Credit (1 pt):** File "storage/log.txt" exists
- **No Credit (0 pt):** File not created, wrong name, or wrong location

### Step 16 (1 point)
- **Requirement:** Create directory "completed" inside "storage" directory
- **Full Credit (1 pt):** Directory "storage/completed" exists and is accessible
- **No Credit (0 pt):** Directory not created, wrong name, or wrong location

### Step 17 (1 point)
- **Requirement:** Move "final_data.txt" from storage to "storage/completed"
- **Full Credit (1 pt):** File "storage/completed/final_data.txt" exists and no "storage/final_data.txt"
- **No Credit (0 pt):** File not moved or still exists in original location

### Step 18 (1 point)
- **Requirement:** Rename "final_data.txt" in "storage/completed" to "archived_data.txt"
- **Full Credit (1 pt):** File "storage/completed/archived_data.txt" exists and "storage/completed/final_data.txt" does not exist
- **No Credit (0 pt):** Original file still exists or wrong new name

## Scoring Summary

- **Maximum Score:** 18 points
- **Pass Threshold:** 14 points (77.8%)
- **Evaluation Method:** Binary scoring (1 or 0) for each step
- **Critical Dependencies:** Later steps must reference files by their current (renamed) names

## Common Deduction Reasons

1. **Name tracking errors:** Using old names instead of current (renamed) names
2. **Incomplete operations:** Files exist in both old and new locations after move/rename
3. **Wrong references:** Attempting to reference files by outdated names
4. **Location errors:** Creating or moving files to wrong directories
5. **Sequence errors:** Attempting operations before dependencies are met
6. **Missing clean-up:** Original files/names still exist after rename operations

## Critical Name Dependencies

**Steps that depend on previous renames:**
- Step 6: Must reference "renamed_file.txt" (not "original_file.txt")
- Step 11: Must reference "backup_file.txt" in archive directory
- Step 13: Must reference "processed_data.txt" (not "temp_data.txt")
- Step 14: Must reference "processed_data.txt" in storage directory
- Step 17: Must reference "final_data.txt" (not "processed_data.txt")
- Step 18: Must reference "final_data.txt" in completed directory

## Evaluation Notes

- Rename operations must be complete (old name disappears, new name appears)
- Move operations must be complete (file appears only in new location)
- Directory structure must match exactly as specified
- Each step builds on the current state from all previous steps
- File tracking through multiple rename/move operations is critical for success