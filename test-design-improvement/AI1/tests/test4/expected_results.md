# Test 4: Expected Results

## Final Directory Structure
```
test4/
├── info.txt (copy of readme.txt)
├── inventory.txt (file listing)
├── organization_complete.txt (final report)
├── documents/
│   ├── readme.txt ("Document storage area")
│   ├── system.log ("Temporary log file" - moved and renamed)
│   └── archived/
├── images/
│   ├── photo1.jpg ("Image file 1")
│   └── archived/
└── data/
    ├── dataset.csv ("name,age,city")
    └── archived/
```

## File Contents
- **documents/readme.txt**: "Document storage area"
- **images/photo1.jpg**: "Image file 1"  
- **data/dataset.csv**: "name,age,city"
- **documents/system.log**: "Temporary log file" (moved from temp.log)
- **info.txt**: "Document storage area" (copy of readme.txt)
- **inventory.txt**: Complete listing of all files and their locations
- **organization_complete.txt**: Report confirming directory structure is complete

## Expected Operations
1. Three main directories created
2. Initial files created in correct locations
3. temp.log successfully moved and renamed to system.log
4. readme.txt successfully copied to info.txt
5. Inventory file contains accurate file listing
6. Archived subdirectories created in all three main directories
7. Final report confirms completion

## Verification Points
- All files in correct locations
- File contents match specifications
- Move and copy operations completed successfully
- All subdirectories created as required