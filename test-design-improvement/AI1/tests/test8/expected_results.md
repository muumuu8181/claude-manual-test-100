# Test 8: Expected Results

## Directory Structure with Files

### Projects Directory
- **project_alpha.txt**: "Client: TechCorp, Budget: 50000, Status: Active"
- **project_beta.txt**: "Client: InnovateLLC, Budget: 35000, Status: Completed"
- **project_gamma.txt**: "Client: StartupInc, Budget: 25000, Status: Active"

### Clients Directory  
- **techcorp.txt**: "Company: TechCorp, Contact: John Smith, Phone: 555-0123"
- **innovatellc.txt**: "Company: InnovateLLC, Contact: Sarah Johnson, Phone: 555-0456"
- **startupinc.txt**: "Company: StartupInc, Contact: Mike Wilson, Phone: 555-0789"

### Invoices Directory
- **invoice_001.txt**: "Client: TechCorp, Amount: 15000, Date: 2024-01-15"
- **invoice_002.txt**: "Client: InnovateLLC, Amount: 35000, Date: 2024-02-01"
- **invoice_003.txt**: "Client: TechCorp, Amount: 20000, Date: 2024-02-15"

## Extracted Data Files
- **client_alpha.txt**: "TechCorp"
- **client_beta.txt**: "InnovateLLC"
- **client_gamma.txt**: "StartupInc"

## Client Invoice Totals
- **techcorp_total.txt**: 35000 (15000 + 20000)
- **innovatellc_total.txt**: 35000
- **startupinc_total.txt**: 0

## Analysis Files
- **contact_list.txt**:
  ```
  TechCorp: John Smith, 555-0123
  InnovateLLC: Sarah Johnson, 555-0456
  StartupInc: Mike Wilson, 555-0789
  ```

- **active_projects.txt**:
  ```
  Project Alpha: TechCorp (Budget: 50000)
  Project Gamma: StartupInc (Budget: 25000)
  ```

- **completed_projects.txt**:
  ```
  Project Beta: InnovateLLC (Budget: 35000)
  ```

- **total_invoiced.txt**: 70000 (35000 + 35000 + 0)

- **client_summary.txt**:
  ```
  TechCorp - Budget: 50000, Invoiced: 35000
  InnovateLLC - Budget: 35000, Invoiced: 35000
  StartupInc - Budget: 25000, Invoiced: 0
  ```

- **reconciliation_report.txt**:
  ```
  TechCorp: Budget 50000 vs Invoiced 35000 (Remaining: 15000)
  InnovateLLC: Budget 35000 vs Invoiced 35000 (Remaining: 0)
  StartupInc: Budget 25000 vs Invoiced 0 (Remaining: 25000)
  Total Budget: 110000
  Total Invoiced: 70000
  Total Remaining: 40000
  ```

## Final Directory Structure
```
test8/
├── projects/
│   ├── project_alpha.txt
│   ├── project_beta.txt
│   └── project_gamma.txt
├── clients/
│   ├── techcorp.txt
│   ├── innovatellc.txt
│   └── startupinc.txt
├── invoices/
│   ├── invoice_001.txt
│   ├── invoice_002.txt
│   └── invoice_003.txt
├── client_alpha.txt
├── client_beta.txt
├── client_gamma.txt
├── techcorp_total.txt
├── innovatellc_total.txt
├── startupinc_total.txt
├── contact_list.txt
├── active_projects.txt
├── completed_projects.txt
├── total_invoiced.txt
├── client_summary.txt
└── reconciliation_report.txt
```