# Test 2: Expected Results

## File Contents

### Source Data
- **numbers.txt**: 
  ```
  15
  23
  7
  89
  34
  ```

### Calculation Results
- **calc1.txt**: 45 (15 × 3)
- **calc2.txt**: 40 (23 + 17)
- **calc3.txt**: 49 (7²)
- **calc4.txt**: 64 (89 - 25)
- **calc5.txt**: 17 (34 ÷ 2)

### Summary Files
- **summary.txt**: "Calculations completed for 5 numbers"
- **total.txt**: 215 (45 + 40 + 49 + 64 + 17)
- **check.txt**: Should contain original numbers and their corresponding results

## Expected Directory Structure
```
test2/
├── numbers.txt
├── calc1.txt
├── calc2.txt
├── calc3.txt
├── calc4.txt
├── calc5.txt
├── summary.txt
├── total.txt
└── check.txt
```

## Mathematical Verification
- Total should equal 215
- Each calculation should be mathematically correct
- All individual results properly saved