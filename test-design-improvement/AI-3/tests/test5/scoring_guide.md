# Test 5: Scoring Guide

## Scoring Criteria
- **Total Points**: 18 points (1 point per step)
- **Passing Score**: 13/18 points (72%)
- **No Partial Credit**: Each step is either complete (1 point) or incomplete (0 points)

## Step-by-step Scoring:

1. **[1 point]** Directory "workspace" created
2. **[1 point]** File "master_list.txt" created in workspace
3. **[1 point]** Content "File inventory:" written to master_list.txt
4. **[1 point]** Directory "archived" created in workspace
5. **[1 point]** File "old_data.txt" created in workspace/archived
6. **[1 point]** Content "Legacy information" written to old_data.txt
7. **[1 point]** "old_data.txt" appended to master_list.txt
8. **[1 point]** Directory "current" created in workspace
9. **[1 point]** File "active_data.txt" created in workspace/current
10. **[1 point]** Content "Current working data" written to active_data.txt
11. **[1 point]** "active_data.txt" appended to master_list.txt
12. **[1 point]** File "index.txt" created in workspace
13. **[1 point]** Content "Directories: archived, current" written to index.txt
14. **[1 point]** Content copied to "backup_inventory.txt" (matches master_list.txt at this step)
15. **[1 point]** "old_data.txt" renamed to "legacy_backup.txt" (original file gone)
16. **[1 point]** Update line appended to master_list.txt
17. **[1 point]** File "status.txt" created in workspace
18. **[1 point]** Content "Organization complete" written to status.txt

## Critical Verification Points:
- [ ] All directories exist in correct locations
- [ ] master_list.txt contains 4 lines total
- [ ] backup_inventory.txt contains 3 lines (pre-rename copy)
- [ ] File renamed successfully (old name gone, new name exists)
- [ ] Dependencies handled correctly (append operations work)
- [ ] All file contents match exactly