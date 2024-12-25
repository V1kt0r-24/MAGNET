import json

# Đường dẫn đến tệp JSON đầu vào
input_json_file_path = 'D:/LTAT/Project/dataset/vulnerables.json'

# Đường dẫn đến tệp JSON đầu ra
output_json_file_path = 'D:/LTAT/Project/dataset/chrome_debian/vulnerables.json'

# Đọc tệp JSON đầu vào
with open(input_json_file_path, 'r') as f:
    json_data = json.load(f)

# Thêm trường 'name' và 'target' cho mỗi mục trong JSON
for idx, entry in enumerate(json_data):
    entry['name'] = f"{idx}_1.c"
    entry['target'] = 0

# Ghi lại tệp JSON đã được cập nhật
with open(output_json_file_path, 'w') as f:
    json.dump(json_data, f, indent=4)

print(f"Updated JSON file saved to {output_json_file_path}")