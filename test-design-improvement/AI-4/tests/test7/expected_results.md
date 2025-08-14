# Test7 Expected Results

## Step-by-Step Expected Outcomes

**Step 1: Create file "original_file.txt"**
- Expected: File "original_file.txt" exists in current directory
- Verification: File can be listed and accessed

**Step 2: Create file "temp_data.txt"**
- Expected: File "temp_data.txt" exists in current directory
- Verification: File can be listed and accessed

**Step 3: Create file "backup_file.txt"**
- Expected: File "backup_file.txt" exists in current directory
- Verification: File can be listed and accessed

**Step 4: Rename "original_file.txt" to "renamed_file.txt"**
- Expected: File "renamed_file.txt" exists, "original_file.txt" no longer exists
- Note: File is now referenced as "renamed_file.txt" in future steps
- Verification: Only "renamed_file.txt" exists in current directory

**Step 5: Create directory "storage"**
- Expected: Directory "storage" exists and is accessible
- Verification: Directory can be navigated into

**Step 6: Move "renamed_file.txt" into "storage" directory**
- Expected: File "storage/renamed_file.txt" exists, no "renamed_file.txt" in root
- Dependency: Requires Steps 4 and 5 completion
- Verification: File exists in storage directory only

**Step 7: Create file "config.txt" inside "storage" directory**
- Expected: File "storage/config.txt" exists
- Dependency: Requires Step 5 completion
- Verification: File exists in storage directory

**Step 8: Rename "temp_data.txt" to "processed_data.txt"**
- Expected: File "processed_data.txt" exists, "temp_data.txt" no longer exists
- Note: File is now referenced as "processed_data.txt" in future steps
- Verification: Only "processed_data.txt" exists in current directory

**Step 9: Create directory "archive"**
- Expected: Directory "archive" exists and is accessible
- Verification: Directory can be navigated into

**Step 10: Move "backup_file.txt" into "archive" directory**
- Expected: File "archive/backup_file.txt" exists, no "backup_file.txt" in root
- Dependency: Requires Steps 3 and 9 completion
- Verification: File exists in archive directory only

**Step 11: Rename "backup_file.txt" in archive to "old_backup.txt"**
- Expected: File "archive/old_backup.txt" exists, no "archive/backup_file.txt"
- Dependency: Requires Step 10 completion
- Note: File is now referenced as "old_backup.txt"
- Verification: Only "old_backup.txt" exists in archive directory

**Step 12: Create file "index.txt" inside "archive" directory**
- Expected: File "archive/index.txt" exists
- Dependency: Requires Step 9 completion
- Verification: File exists in archive directory

**Step 13: Move "processed_data.txt" into "storage" directory**
- Expected: File "storage/processed_data.txt" exists, no "processed_data.txt" in root
- Dependency: Requires Steps 8 and 5 completion
- Verification: File exists in storage directory only

**Step 14: Rename "processed_data.txt" in storage to "final_data.txt"**
- Expected: File "storage/final_data.txt" exists, no "storage/processed_data.txt"
- Dependency: Requires Step 13 completion
- Note: File is now referenced as "final_data.txt"
- Verification: Only "final_data.txt" exists in storage directory

**Step 15: Create file "log.txt" inside "storage" directory**
- Expected: File "storage/log.txt" exists
- Dependency: Requires Step 5 completion
- Verification: File exists in storage directory

**Step 16: Create directory "completed" inside "storage" directory**
- Expected: Directory "storage/completed" exists and is accessible
- Dependency: Requires Step 5 completion
- Verification: Directory can be navigated into

**Step 17: Move "final_data.txt" from storage to "storage/completed"**
- Expected: File "storage/completed/final_data.txt" exists, no "storage/final_data.txt"
- Dependency: Requires Steps 14 and 16 completion
- Verification: File exists in completed subdirectory only

**Step 18: Rename "final_data.txt" in "storage/completed" to "archived_data.txt"**
- Expected: File "storage/completed/archived_data.txt" exists, no "storage/completed/final_data.txt"
- Dependency: Requires Step 17 completion
- Verification: Only "archived_data.txt" exists in completed subdirectory

## Final Directory Structure

```
├── storage/
│   ├── renamed_file.txt
│   ├── config.txt
│   ├── log.txt
│   └── completed/
│       └── archived_data.txt
└── archive/
    ├── old_backup.txt
    └── index.txt
```

## Name Evolution Tracking

1. **original_file.txt** → renamed_file.txt (Step 4) → storage/renamed_file.txt (Step 6)
2. **temp_data.txt** → processed_data.txt (Step 8) → storage/processed_data.txt (Step 13) → storage/final_data.txt (Step 14) → storage/completed/final_data.txt (Step 17) → storage/completed/archived_data.txt (Step 18)
3. **backup_file.txt** → archive/backup_file.txt (Step 10) → archive/old_backup.txt (Step 11)

## Total Expected Items
- **Directories created:** 3 (storage, archive, storage/completed)
- **Files in final locations:** 6 (renamed_file.txt, config.txt, log.txt, archived_data.txt, old_backup.txt, index.txt)
- **Rename operations:** 4 total rename operations
- **Move operations:** 4 total move operations