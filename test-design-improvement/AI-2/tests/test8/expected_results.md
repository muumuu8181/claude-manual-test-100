# Test8 期待結果

## 最終的なディレクトリ構造

```
inventory_system/
├── README.txt
├── products/
│   ├── electronics.json
│   └── furniture.json
├── orders/
│   ├── order_001.txt
│   └── order_002.txt
├── scripts/
│   ├── inventory_checker.py
│   └── process_orders.py
└── reports/
    ├── electronics_value.txt
    ├── furniture_value.txt
    ├── low_stock_alert.txt
    ├── order_001_total.txt
    ├── order_002_total.txt
    └── system_summary.txt
```

## 各ファイルの期待内容

### products/electronics.json
```json
{"laptop": {"price": 80000, "stock": 15}, "smartphone": {"price": 60000, "stock": 25}, "tablet": {"price": 45000, "stock": 12}}
```

### products/furniture.json
```json
{"desk": {"price": 25000, "stock": 8}, "chair": {"price": 15000, "stock": 20}, "shelf": {"price": 18000, "stock": 10}}
```

### orders/order_001.txt
```
Customer: Tanaka
Product: laptop
Quantity: 2
Date: 2024-01-15
```

### orders/order_002.txt
```
Customer: Suzuki
Product: chair
Quantity: 5
Date: 2024-01-15
```

### scripts/inventory_checker.py
```python
import json

def load_inventory(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_total_value(inventory):
    total = 0
    for item, details in inventory.items():
        total += details['price'] * details['stock']
    return total

def find_low_stock(inventory, threshold=10):
    low_stock_items = []
    for item, details in inventory.items():
        if details['stock'] < threshold:
            low_stock_items.append(f"{item}: {details['stock']}")
    return low_stock_items
```

### scripts/process_orders.py
```python
def parse_order_file(filename):
    order_data = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                key, value = line.strip().split(': ', 1)
                order_data[key.lower()] = value
    return order_data

def calculate_order_total(product_price, quantity):
    return product_price * int(quantity)
```

### reports/electronics_value.txt
```
2940000
```
計算: laptop(80000×15) + smartphone(60000×25) + tablet(45000×12) = 1200000 + 1500000 + 540000 = 3240000

### reports/furniture_value.txt
```
680000
```
計算: desk(25000×8) + chair(15000×20) + shelf(18000×10) = 200000 + 300000 + 180000 = 680000

### reports/low_stock_alert.txt
```
desk: 8
```

### reports/order_001_total.txt
```
160000
```
計算: laptop価格(80000) × 数量(2) = 160000

### reports/order_002_total.txt
```
75000
```
計算: chair価格(15000) × 数量(5) = 75000

### reports/system_summary.txt
```
Inventory Management Report
Electronics Total Value: 3240000
Furniture Total Value: 680000
Low Stock Items: 1
Orders Processed: 2
```

### README.txt
```
Inventory Management System

This system manages product inventory and processes orders.

Folder Structure:
- products/: Contains product information in JSON format
- orders/: Contains individual order files
- scripts/: Contains Python scripts for processing
- reports/: Contains generated reports and calculations

Files:
- electronics.json: Electronics product inventory
- furniture.json: Furniture product inventory  
- inventory_checker.py: Script for inventory analysis
- process_orders.py: Script for order processing
```