import os

# Đường dẫn đến thư mục mẹ chứa các thư mục con cần đổi tên
parent_dir = 'D:/LTAT/Project/ReVeal/code-slicer/joern/vulnerables'

# Lấy danh sách các thư mục con trong thư mục mẹ
subfolders = [f.path for f in os.scandir(parent_dir) if f.is_dir()]

# Đổi tên các thư mục từ định dạng name.c sang name_0.c
for subfolder in subfolders:
    folder_name = os.path.basename(subfolder)
    if folder_name.endswith('.c') and folder_name[:-2].isdigit():
        new_folder_name = f"{folder_name[:-2]}_1.c"
        new_folder_path = os.path.join(parent_dir, new_folder_name)
        os.rename(subfolder, new_folder_path)
        print(f"Renamed {subfolder} to {new_folder_path}")

print("Renaming completed.")