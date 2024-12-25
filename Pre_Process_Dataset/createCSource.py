import json
import os

# Đường dẫn đến tệp JSON
json_file_path = 'D:/LTAT/Project/dataset/non-vulnerables.json'

# Đường dẫn đến thư mục chứa các tệp mã nguồn C
output_dir = 'D:/LTAT/Project/dataset/chrome_debian/non-vulnerables'

# Đảm bảo thư mục đầu ra tồn tại
os.makedirs(output_dir, exist_ok=True)

# Đọc tệp JSON
with open(json_file_path, 'r') as f:
    ggnn_json_data = json.load(f)

# Tạo các tệp mã nguồn C từ nội dung của tệp JSON
for idx, entry in enumerate(ggnn_json_data, start=0):
    code = entry['code']
    # target = entry['target']
    # Tạo tên tệp bằng cách đánh số từ 1
    file_name = f"{idx}.c"
    file_path = os.path.join(output_dir, file_name)
    
    # print("File name: ", file_name)
    
    # Ghi mã nguồn vào tệp
    with open(file_path, 'w') as code_file:
        code_file.write(code)

print(f"Created {len(ggnn_json_data)} C source files in {output_dir}")
