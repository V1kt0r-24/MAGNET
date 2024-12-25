import json

# Đường dẫn đến tệp JSON đầu vào
input_json_file_path = 'D:/LTAT/Project/dataset/function.json'

# Đường dẫn đến tệp JSON đầu ra
output_json_file_path = 'C:/Users/ngocbao/Downloads/parsed/new.json'

# Đọc tệp JSON đầu vào
with open(input_json_file_path, 'r') as f:
    ggnn_json_data = json.load(f)

# Thêm trường 'name' với giá trị bắt đầu từ 1
for idx, entry in enumerate(ggnn_json_data, start=0):
    entry['name'] = str(idx) + '_' + str(entry['target']) + '.c'

# Ghi lại tệp JSON đã được cập nhật
with open(output_json_file_path, 'w') as f:
    json.dump(ggnn_json_data, f, indent=4)

print(f"Updated JSON file saved to {output_json_file_path}")