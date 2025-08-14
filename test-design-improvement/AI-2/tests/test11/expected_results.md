# Test11 期待結果

## 最終的なディレクトリ構造

```
sales_analytics/
├── pipeline_documentation.txt
├── raw_data/
│   ├── sales_2023.csv
│   ├── customers.csv
│   └── products.csv
├── processed/
│   ├── monthly_summary.csv
│   ├── category_analysis.csv
│   ├── top_products.csv
│   ├── top_regions.csv
│   ├── pipeline_monthly_summary.csv
│   └── pipeline_category_analysis.csv
├── reports/
│   ├── executive_summary.json
│   ├── kpi_analysis.json
│   ├── detailed_sales_report.csv
│   ├── summary_report.txt
│   ├── pipeline_executive_summary.json
│   ├── pipeline_kpi_analysis.json
│   ├── pipeline_summary.txt
│   ├── pipeline_log.txt
│   └── data_validation.txt
├── scripts/
│   ├── data_loader.py
│   ├── data_processor.py
│   ├── report_generator.py
│   └── pipeline_orchestrator.py
└── config/
    └── analysis_config.json
```

## 重要な計算期待値

### 売上データの基本統計:
- 総注文数: 10件
- 総売上金額: 1,001,000円
- 平均注文金額: 100,100円

### カテゴリー別分析（Electronics vs Accessories）:
- Electronics: 7件の注文、790,000円
- Accessories: 3件の注文、211,000円

### 利益計算:
- P001 Laptop: 売価80,000 - 原価60,000 = 利益20,000
- P002 Mouse: 売価3,000 - 原価2,000 = 利益1,000
- P003 Monitor: 売価45,000 - 原価30,000 = 利益15,000
- P004 Keyboard: 売価8,000 - 原価5,000 = 利益3,000
- P005 Tablet: 売価60,000 - 原価45,000 = 利益15,000

### 注文カテゴリー分類:
- HighValue（100,000以上）: Laptop注文、Monitor注文、Tablet注文
- Bulk（10個以上）: Mouse注文（12個）
- Standard: その他の注文

## 各ファイルの期待内容例

### processed/monthly_summary.csv
```
YearMonth,TotalAmount,WeightedAmount,TotalProfit,Quantity
2023-01,175000.00,172500.00,42000.00,7
2023-02,215000.00,228500.00,65000.00,4
2023-03,456000.00,441200.00,51000.00,12
2023-04,360000.00,368000.00,90000.00,5
2023-05,81000.00,78950.00,16000.00,13
```

### processed/category_analysis.csv
```
Category,TotalSales,AvgOrderValue,TotalProfit,AvgMargin,TotalQuantity
Accessories,87000.00,29000.00,17000.00,0.41,29
Electronics,914000.00,130571.43,247000.00,0.27,12
```

### processed/top_products.csv
```
ProductName,TotalAmount,TotalProfit
Laptop,480000.00,120000.00
Monitor,180000.00,60000.00
Tablet,120000.00,30000.00
```

### processed/top_regions.csv
```
Region,TotalAmount,TotalProfit
East,455000.00,125000.00
North,320000.00,80000.00
West,189000.00,42000.00
```

### reports/executive_summary.json
```json
{
  "report_date": "[実行時のISO日時]",
  "analysis_period": {
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
  },
  "total_sales": 1001000.0,
  "total_profit": 264000.0,
  "total_orders": 10,
  "average_order_value": 100100.0,
  "overall_profit_margin": 0.26
}
```

### reports/kpi_analysis.json
```json
{
  "high_value_orders": 6,
  "bulk_orders": 1,
  "high_margin_products": 4,
  "order_categories": {
    "HighValue": 6,
    "Bulk": 1,
    "Standard": 3
  }
}
```

### reports/summary_report.txt
```
=== SALES ANALYTICS SUMMARY REPORT ===

Report Date: [実行時のISO日時]
Analysis Period: {'start_date': '2023-01-01', 'end_date': '2023-12-31'}
Total Sales: 1001000.0
Total Profit: 264000.0
Total Orders: 10
Average Order Value: 100100.0
Overall Profit Margin: 0.26
```

### reports/data_validation.txt
```
Data Validation Report

Processed Files Validation:
- monthly_summary.csv: 5 rows, 5 columns
- category_analysis.csv: 2 rows, 5 columns  
- top_products.csv: 3 rows, 3 columns
- top_regions.csv: 4 rows, 3 columns
- pipeline_monthly_summary.csv: 5 rows, 5 columns
- pipeline_category_analysis.csv: 2 rows, 5 columns

JSON Files Validation:
- executive_summary.json: All required keys present
- kpi_analysis.json: All required keys present
- pipeline_executive_summary.json: All required keys present
- pipeline_kpi_analysis.json: All required keys present

Validation Status: All files validated successfully
```

### reports/pipeline_log.txt
```
Pipeline execution result: Pipeline completed successfully
Executed at: [実行時のISO日時]
```

### pipeline_documentation.txt
指定された内容でパイプラインの各段階、依存関係、出力ファイルについて詳細に記録されている。

## 重要な依存関係の確認

### データ依存関係:
1. sales_2023.csv + products.csv → 利益計算
2. 利益計算結果 → 注文カテゴリー分類
3. 地域データ + config設定 → 重み付け売上
4. 処理済みデータ → 各種分析レポート

### ファイル生成順序:
1. 生データ読み込み
2. データ処理（利益、カテゴリー、重み付け）
3. 分析生成（月次、カテゴリー、上位）
4. レポート生成（サマリー、KPI）
5. 統合パイプライン実行
6. 検証レポート作成

### 計算の整合性:
- 月次合計と全体合計の一致
- カテゴリー別合計と全体合計の一致
- 利益率の計算精度
- 地域重み付けの適用