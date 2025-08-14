# Test 2: Expected Results

## Step-by-step Expected Outcomes:

1. **Create document_v1.txt**: File "document_v1.txt" exists in current directory
2. **Write to document_v1.txt**: File contains exactly "Initial draft content"
3. **Create backup_file.txt**: File "backup_file.txt" exists in current directory
4. **Copy content**: backup_file.txt contains exactly "Initial draft content"
5. **Rename document_v1.txt**: File is now named "document_v2.txt", original name no longer exists
6. **Create notes.txt**: File "notes.txt" exists in current directory
7. **Write to notes.txt**: File contains exactly "Version 2 notes: Updated formatting"
8. **Rename backup_file.txt**: File is now named "document_v1_backup.txt", original name no longer exists
9. **Create changelog.txt**: File "changelog.txt" exists in current directory
10. **Write to changelog.txt**: File contains exactly "v1 -> v2: Renamed and backed up original file"

## Final State:
- document_v2.txt (contains: "Initial draft content")
- document_v1_backup.txt (contains: "Initial draft content")
- notes.txt (contains: "Version 2 notes: Updated formatting")
- changelog.txt (contains: "v1 -> v2: Renamed and backed up original file")
- Total files: 4