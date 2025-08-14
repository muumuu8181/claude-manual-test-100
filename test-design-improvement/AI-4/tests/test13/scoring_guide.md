# Test 13: Scoring Guide

**Total Points: 50 (1 point per step)**

## Scoring Criteria

### Step 1: Create database_engine directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect name

### Step 2: Create tables directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/tables" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 3: Create indexes directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/indexes" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 4: Create transactions directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/transactions" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 5: Create initial db_config.json (1 point)
- **Full Credit (1 pt):** File exists with valid JSON containing all required fields with correct initial values
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or missing/incorrect fields

### Step 6: Create users.csv (1 point)
- **Full Credit (1 pt):** File exists with exact CSV content including header and 3 user records
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing/wrong data

### Step 7: Create products.csv (1 point)
- **Full Credit (1 pt):** File exists with exact CSV content including header and 4 product records
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing/wrong data

### Step 8: Create categories.csv (1 point)
- **Full Credit (1 pt):** File exists with exact CSV content including header and 2 category records
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing/wrong data

### Step 9: Update db_config.json after table initialization (1 point)
- **Full Credit (1 pt):** JSON updated with table_count: 3 and operations_log: ["tables_initialized"]
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 10: Create primary_keys directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/indexes/primary_keys" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 11: Create users_pk.idx (1 point)
- **Full Credit (1 pt):** File exists with correct index format containing exactly 3 user index entries
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing/wrong entries

### Step 12: Create products_pk.idx (1 point)
- **Full Credit (1 pt):** File exists with correct index format containing exactly 4 product index entries
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing/wrong entries

### Step 13: Create categories_pk.idx (1 point)
- **Full Credit (1 pt):** File exists with correct index format containing exactly 2 category index entries
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing/wrong entries

### Step 14: Update db_config.json with index creation (1 point)
- **Full Credit (1 pt):** JSON updated with index_count: 3 and "primary_indexes_created" added to operations_log
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 15: Create foreign_keys directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/indexes/foreign_keys" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 16: Create products_category_fk.idx (1 point)
- **Full Credit (1 pt):** File exists with correct foreign key index format containing exactly 4 valid entries
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing/wrong entries

### Step 17: Create orders directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/tables/orders" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 18: Create orders.csv (1 point)
- **Full Credit (1 pt):** File exists with exact CSV content including header and 3 order records
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing/wrong data

### Step 19: Create order_items.csv (1 point)
- **Full Credit (1 pt):** File exists with exact CSV content including header and 5 order item records
- **No Credit (0 pts):** File not created, wrong location, incorrect format, or missing/wrong data

### Step 20: Update db_config.json after order tables (1 point)
- **Full Credit (1 pt):** JSON updated with table_count: 5 and "order_tables_created" added to operations_log
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 21: Create transaction_001 directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/transactions/transaction_001" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 22: Create begin_transaction.log (1 point)
- **Full Credit (1 pt):** File exists with exact transaction begin log content
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 23: Create users_backup_001.csv (1 point)
- **Full Credit (1 pt):** File exists with identical content to current users.csv (3 users)
- **No Credit (0 pts):** Backup not created, wrong location, or content doesn't match

### Step 24: Append new user to users.csv (1 point)
- **Full Credit (1 pt):** users.csv now contains 4 users with diana as the last entry
- **No Credit (0 pts):** User not added, wrong format, or incorrect data

### Step 25: Create insert_user.log (1 point)
- **Full Credit (1 pt):** File exists with exact insert operation log content
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 26: Update users_pk.idx with new user (1 point)
- **Full Credit (1 pt):** Index updated with "user_id|4|users.csv:4" entry appended
- **No Credit (0 pts):** Index not updated or incorrect entry format

### Step 27: Create index_update.log (1 point)
- **Full Credit (1 pt):** File exists with exact index update log content
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 28: Update db_config.json with active transaction (1 point)
- **Full Credit (1 pt):** JSON updated with "001" in active_transactions and "transaction_001_started" in operations_log
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 29: Create queries directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/queries" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 30: Create query_001.sql (1 point)
- **Full Credit (1 pt):** File exists with exact SQL query for active users
- **No Credit (0 pts):** File not created, wrong location, or incorrect SQL

### Step 31: Create query_001_results.csv (1 point)
- **Full Credit (1 pt):** File exists with correct query results showing 3 active users (including diana)
- **No Credit (0 pts):** File not created, wrong location, incorrect results, or wrong format

### Step 32: Create query_002.sql (1 point)
- **Full Credit (1 pt):** File exists with exact SQL query for products join categories with price filter
- **No Credit (0 pts):** File not created, wrong location, or incorrect SQL

### Step 33: Create query_002_results.csv (1 point)
- **Full Credit (1 pt):** File exists with correct joined results showing 3 products over $100 with category names
- **No Credit (0 pts):** File not created, wrong location, incorrect join results, or wrong format

### Step 34: Create aggregations directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/queries/aggregations" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 35: Create total_orders_by_user.csv (1 point)
- **Full Credit (1 pt):** File exists with correct aggregation showing total amounts per user (user 1: 1209.96, user 2: 199.99)
- **No Credit (0 pts):** File not created, wrong location, incorrect calculations, or wrong format

### Step 36: Create product_sales_summary.csv (1 point)
- **Full Credit (1 pt):** File exists with correct aggregation showing total quantity sold per product
- **No Credit (0 pts):** File not created, wrong location, incorrect calculations, or wrong format

