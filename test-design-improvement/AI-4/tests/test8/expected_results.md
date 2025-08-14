# Test8 Expected Results

## Step-by-Step Expected Outcomes

**Step 1: Create directory "workspace"**
- Expected: Directory "workspace" exists and is accessible
- Verification: Directory can be navigated into

**Step 2: Create file "input.txt" with content "start"**
- Expected: File "input.txt" exists with exact content "start"
- Verification: File exists and reading returns "start"

**Step 3: Create file "config.json" inside workspace directory**
- Expected: File "workspace/config.json" exists
- Dependency: Requires Step 1 completion
- Verification: File exists in workspace directory

**Step 4: Read input.txt content and create "start_process.txt"**
- Expected: File "start_process.txt" exists (uses "start" from input.txt)
- Dependency: Requires Step 2 completion and reading input.txt
- Verification: File exists with correct name derived from input.txt content

**Step 5: Create directory "temp" inside workspace directory**
- Expected: Directory "workspace/temp" exists and is accessible
- Dependency: Requires Step 1 completion
- Verification: Directory path "workspace/temp" is accessible

**Step 6: Move "start_process.txt" into "workspace/temp" directory**
- Expected: File "workspace/temp/start_process.txt" exists, no "start_process.txt" in root
- Dependency: Requires Steps 4 and 5 completion
- Verification: File exists only in temp subdirectory

**Step 7: Check for "missing_file.txt" and create "error_log.txt"**
- Expected: File "error_log.txt" exists with content "file_not_found" (since missing_file.txt doesn't exist)
- Conditional: Creates file because missing_file.txt should not exist
- Verification: File exists with correct content

**Step 8: Create file "data.txt" with content "processing"**
- Expected: File "data.txt" exists with exact content "processing"
- Verification: File exists and reading returns "processing"

**Step 9: Read data.txt content and create "processing_dir" directory**
- Expected: Directory "processing_dir" exists (uses "processing" from data.txt)
- Dependency: Requires Step 8 completion and reading data.txt
- Verification: Directory exists with name derived from data.txt content

**Step 10: Create file "status.txt" inside processing_dir directory**
- Expected: File "processing_dir/status.txt" exists
- Dependency: Requires Step 9 completion
- Verification: File exists in processing_dir directory

**Step 11: Rename "config.json" in workspace to "settings.json"**
- Expected: File "workspace/settings.json" exists, no "workspace/config.json"
- Dependency: Requires Step 3 completion
- Verification: Only settings.json exists in workspace directory

**Step 12: Copy "error_log.txt" into workspace directory**
- Expected: File "workspace/error_log.txt" exists (copy of original error_log.txt)
- Dependency: Requires Steps 1 and 7 completion
- Conditional: Only executes if error_log.txt exists (should exist from Step 7)
- Verification: File exists in both root and workspace directories

**Step 13: Create file "output.txt" with content "complete"**
- Expected: File "output.txt" exists with exact content "complete"
- Verification: File exists and reading returns "complete"

**Step 14: Check if workspace/settings.json exists and create "validation_passed.txt"**
- Expected: File "validation_passed.txt" exists
- Dependency: Requires Step 11 completion
- Conditional: Creates file because settings.json should exist from Step 11
- Verification: File exists

**Step 15: Move "data.txt" into processing_dir directory**
- Expected: File "processing_dir/data.txt" exists, no "data.txt" in root
- Dependency: Requires Steps 8 and 9 completion
- Verification: File exists only in processing_dir directory

**Step 16: Rename "data.txt" in processing_dir to "processed_data.txt"**
- Expected: File "processing_dir/processed_data.txt" exists, no "processing_dir/data.txt"
- Dependency: Requires Step 15 completion
- Verification: Only processed_data.txt exists in processing_dir

**Step 17: Create directory "results" inside workspace directory**
- Expected: Directory "workspace/results" exists and is accessible
- Dependency: Requires Step 1 completion
- Verification: Directory path "workspace/results" is accessible

**Step 18: Move "output.txt" into workspace/results directory**
- Expected: File "workspace/results/output.txt" exists, no "output.txt" in root
- Dependency: Requires Steps 13 and 17 completion
- Verification: File exists only in results subdirectory

**Step 19: Read output.txt in results and create "complete_summary.txt" in same directory**
- Expected: File "workspace/results/complete_summary.txt" exists
- Dependency: Requires Step 18 completion and reading output.txt content
- Verification: File exists with name derived from output.txt content ("complete")

**Step 20: Create "final_report.txt" in workspace with content "test_finished"**
- Expected: File "workspace/final_report.txt" exists with content "test_finished"
- Dependency: Requires Step 1 completion
- Verification: File exists with correct content

## Final Directory Structure

```
├── workspace/
│   ├── settings.json
│   ├── error_log.txt (content: "file_not_found")
│   ├── validation_passed.txt
│   ├── final_report.txt (content: "test_finished")
│   ├── temp/
│   │   └── start_process.txt
│   └── results/
│       ├── output.txt (content: "complete")
│       └── complete_summary.txt
├── processing_dir/
│   ├── status.txt
│   └── processed_data.txt (content: "processing")
├── input.txt (content: "start")
├── error_log.txt (content: "file_not_found")
└── validation_passed.txt
```

## Conditional Operations Results

**Step 7 Condition:** missing_file.txt does NOT exist → error_log.txt IS created
**Step 12 Condition:** error_log.txt exists (from Step 7) → copy IS executed
**Step 14 Condition:** workspace/settings.json exists (from Step 11) → validation_passed.txt IS created

## Total Expected Items
- **Directories created:** 4 (workspace, workspace/temp, processing_dir, workspace/results)
- **Files with specific content:** 4 (input.txt, error_log.txt, output.txt, final_report.txt)
- **Files created from content:** 3 (start_process.txt, processing_dir, complete_summary.txt)
- **Other files:** 4 (settings.json, status.txt, processed_data.txt, validation_passed.txt)
- **Move operations:** 3
- **Rename operations:** 2
- **Conditional operations:** 3 (all should execute successfully)