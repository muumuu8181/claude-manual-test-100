# Test 6: Expected Results

## Source Files
- **input_list.txt**: Alice, Bob, Charlie, Diana, Eve, Frank

## Individual Employee Files
- **alice.txt**: "Name: Alice, ID: 001, Department: Sales"
- **bob.txt**: "Name: Bob, ID: 002, Department: Engineering"
- **charlie.txt**: "Name: Charlie, ID: 003, Department: Marketing"
- **diana.txt**: "Name: Diana, ID: 004, Department: HR"
- **eve.txt**: "Name: Eve, ID: 005, Department: Finance"
- **frank.txt**: "Name: Frank, ID: 006, Department: Operations"

## Department Extraction Files
- **dept_alice.txt**: "Sales"
- **dept_bob.txt**: "Engineering"
- **dept_charlie.txt**: "Marketing"
- **dept_diana.txt**: "HR"
- **dept_eve.txt**: "Finance"
- **dept_frank.txt**: "Operations"

## Analysis Files
- **departments.txt**: 
  ```
  Sales
  Engineering
  Marketing
  HR
  Finance
  Operations
  ```

- **dept_count.txt**:
  ```
  Sales: 1
  Engineering: 1
  Marketing: 1
  HR: 1
  Finance: 1
  Operations: 1
  ```

- **employee_roster.txt** (ordered by ID):
  ```
  Alice, ID: 001
  Bob, ID: 002
  Charlie, ID: 003
  Diana, ID: 004
  Eve, ID: 005
  Frank, ID: 006
  ```

- **validation_report.txt**: Report confirming all 6 employee files exist with correct content

## Directory Structure
```
test6/
├── input_list.txt
├── alice.txt
├── bob.txt
├── charlie.txt
├── diana.txt
├── eve.txt
├── frank.txt
├── dept_alice.txt
├── dept_bob.txt
├── dept_charlie.txt
├── dept_diana.txt
├── dept_eve.txt
├── dept_frank.txt
├── departments.txt
├── dept_count.txt
├── employee_roster.txt
└── validation_report.txt
```

## Verification Points
- All employee files contain exact formatted content
- Department extraction is accurate
- All departments listed without duplicates
- Employee roster ordered by ID correctly
- Validation confirms all files exist