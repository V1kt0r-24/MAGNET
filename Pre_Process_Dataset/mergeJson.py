import json

# Đường dẫn đến hai tệp JSON đầu vào
input_json_file_path_1 = 'D:/LTAT/Project/dataset/chrome_debian/non-vulnerables.json'
input_json_file_path_2 = 'D:/LTAT/Project/dataset/chrome_debian/vulnerables.json'

# Đường dẫn đến tệp JSON đầu ra
output_json_file_path = 'D:/LTAT/Project/dataset/chrome_debian/chrome-debian.json'

# Đọc tệp JSON đầu vào thứ nhất
with open(input_json_file_path_1, 'r') as f:
    json_data_1 = json.load(f)

# Đọc tệp JSON đầu vào thứ hai
with open(input_json_file_path_2, 'r') as f:
    json_data_2 = json.load(f)

# Nối hai danh sách JSON lại với nhau
merged_json_data = json_data_1 + json_data_2

# Ghi lại tệp JSON đã được nối
with open(output_json_file_path, 'w') as f:
    json.dump(merged_json_data, f, indent=4)

print(f"Merged JSON file saved to {output_json_file_path}")