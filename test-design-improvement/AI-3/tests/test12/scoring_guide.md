# Test 12: Scoring Guide

## Scoring Criteria
- **Total Points**: 40 points (1 point per step)
- **Passing Score**: 28/40 points (70%)
- **No Partial Credit**: Each step is either complete (1 point) or incomplete (0 points)

## Step-by-step Scoring:

**Infrastructure (Steps 1-5, 20)**: 6 points
1-5. **[5 points]** All department directories created
20. **[1 point]** Reports directory created

**Warehouse Data (Steps 6-10)**: 5 points
6-10. **[5 points]** Stock levels file created and populated

**Sales Data (Steps 11-15)**: 5 points
11-15. **[5 points]** Pending orders file created and populated

**Purchasing Data (Steps 16-19)**: 4 points
16-19. **[4 points]** Procurement requests created and populated

**Stock Allocation Report (Steps 21-28)**: 8 points
21-23. **[3 points]** Report created with warehouse data copy
24-28. **[5 points]** Allocation calculations added

**Reorder Analysis (Steps 29-34)**: 6 points
29-34. **[6 points]** Reorder analysis with threshold comparisons

**Master Dashboard (Steps 35-40)**: 6 points
35-40. **[6 points]** Master inventory with cross-department summary

## Critical Business Logic Verification:
- [ ] Stock allocation calculations correct (stock - orders = available)
- [ ] Reorder analysis applies thresholds correctly
- [ ] Master dashboard counts match department data
- [ ] Cross-departmental data integration works
- [ ] All mathematical calculations accurate
- [ ] Business rules properly implemented