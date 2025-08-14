# Test5 Expected Results

## Step-by-Step Expected Outcomes

**Step 1: Create "projects" directory**
- Expected: Directory "projects" exists at current working location
- Verification: Directory can be navigated into and listed

**Step 2: Create "documents" directory inside "projects"**
- Expected: Directory "projects/documents" exists
- Dependency: Requires Step 1 completion
- Verification: Path "projects/documents" is accessible

**Step 3: Create "reports" directory inside "projects"**
- Expected: Directory "projects/reports" exists
- Dependency: Requires Step 1 completion
- Verification: Path "projects/reports" is accessible

**Step 4: Create "archive" directory inside "documents"**
- Expected: Directory "projects/documents/archive" exists
- Dependency: Requires Step 2 completion
- Verification: Path "projects/documents/archive" is accessible

**Step 5: Create "templates" directory inside "documents"**
- Expected: Directory "projects/documents/templates" exists
- Dependency: Requires Step 2 completion
- Verification: Path "projects/documents/templates" is accessible

**Step 6: Create "readme.txt" file inside "projects"**
- Expected: File "projects/readme.txt" exists
- Dependency: Requires Step 1 completion
- Verification: File can be read/listed

**Step 7: Create "project_list.txt" file inside "documents"**
- Expected: File "projects/documents/project_list.txt" exists
- Dependency: Requires Step 2 completion
- Verification: File can be read/listed

**Step 8: Create "monthly_report.txt" file inside "reports"**
- Expected: File "projects/reports/monthly_report.txt" exists
- Dependency: Requires Step 3 completion
- Verification: File can be read/listed

**Step 9: Create "old_data.txt" file inside "archive"**
- Expected: File "projects/documents/archive/old_data.txt" exists
- Dependency: Requires Step 4 completion
- Verification: File can be read/listed

**Step 10: Create "template_basic.txt" file inside "templates"**
- Expected: File "projects/documents/templates/template_basic.txt" exists
- Dependency: Requires Step 5 completion
- Verification: File can be read/listed

**Step 11: Create "summary.txt" file inside "reports"**
- Expected: File "projects/reports/summary.txt" exists
- Dependency: Requires Step 3 completion
- Verification: File can be read/listed

**Step 12: Create "backup_info.txt" file inside "archive"**
- Expected: File "projects/documents/archive/backup_info.txt" exists
- Dependency: Requires Step 4 completion
- Verification: File can be read/listed

## Final Structure Verification

The complete directory tree should match exactly:
```
projects/
├── readme.txt
├── documents/
│   ├── project_list.txt
│   ├── archive/
│   │   ├── old_data.txt
│   │   └── backup_info.txt
│   └── templates/
│       └── template_basic.txt
└── reports/
    ├── monthly_report.txt
    └── summary.txt
```

## Total Expected Files and Directories
- **Directories created:** 5 (projects, documents, reports, archive, templates)
- **Files created:** 7 (readme.txt, project_list.txt, monthly_report.txt, old_data.txt, template_basic.txt, summary.txt, backup_info.txt)