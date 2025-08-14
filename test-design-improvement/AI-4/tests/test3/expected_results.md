# Test 3: Expected Results

## Step 1: Create folder "temp_folder"
- Expected: A directory named "temp_folder" exists in the current working directory
- Verification: Directory listing should show "temp_folder/"

## Step 2: Create folder "backup_dir"
- Expected: A directory named "backup_dir" exists in the current working directory
- Verification: Directory listing should show "backup_dir/"

## Step 3: Create file "document_X.txt"
- Expected: An empty file named "document_X.txt" exists in the current working directory
- Verification: File listing should show "document_X.txt"

## Step 4: Create file "document_Y.txt"
- Expected: An empty file named "document_Y.txt" exists in the current working directory
- Verification: File listing should show "document_Y.txt"

## Step 5: Rename "temp_folder" to "main_folder"
- Expected: The directory "temp_folder" no longer exists and "main_folder" now exists
- Verification: Directory listing should show "main_folder/" and not show "temp_folder/"

## Step 6: Rename "backup_dir" to "archive_storage"
- Expected: The directory "backup_dir" no longer exists and "archive_storage" now exists
- Verification: Directory listing should show "archive_storage/" and not show "backup_dir/"

## Step 7: Move "document_X.txt" into "main_folder"
- Expected: File "document_X.txt" no longer exists in root directory but exists in "main_folder/"
- Verification: Root directory should not contain "document_X.txt", but "main_folder/document_X.txt" should exist

## Step 8: Move "document_Y.txt" into "archive_storage"
- Expected: File "document_Y.txt" no longer exists in root directory but exists in "archive_storage/"
- Verification: Root directory should not contain "document_Y.txt", but "archive_storage/document_Y.txt" should exist

## Final State
After all steps, the directory structure should be:
```
current_directory/
├── main_folder/
│   └── document_X.txt
└── archive_storage/
    └── document_Y.txt
```