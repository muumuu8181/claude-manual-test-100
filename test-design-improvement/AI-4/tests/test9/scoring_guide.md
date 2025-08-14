# Test 9: Scoring Guide

**Total Points: 25 (1 point per step)**

## Scoring Criteria

### Step 1: Create project_root directory (1 point)
- **Full Credit (1 pt):** Directory "project_root" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect name

### Step 2: Create src directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/src" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 3: Create assets directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/assets" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 4: Create config directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/config" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 5: Create main.txt file (1 point)
- **Full Credit (1 pt):** File "project_root/src/main.txt" exists with content "application_entry"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 6: Create components directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/src/components" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 7: Create utils directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/src/utils" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 8: Create helper.txt file (1 point)
- **Full Credit (1 pt):** File "project_root/src/utils/helper.txt" exists with content "utility_functions"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 9: Create images directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/assets/images" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 10: Create styles directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/assets/styles" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 11: Create logo.txt file (1 point)
- **Full Credit (1 pt):** File "project_root/assets/images/logo.txt" exists with content "brand_image"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 12: Create theme.txt file (1 point)
- **Full Credit (1 pt):** File "project_root/assets/styles/theme.txt" exists with content "visual_design"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 13: Create settings.txt file (1 point)
- **Full Credit (1 pt):** File "project_root/config/settings.txt" exists with content "app_configuration"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 14: Create backup directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/backup" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 15: Copy and rename main.txt (1 point)
- **Full Credit (1 pt):** File "project_root/backup/main_backup.txt" exists with content "application_entry" AND original file still exists at "project_root/src/main.txt"
- **No Credit (0 pts):** Copy not created, wrong name/location, incorrect content, or original file removed

### Step 16: Create archive directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/backup/archive" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 17: Move helper.txt to archive (1 point)
- **Full Credit (1 pt):** File "project_root/backup/archive/helper.txt" exists with content "utility_functions" AND original file no longer exists at "project_root/src/utils/helper.txt"
- **No Credit (0 pts):** File not moved, wrong location, incorrect content, or original file still exists

### Step 18: Create index.txt file (1 point)
- **Full Credit (1 pt):** File "project_root/src/components/index.txt" exists with content "component_list"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 19: Create temp directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/src/components/temp" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 20: Copy logo.txt to temp (1 point)
- **Full Credit (1 pt):** File "project_root/src/components/temp/logo.txt" exists with content "brand_image" AND original file still exists at "project_root/assets/images/logo.txt"
- **No Credit (0 pts):** Copy not created, wrong location, incorrect content, or original file removed

### Step 21: Rename logo.txt in temp (1 point)
- **Full Credit (1 pt):** File "project_root/src/components/temp/temp_logo.txt" exists with content "brand_image" AND file "project_root/src/components/temp/logo.txt" no longer exists
- **No Credit (0 pts):** Rename not completed, wrong name, or old file still exists

### Step 22: Create production directory (1 point)
- **Full Credit (1 pt):** Directory "project_root/production" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 23: Move theme.txt to production (1 point)
- **Full Credit (1 pt):** File "project_root/production/theme.txt" exists with content "visual_design" AND original file no longer exists at "project_root/assets/styles/theme.txt"
- **No Credit (0 pts):** File not moved, wrong location, incorrect content, or original file still exists

### Step 24: Create deployment.txt file (1 point)
- **Full Credit (1 pt):** File "project_root/production/deployment.txt" exists with content "ready_for_production"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 25: Create manifest.txt file (1 point)
- **Full Credit (1 pt):** File "project_root/manifest.txt" exists with content "project_structure_complete"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

## Scoring Summary

- **Perfect Score:** 25/25 points
- **Good Performance:** 20-24 points (80-96%)
- **Acceptable Performance:** 15-19 points (60-76%)
- **Needs Improvement:** Below 15 points (<60%)

## Common Deduction Scenarios

1. **Incorrect file paths:** Deduct full point for each misplaced file/directory
2. **Missing content:** Deduct full point for files with incorrect or missing content
3. **Failed operations:** Deduct full point for incomplete moves/copies
4. **Wrong naming:** Deduct full point for files/directories with incorrect names
5. **Dependency failures:** If a step fails due to missing prerequisite, deduct point for failed step only

## Validation Commands

To verify completion:
```bash
find project_root -type f -exec echo "File: {}" \; -exec cat {} \;
find project_root -type d -exec echo "Directory: {}" \;
```

Expected final count:
- Directories: 11 total (including project_root)
- Files: 9 total
- Empty directories: 2 (utils, styles)