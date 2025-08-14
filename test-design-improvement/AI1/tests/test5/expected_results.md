# Test 5: Expected Results

## Source Data
- **sales_data.txt**: Product A: 150, Product B: 89, Product C: 203, Product D: 67, Product E: 134

## Commission Calculations (15% each)
- **commission_a.txt**: 22.5 (150 × 0.15)
- **commission_b.txt**: 13.35 (89 × 0.15)
- **commission_c.txt**: 30.45 (203 × 0.15)
- **commission_d.txt**: 10.05 (67 × 0.15)
- **commission_e.txt**: 20.1 (134 × 0.15)

## Statistical Analysis
- **top_performer.txt**: Product C: 203
- **bottom_performer.txt**: Product D: 67
- **total_sales.txt**: 643 (150+89+203+67+134)
- **average_sales.txt**: 128.6 (643 ÷ 5)
- **total_commission.txt**: 96.45 (sum of all commissions)

## Comparative Analysis  
- **above_average.txt**: 3 (Products A: 150, C: 203, E: 134)
- **below_average.txt**: 2 (Products B: 89, D: 67)

## Reports
- **sales_report.txt**: Products listed in descending sales order:
  ```
  Product C: 203
  Product A: 150  
  Product E: 134
  Product B: 89
  Product D: 67
  ```

- **analysis_summary.txt**: Complete summary including:
  - Total sales: 643
  - Average sales: 128.6
  - Top performer: Product C (203)
  - Bottom performer: Product D (67)
  - Total commission: 96.45
  - Products above average: 3
  - Products below average: 2

## Directory Structure
```
test5/
├── sales_data.txt
├── commission_a.txt
├── commission_b.txt
├── commission_c.txt
├── commission_d.txt
├── commission_e.txt
├── top_performer.txt
├── bottom_performer.txt
├── total_sales.txt
├── average_sales.txt
├── sales_report.txt
├── total_commission.txt
├── above_average.txt
├── below_average.txt
└── analysis_summary.txt
```