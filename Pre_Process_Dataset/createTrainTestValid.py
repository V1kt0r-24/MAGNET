import json
import random

# Đường dẫn đến tệp JSON đầu vào
input_json_file_path = 'D:/LTAT/Project/dataset/chrome_debian/parsed/chrome-debian.json'

# Đường dẫn đến các tệp JSON đầu ra
train_json_file_path = 'D:/LTAT/Project/MAGNET/Data/reveal-train-v0.json'
test_json_file_path = 'D:/LTAT/Project/MAGNET/Data/reveal-test-v0.json'
valid_json_file_path = 'D:/LTAT/Project/MAGNET/Data/reveal-valid-v0.json'

# Đọc tệp JSON đầu vào
with open(input_json_file_path, 'r') as f:
    json_data = json.load(f)

# Xáo trộn danh sách JSON
random.shuffle(json_data)

# Tính số lượng mục cho mỗi tập
total = len(json_data)
train_size = int(total * 0.6)
test_size = int(total * 0.2)
valid_size = total - train_size - test_size

# Chia dữ liệu thành ba tập
train_data = json_data[:train_size]
test_data = json_data[train_size:train_size + test_size]
valid_data = json_data[train_size + test_size:]

# Ghi lại các tệp JSON đã được chia
with open(train_json_file_path, 'w') as f:
    json.dump(train_data, f, indent=4)

with open(test_json_file_path, 'w') as f:
    json.dump(test_data, f, indent=4)

with open(valid_json_file_path, 'w') as f:
    json.dump(valid_data, f, indent=4)

print(f"Train JSON file saved to {train_json_file_path}")
print(f"Test JSON file saved to {test_json_file_path}")
print(f"Validation JSON file saved to {valid_json_file_path}")