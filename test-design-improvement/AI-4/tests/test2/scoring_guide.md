# Test 2: Scoring Guide

**Total Points: 7 (1 point per step)**

## Scoring Criteria

### Step 1 (1 point)
- **1 point**: File "notes_A.txt" is created with exact content "Hello World"
- **0 points**: File not created, wrong name, wrong content, or created in wrong location

### Step 2 (1 point)
- **1 point**: File "notes_B.txt" is created with exact content "Testing 123"
- **0 points**: File not created, wrong name, wrong content, or created in wrong location

### Step 3 (1 point)
- **1 point**: File "config.json" is created with exact content '{"name": "test", "value": 42}'
- **0 points**: File not created, wrong name, wrong content, or created in wrong location

### Step 4 (1 point)
- **1 point**: AI successfully reads and displays/outputs the content "Hello World" from notes_A.txt
- **0 points**: AI fails to read the file or displays incorrect content

### Step 5 (1 point)
- **1 point**: AI successfully reads and displays/outputs the content '{"name": "test", "value": 42}' from config.json
- **0 points**: AI fails to read the file or displays incorrect content

### Step 6 (1 point)
- **1 point**: File "summary.md" is created with exact content "# Project Summary"
- **0 points**: File not created, wrong name, wrong content, or created in wrong location

### Step 7 (1 point)
- **1 point**: File "data_03.csv" is created with exact content "name,age,city"
- **0 points**: File not created, wrong name, wrong content, or created in wrong location

## Scoring Notes
- Each step is scored independently
- Partial credit is not awarded for individual steps
- File names and content must match exactly (case-sensitive)
- All files must be created in the current working directory
- For read operations (Steps 4-5), the AI must demonstrate successful reading by displaying the content