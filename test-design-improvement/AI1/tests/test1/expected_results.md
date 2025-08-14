# Test 1: Expected Results

## Directory Structure
After completion, the following structure should exist:

```
test1/
├── workspace/
│   ├── data.txt (content: "Initial data")
│   ├── config.json (content: {"version": 1, "active": true}, read: true)
│   ├── file_list.txt (containing list of files in workspace)
│   └── archive/
│       └── data_backup.txt (content: "Initial data")
```

## File Contents
- **data.txt**: "Initial data"
- **data_backup.txt**: "Initial data" (copy of data.txt)
- **config.json**: {"version": 1, "active": true}, read: true
- **file_list.txt**: Should contain listing of workspace directory files

## Expected Behaviors
- All 8 steps completed in sequence
- Files created in correct locations
- Content matches specifications
- Backup file successfully moved to archive directory
- Directory listing captured in file_list.txt