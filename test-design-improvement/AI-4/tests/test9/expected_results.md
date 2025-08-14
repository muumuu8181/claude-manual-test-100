# Test 9: Expected Results

## Step-by-Step Expected Outcomes

**Step 1:** Directory "project_root" created successfully
- Expected: New empty directory at ./project_root/

**Step 2:** Directory "src" created inside project_root
- Expected: New empty directory at ./project_root/src/

**Step 3:** Directory "assets" created inside project_root
- Expected: New empty directory at ./project_root/assets/

**Step 4:** Directory "config" created inside project_root
- Expected: New empty directory at ./project_root/config/

**Step 5:** File "main.txt" created with specified content
- Expected: File at ./project_root/src/main.txt containing "application_entry"

**Step 6:** Directory "components" created inside src
- Expected: New empty directory at ./project_root/src/components/

**Step 7:** Directory "utils" created inside src
- Expected: New empty directory at ./project_root/src/utils/

**Step 8:** File "helper.txt" created with specified content
- Expected: File at ./project_root/src/utils/helper.txt containing "utility_functions"

**Step 9:** Directory "images" created inside assets
- Expected: New empty directory at ./project_root/assets/images/

**Step 10:** Directory "styles" created inside assets
- Expected: New empty directory at ./project_root/assets/styles/

**Step 11:** File "logo.txt" created with specified content
- Expected: File at ./project_root/assets/images/logo.txt containing "brand_image"

**Step 12:** File "theme.txt" created with specified content
- Expected: File at ./project_root/assets/styles/theme.txt containing "visual_design"

**Step 13:** File "settings.txt" created with specified content
- Expected: File at ./project_root/config/settings.txt containing "app_configuration"

**Step 14:** Directory "backup" created inside project_root
- Expected: New empty directory at ./project_root/backup/

**Step 15:** File copied and renamed successfully
- Expected: File at ./project_root/backup/main_backup.txt containing "application_entry"
- Original file at ./project_root/src/main.txt remains unchanged

**Step 16:** Directory "archive" created inside backup
- Expected: New empty directory at ./project_root/backup/archive/

**Step 17:** File moved successfully from utils to archive
- Expected: File at ./project_root/backup/archive/helper.txt containing "utility_functions"
- Original file at ./project_root/src/utils/helper.txt no longer exists

**Step 18:** File "index.txt" created with specified content
- Expected: File at ./project_root/src/components/index.txt containing "component_list"

**Step 19:** Directory "temp" created inside components
- Expected: New empty directory at ./project_root/src/components/temp/

**Step 20:** File copied successfully from images to temp
- Expected: File at ./project_root/src/components/temp/logo.txt containing "brand_image"
- Original file at ./project_root/assets/images/logo.txt remains unchanged

**Step 21:** File renamed successfully in temp directory
- Expected: File at ./project_root/src/components/temp/temp_logo.txt containing "brand_image"
- File ./project_root/src/components/temp/logo.txt no longer exists

**Step 22:** Directory "production" created inside project_root
- Expected: New empty directory at ./project_root/production/

**Step 23:** File moved successfully from styles to production
- Expected: File at ./project_root/production/theme.txt containing "visual_design"
- Original file at ./project_root/assets/styles/theme.txt no longer exists

**Step 24:** File "deployment.txt" created with specified content
- Expected: File at ./project_root/production/deployment.txt containing "ready_for_production"

**Step 25:** File "manifest.txt" created with specified content
- Expected: File at ./project_root/manifest.txt containing "project_structure_complete"

## Final Directory Structure Verification

The completed test should result in the following exact structure:

```
project_root/
├── manifest.txt (content: "project_structure_complete")
├── src/
│   ├── main.txt (content: "application_entry")
│   ├── components/
│   │   ├── index.txt (content: "component_list")
│   │   └── temp/
│   │       └── temp_logo.txt (content: "brand_image")
│   └── utils/
│       [empty directory]
├── assets/
│   ├── images/
│   │   └── logo.txt (content: "brand_image")
│   └── styles/
│       [empty directory]
├── config/
│   └── settings.txt (content: "app_configuration")
├── backup/
│   ├── main_backup.txt (content: "application_entry")
│   └── archive/
│       └── helper.txt (content: "utility_functions")
└── production/
    ├── theme.txt (content: "visual_design")
    └── deployment.txt (content: "ready_for_production")
```

## Key Validation Points

1. All 7 directories should be present at the root level
2. File movements should be complete (source files removed, destination files present)
3. File copies should preserve originals
4. All file contents should match exactly as specified
5. Empty directories (utils, styles) should exist but contain no files
6. Total of 9 files should exist across all directories