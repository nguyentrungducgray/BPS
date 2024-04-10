import pandas as pd

data = pd.read_csv("data.csv")
data.head()

# Xử lý giá trị thiếu (Null)
data.fillna(data.mean(), inplace=True)

# Loại bỏ dữ liệu trùng lặp
data.drop_duplicates(inplace=True)

# Xử lý giá trị rỗng
data.dropna(inplace=True)

# Tính toán thống kê mô tả
description = data.describe()

# Tính toán và thêm cột mới
data['Tổng lợi nhuận'] = data['Sản lượng bán hàng'] * 10 
print(description)
print(data)