# Test 4: Scoring Guide

## Scoring Criteria
- **Total Points**: 10 points (1 point per step)
- **Passing Score**: 7/10 points (70%)
- **No Partial Credit**: Each step is either complete (1 point) or incomplete (0 points)

## Step-by-step Scoring:

1. **[1 point]** File "config.txt" created successfully
2. **[1 point]** Content "server_port=8080" written to config.txt
3. **[1 point]** File "log.txt" created successfully
4. **[1 point]** Content "Application started" written to log.txt
5. **[1 point]** Content "Server listening on port 8080" appended to log.txt (both lines present)
6. **[1 point]** File "users.txt" created successfully
7. **[1 point]** Content "admin:password123" written to users.txt
8. **[1 point]** Content "guest:guest123" appended to users.txt (both lines present)
9. **[1 point]** File "summary.txt" created successfully
10. **[1 point]** Content "Total users: 2" written to summary.txt

## Verification Checklist:
- [ ] All 4 files exist with correct names
- [ ] config.txt contains exactly "server_port=8080"
- [ ] log.txt contains both lines in correct order
- [ ] users.txt contains both user entries in correct order
- [ ] summary.txt contains exactly "Total users: 2"
- [ ] Append operations preserved existing content