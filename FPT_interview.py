import pandas as pd
import numpy as np

# --- Bước 1: Tạo DataFrame từ dữ liệu ---
orders_data = {
    'OrderDate': ['2025-07-15', '2025-07-15', '2025-07-15', '2025-07-15', '2025-07-16', '2025-07-16', '2025-07-16', '2025-07-16', '2025-07-17', '2025-07-17', '2025-07-17', '2025-07-18', '2025-07-18', '2025-07-18'],
    'OrderID': ['ORD001', 'ORD002', 'ORD003', 'ORD004', 'ORD005', 'ORD006', 'ORD007', 'ORD008', 'ORD009', 'ORD010', 'ORD011', 'ORD012', 'ORD013', 'ORD014'],
    'CustomerName': ['Alice Nguyen', 'Bob Tran', 'Charlie Le', 'Alice Nguyen', 'Alice Nguyen', 'Bob Tran', 'Diana Pham', 'Charlie Le', 'Alice Nguyen', 'Bob Tran', 'Diana Pham', 'Evan Ho', 'Bob Tran', 'Alice Nguyen'],
    'ProductCategory': ['Electronics', 'Furniture', 'Groceries', 'Electronics', 'Electronics', 'Groceries', 'Furniture', 'Electronics', 'Electronics', 'Groceries', 'Furniture', 'Furniture', 'Groceries', 'Electronics'],
    'ProductName': ['Smartphone X1', 'Wooden Chair', 'Organic Rice', 'Bluetooth Earbuds', 'Smartphone X1', 'Organic Rice', 'Office Desk', 'Bluetooth Earbuds', 'Smartphone X1', 'Organic Rice', 'Office Desk', 'Wooden Chair', 'Organic Rice', 'Smartphone X1'],
    'UnitPrice': [350, 75, 1.2, 45, 350, 1.2, 120, 45, 350, 1.2, 120, 75, 1.2, 350],
    'NumSold': [1, 2, 10, 1, 1, 8, 1, 2, 1, 5, 1, 1, 12, 1]
}
orders_df = pd.DataFrame(orders_data)

discount_data = {
    'ProductCategory': ['Electronics', 'Groceries'],
    'DiscountPercent': [10, 15]
}
discount_df = pd.DataFrame(discount_data)

# JOIN
merged_df = pd.merge(orders_df, discount_df, on='ProductCategory', how='left')

merged_df['DiscountPercent'] = merged_df['DiscountPercent'].fillna(0)

# Tinh doanh thu cho tung dong
merged_df['Revenue'] = merged_df['UnitPrice']*merged_df['NumSold'] * (1 - merged_df['DiscountPercent'] / 100)

customer_sales = merged_df.groupby('CustomerName')['Revenue'].sum()

result = customer_sales[customer_sales < 500]
print(result.reset_index())