import os
import shutil
import random

# Đường dẫn đến thư mục mẹ
parent_dir = 'D:/LTAT/Project/ReVeal/code-slicer/joern/vulnerable'

# Đường dẫn đến hai thư mục mẹ mới
new_parent_dir_1 = 'D:/LTAT/Project/dataset/chrome_debian/parsed/Train'
new_parent_dir_2 = 'D:/LTAT/Project/dataset/chrome_debian/parsed/Test'

# Tạo hai thư mục mẹ mới nếu chưa tồn tại
os.makedirs(new_parent_dir_1, exist_ok=True)
os.makedirs(new_parent_dir_2, exist_ok=True)

# Lấy danh sách các thư mục con trong thư mục mẹ
subfolders = [f.path for f in os.scandir(parent_dir) if f.is_dir()]

# Xáo trộn danh sách thư mục con
random.shuffle(subfolders)

# Tính số lượng thư mục con cho mỗi thư mục mẹ mới
split_index = int(len(subfolders) * 0.7)

def get_unique_path(destination, name):
    counter = 1
    new_name = name
    while os.path.exists(os.path.join(destination, new_name)):
        new_name = f"{name}_{counter}"
        counter += 1
    return os.path.join(destination, new_name)

# Di chuyển các thư mục con vào thư mục mẹ mới
for subfolder in subfolders[:split_index]:
    shutil.move(subfolder, new_parent_dir_1)

for subfolder in subfolders[split_index:]:
    shutil.move(subfolder, new_parent_dir_2)

print(f"Moved {split_index} subfolders to {new_parent_dir_1}")
print(f"Moved {len(subfolders) - split_index} subfolders to {new_parent_dir_2}")