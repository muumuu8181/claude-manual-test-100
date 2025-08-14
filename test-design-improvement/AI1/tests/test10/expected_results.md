# Test 10: Expected Results

## Source Data Files
- **products.txt**: Laptop|500|25, Mouse|35|150, Keyboard|75|80, Monitor|250|40, Printer|180|30
- **suppliers.txt**: TechSupply|Laptop,Monitor, OfficeWorld|Mouse,Keyboard,Printer, GlobalTech|Laptop,Printer
- **orders.txt**: Order001|Laptop|5|2024-01-15, Order002|Mouse|20|2024-01-16, Order003|Monitor|3|2024-01-17

## Product Extraction Files
- **laptop.txt**: "Laptop|500|25"
- **mouse.txt**: "Mouse|35|150" 
- **keyboard.txt**: "Keyboard|75|80"
- **monitor.txt**: "Monitor|250|40"
- **printer.txt**: "Printer|180|30"

## Initial Inventory Values
- **value_laptop.txt**: 12500 (500×25)
- **value_mouse.txt**: 5250 (35×150)
- **value_keyboard.txt**: 6000 (75×80)
- **value_monitor.txt**: 10000 (250×40)
- **value_printer.txt**: 5400 (180×30)

## Supplier Relationships
- **supplier_laptop.txt**: TechSupply, GlobalTech
- **supplier_mouse.txt**: OfficeWorld
- **supplier_keyboard.txt**: OfficeWorld
- **supplier_monitor.txt**: TechSupply
- **supplier_printer.txt**: OfficeWorld, GlobalTech

## Order Processing
- **order001_total.txt**: 2500 (5×500)
- **order002_total.txt**: 700 (20×35)
- **order003_total.txt**: 750 (3×250)

## Updated Inventory After Orders
- **updated_laptop.txt**: 20 (25-5)
- **updated_mouse.txt**: 130 (150-20)
- **updated_monitor.txt**: 37 (40-3)

## New Inventory Values
- **new_value_laptop.txt**: 10000 (500×20)
- **new_value_mouse.txt**: 4550 (35×130)
- **new_value_monitor.txt**: 9250 (250×37)

## Stock Analysis
- **low_stock.txt**: Laptop (20), Monitor (37), Printer (30)
- **high_stock.txt**: Mouse (130)
- **total_value_before.txt**: 39150
- **total_value_after.txt**: 35250
- **total_orders_value.txt**: 3950

## Final Reports
Contains comprehensive analysis including supplier relationships, inventory optimization recommendations, and executive summary with key findings.