### Step 37: Update db_config.json after query operations (1 point)
- **Full Credit (1 pt):** JSON updated with "query_operations_completed" added to operations_log
- **No Credit (0 pts):** File not updated, invalid JSON, or missing entry

### Step 38: Create integrity_check directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/integrity_check" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 39: Create fk_integrity_report.txt (1 point)
- **Full Credit (1 pt):** File exists with foreign key integrity validation results for products-categories
- **No Credit (0 pts):** File not created, wrong location, or missing validation content

### Step 40: Create referential_integrity_report.txt (1 point)
- **Full Credit (1 pt):** File exists with referential integrity validation results for orders-users
- **No Credit (0 pts):** File not created, wrong location, or missing validation content

### Step 41: Create rollback_scenario directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/transactions/rollback_scenario" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 42: Create rollback_trigger.txt (1 point)
- **Full Credit (1 pt):** File exists with exact content "integrity_violation_detected"
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 43: Create rollback_001.log (1 point)
- **Full Credit (1 pt):** File exists with exact rollback log content
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

### Step 44: Restore users.csv from backup (1 point)
- **Full Credit (1 pt):** users.csv restored to original 3-user state, identical to backup content
- **No Credit (0 pts):** File not restored, incorrect content, or diana user still present

### Step 45: Restore users_pk.idx (1 point)
- **Full Credit (1 pt):** Index restored to original 3-entry state with user_id|4 entry removed
- **No Credit (0 pts):** Index not restored or user_id|4 entry still present

### Step 46: Update db_config.json after rollback (1 point)
- **Full Credit (1 pt):** JSON updated with "001" removed from active_transactions and "transaction_001_rolled_back" in operations_log
- **No Credit (0 pts):** File not updated, invalid JSON, or incorrect values

### Step 47: Create database_statistics directory (1 point)
- **Full Credit (1 pt):** Directory "database_engine/database_statistics" exists and is empty
- **No Credit (0 pts):** Directory not created or incorrect location/name

### Step 48: Create table_stats.json (1 point)
- **Full Credit (1 pt):** File exists with valid JSON containing accurate record counts for all tables
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect counts

### Step 49: Create system_health.json (1 point)
- **Full Credit (1 pt):** File exists with exact system health JSON content
- **No Credit (0 pts):** File not created, wrong location, invalid JSON, or incorrect content

### Step 50: Create database_session_log.txt (1 point)
- **Full Credit (1 pt):** File exists with exact database session completion log
- **No Credit (0 pts):** File not created, wrong location, or incorrect content

## Scoring Summary

- **Perfect Score:** 50/50 points (100%)
- **Excellent Performance:** 45-49 points (90-98%)
- **Good Performance:** 40-44 points (80-88%)
- **Acceptable Performance:** 30-39 points (60-78%)
- **Needs Improvement:** Below 30 points (<60%)

## Common Deduction Scenarios

1. **Transaction integrity failures:** Deduct full point for incorrect rollback implementation, backup/restore failures
2. **Data consistency errors:** Deduct full point for users.csv or index not properly restored after rollback
3. **Index synchronization failures:** Deduct full point if indexes don't match table data state
4. **Query execution errors:** Deduct full point for incorrect joins, aggregations, or filtering
5. **JSON validity:** Deduct full point for any syntactically invalid JSON files
6. **CSV format errors:** Deduct full point for incorrect CSV structure or data
7. **State tracking failures:** Deduct full point for incorrect operations_log tracking in db_config.json

## Critical Validation Points

1. **Transaction Lifecycle:** Complete transaction with proper begin, execute, and rollback phases
2. **Data Consistency:** users.csv must be restored to exactly 3 users after rollback
3. **Index Integrity:** users_pk.idx must be synchronized with users.csv at all times
4. **Referential Integrity:** All foreign key relationships must be valid and verified
5. **Query Accuracy:** Complex joins and aggregations must produce mathematically correct results
6. **State Persistence:** db_config.json must accurately track all database operations
7. **File Organization:** Proper directory structure with 13 directories and 22 files total
8. **Backup/Restore:** Transaction backup mechanism must successfully restore data
9. **Integrity Validation:** All integrity check reports must validate database consistency
10. **Statistics Accuracy:** Table stats must reflect actual record counts after rollback

## Validation Commands

To verify database simulation and transaction handling:
```bash
# Check transaction rollback success
wc -l database_engine/tables/users.csv  # Should show 4 lines (header + 3 users)
grep -c "user_id|" database_engine/indexes/primary_keys/users_pk.idx  # Should show 3

# Verify all JSON files are valid
find database_engine -name "*.json" -exec python -m json.tool {} \;

# Check final state consistency
cat database_engine/db_config.json | grep -E '"active_transactions"|"operations_log"'

# Verify query results accuracy
cat database_engine/queries/aggregations/total_orders_by_user.csv  # User 1 total: 1209.96
cat database_engine/queries/aggregations/product_sales_summary.csv  # Product 102 quantity: 3

# Check transaction logs
ls database_engine/transactions/transaction_001/  # Should have 4 files
ls database_engine/transactions/rollback_scenario/  # Should have 2 files
```

Expected final count:
- Directories: 13 total (1 empty: database_statistics initially)
- Files: 22 total
- JSON files: 4 (all must be syntactically valid)
- CSV files: 8 (all must have proper format and correct data)
- Log files: 6 (transaction and rollback logs)
- SQL files: 2 (query definitions)
- Index files: 4 (primary and foreign key indexes)
- Report files: 3 (integrity checks and session summary)