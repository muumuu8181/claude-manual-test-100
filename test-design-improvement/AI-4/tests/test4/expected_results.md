# Test 4: Expected Results

## Step 1: Create folder "project_alpha"
- Expected: A directory named "project_alpha" exists in the current working directory
- Verification: Directory listing should show "project_alpha/"

## Step 2: Create folder "project_beta"
- Expected: A directory named "project_beta" exists in the current working directory
- Verification: Directory listing should show "project_beta/"

## Step 3: Create "readme_v1.md" with content
- Expected: File "readme_v1.md" is created with content "# Alpha Project"
- Verification: File exists and contains exactly "# Alpha Project"

## Step 4: Create "readme_v2.md" with content
- Expected: File "readme_v2.md" is created with content "# Beta Project"
- Verification: File exists and contains exactly "# Beta Project"

## Step 5: Create file "config_prod.json"
- Expected: An empty file named "config_prod.json" exists in the current working directory
- Verification: File listing should show "config_prod.json"

## Step 6: Move "readme_v1.md" into "project_alpha"
- Expected: File "readme_v1.md" no longer exists in root directory but exists in "project_alpha/"
- Verification: Root directory should not contain "readme_v1.md", but "project_alpha/readme_v1.md" should exist

## Step 7: Move "readme_v2.md" into "project_beta"
- Expected: File "readme_v2.md" no longer exists in root directory but exists in "project_beta/"
- Verification: Root directory should not contain "readme_v2.md", but "project_beta/readme_v2.md" should exist

## Step 8: Rename "config_prod.json" to "settings_final.json"
- Expected: File "config_prod.json" no longer exists and "settings_final.json" now exists
- Verification: Root directory should show "settings_final.json" and not show "config_prod.json"

## Step 9: Create "log_data.txt" with content
- Expected: File "log_data.txt" is created with content "System startup complete"
- Verification: File exists and contains exactly "System startup complete"

## Step 10: Create folder "output_results"
- Expected: A directory named "output_results" exists in the current working directory
- Verification: Directory listing should show "output_results/"

## Final State
After all steps, the directory structure should be:
```
current_directory/
├── project_alpha/
│   └── readme_v1.md (contains "# Alpha Project")
├── project_beta/
│   └── readme_v2.md (contains "# Beta Project")
├── output_results/
├── settings_final.json (empty file)
└── log_data.txt (contains "System startup complete")
```