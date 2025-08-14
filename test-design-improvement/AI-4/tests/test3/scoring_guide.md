# Test 3: Scoring Guide

**Total Points: 8 (1 point per step)**

## Scoring Criteria

### Step 1 (1 point)
- **1 point**: Folder "temp_folder" is created successfully in the current working directory
- **0 points**: Folder not created, wrong name, or created in wrong location

### Step 2 (1 point)
- **1 point**: Folder "backup_dir" is created successfully in the current working directory
- **0 points**: Folder not created, wrong name, or created in wrong location

### Step 3 (1 point)
- **1 point**: File "document_X.txt" is created successfully in the current working directory
- **0 points**: File not created, wrong name, or created in wrong location

### Step 4 (1 point)
- **1 point**: File "document_Y.txt" is created successfully in the current working directory
- **0 points**: File not created, wrong name, or created in wrong location

### Step 5 (1 point)
- **1 point**: Folder "temp_folder" is successfully renamed to "main_folder" (original folder no longer exists, new folder exists)
- **0 points**: Original folder still exists, new folder doesn't exist, or wrong name used

### Step 6 (1 point)
- **1 point**: Folder "backup_dir" is successfully renamed to "archive_storage" (original folder no longer exists, new folder exists)
- **0 points**: Original folder still exists, new folder doesn't exist, or wrong name used

### Step 7 (1 point)
- **1 point**: File "document_X.txt" is successfully moved from root directory to "main_folder" directory
- **0 points**: File still exists in root, file doesn't exist in target folder, or file was copied instead of moved

### Step 8 (1 point)
- **1 point**: File "document_Y.txt" is successfully moved from root directory to "archive_storage" directory
- **0 points**: File still exists in root, file doesn't exist in target folder, or file was copied instead of moved

## Scoring Notes
- Each step is scored independently
- Partial credit is not awarded for individual steps
- File/folder names must match exactly (case-sensitive)
- For rename operations, the original item must no longer exist
- For move operations, the file must exist only in the target location (not copied)
- All operations must maintain the correct directory structure