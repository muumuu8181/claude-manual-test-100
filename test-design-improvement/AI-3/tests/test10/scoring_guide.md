# Test 10: Scoring Guide

## Scoring Criteria
- **Total Points**: 40 points (1 point per step)
- **Passing Score**: 28/40 points (70%)
- **No Partial Credit**: Each step is either complete (1 point) or incomplete (0 points)

## Step-by-step Scoring:

**Infrastructure Setup (Steps 1-5)**: 5 points
1-5. **[5 points]** All required directories created

**Source Data Creation (Steps 6-13)**: 8 points
6-9. **[4 points]** Customers source file created and populated
10-13. **[4 points]** Products source file created and populated

**Migration Logging (Steps 14-16, 23, 28, 35)**: 6 points
14-16. **[3 points]** Initial log setup
23. **[1 point]** Staging completion logged
28. **[1 point]** Processing completion logged
35. **[1 point]** Archive completion logged

**Staging Phase (Steps 17-22)**: 6 points
17-19. **[3 points]** Customers staging with new record
20-22. **[3 points]** Products staging with new record

**Processing Phase (Steps 24-27)**: 4 points
24-25. **[2 points]** Customers processed file
26-27. **[2 points]** Products processed file

**Archive Phase (Steps 29-34)**: 6 points
29-31. **[3 points]** Customers archive with timestamp
32-34. **[3 points]** Products archive with timestamp

**Summary Report (Steps 36-40)**: 5 points
36-40. **[5 points]** Migration summary with statistics

## Critical Verification:
- [ ] Data flows correctly through all pipeline stages
- [ ] Record counts increase correctly (2’3 in staging)
- [ ] Archive preserves original data + metadata
- [ ] Log tracks all major milestones
- [ ] Summary provides accurate final statistics