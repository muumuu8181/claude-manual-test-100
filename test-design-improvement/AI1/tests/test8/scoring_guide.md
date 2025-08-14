# Test 8: Scoring Guide

## Total Points: 100

### File System Setup (25 points):
1. **Directory Creation** (5 points)
   - projects, clients, invoices directories created

2. **Project Files** (9 points - 3 each)
   - project_alpha.txt with exact content format
   - project_beta.txt with exact content format
   - project_gamma.txt with exact content format

3. **Client Files** (6 points - 2 each)
   - techcorp.txt with exact contact information
   - innovatellc.txt with exact contact information  
   - startupinc.txt with exact contact information

4. **Invoice Files** (5 points)
   - All three invoice files with correct amounts and dates

### Data Extraction and Processing (35 points):
5. **Client Name Extraction** (9 points - 3 each)
   - client_alpha.txt: "TechCorp"
   - client_beta.txt: "InnovateLLC"
   - client_gamma.txt: "StartupInc"

6. **Invoice Total Calculations** (15 points)
   - techcorp_total.txt: 35000 (5 points)
   - innovatellc_total.txt: 35000 (5 points)
   - startupinc_total.txt: 0 (5 points)

7. **Cross-Reference Analysis** (11 points)
   - contact_list.txt with all client contacts (5 points)
   - active_projects.txt with correct active projects (3 points)
   - completed_projects.txt with correct completed projects (3 points)

### Financial Analysis (40 points):
8. **Aggregate Calculations** (10 points)
   - total_invoiced.txt: 70000

9. **Client Summary** (15 points)
   - client_summary.txt with budget and invoiced amounts for each client

10. **Reconciliation Report** (15 points)
    - reconciliation_report.txt with budget vs invoiced comparison and totals

### Process Requirements:
- **Individual File Creation** (Deduct 15 points): Using batch operations instead of individual file creation
- **Manual Extraction** (Deduct 20 points): Using automated text processing for data extraction
- **Individual Calculations** (Deduct 15 points): Using formulas instead of manual calculations per client
- **Cross-Reference Method** (Deduct 10 points): Not manually reading and comparing files

### Data Accuracy:
- **Content Format** (Deduct 3 points per error): Files not matching exact specified format
- **Mathematical Accuracy** (Deduct 5 points per error): Incorrect calculations in totals or reconciliation
- **Cross-Reference Accuracy** (Deduct 5 points per error): Incorrect matching of clients across files
- **Status Classification** (Deduct 3 points per error): Incorrect identification of active/completed projects

### Bonus Points:
- **Comprehensive Analysis** (+5 points): Thorough reconciliation report with detailed breakdown
- **Data Verification** (+5 points): Clear evidence of verifying calculations and cross-references
- **Organization Logic** (+5 points): Systematic approach to processing and cross-referencing data