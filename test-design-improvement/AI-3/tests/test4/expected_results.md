# Test 4: Expected Results

## Step-by-step Expected Outcomes:

1. **Create config.txt**: File "config.txt" exists in current directory
2. **Write to config.txt**: File contains exactly "server_port=8080"
3. **Create log.txt**: File "log.txt" exists in current directory
4. **Write to log.txt**: File contains exactly "Application started"
5. **Append to log.txt**: File now contains "Application started" + newline + "Server listening on port 8080"
6. **Create users.txt**: File "users.txt" exists in current directory
7. **Write to users.txt**: File contains exactly "admin:password123"
8. **Append to users.txt**: File now contains "admin:password123" + newline + "guest:guest123"
9. **Create summary.txt**: File "summary.txt" exists in current directory
10. **Write to summary.txt**: File contains exactly "Total users: 2"

## Final File Contents:
- **config.txt**: "server_port=8080"
- **log.txt**: "Application started\nServer listening on port 8080"
- **users.txt**: "admin:password123\nguest:guest123"
- **summary.txt**: "Total users: 2"
- Total files: 4

## Key Requirements:
- Append operations must preserve existing content
- Each append adds content on a new line
- No extra whitespace or formatting