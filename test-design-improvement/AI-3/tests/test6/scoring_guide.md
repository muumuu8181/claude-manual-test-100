# Test 6: Scoring Guide

## Scoring Criteria
- **Total Points**: 20 points (1 point per step)
- **Passing Score**: 14/20 points (70%)
- **No Partial Credit**: Each step is either complete (1 point) or incomplete (0 points)

## Step-by-step Scoring:

1. **[1 point]** Directory "pipeline" created
2. **[1 point]** File "raw_data.txt" created in pipeline
3. **[1 point]** Content "raw,input,data,batch1" written to raw_data.txt
4. **[1 point]** Directory "processed" created in pipeline
5. **[1 point]** File "cleaned_data.txt" created in processed
6. **[1 point]** Content copied from raw_data.txt to cleaned_data.txt
7. **[1 point]** File "validation.txt" created in pipeline
8. **[1 point]** Content "Validation started" written to validation.txt
9. **[1 point]** "Data format: CSV" appended to validation.txt
10. **[1 point]** "Records found: 1" appended to validation.txt
11. **[1 point]** Directory "output" created in pipeline
12. **[1 point]** File "final_data.txt" created in output
13. **[1 point]** Content copied from cleaned_data.txt to final_data.txt
14. **[1 point]** ",validated" appended to final_data.txt
15. **[1 point]** File "report.txt" created in pipeline
16. **[1 point]** Content "Processing report:" written to report.txt
17. **[1 point]** "Input: raw_data.txt" appended to report.txt
18. **[1 point]** "Output: final_data.txt" appended to report.txt
19. **[1 point]** "Status: Complete" appended to report.txt
20. **[1 point]** File "metadata.txt" created with correct content

## Critical Verification:
- [ ] All directories created in correct hierarchy
- [ ] Data flow integrity (raw -> cleaned -> final)
- [ ] Append operations preserve existing content
- [ ] Final data includes validation marker
- [ ] All file contents match exactly