import os
import csv
import json
import pandas as pd
import numpy as np
def parse_edges(edges_file):
    """Đọc file edges.csv và trả về danh sách các liên kết."""
    # edges = []
    # with open(edges_file, 'r') as file:
    #     reader = csv.DictReader(file, delimiter='\t')
    #     for row in reader:
    #         edge = {
    #             "start": row["start"],
    #             "end": row["end"],
    #             "type": row["type"]
    #         }
    #         edges.append(edge)
    
    df = pd.read_csv(edges_file, delimiter='\t')
    df = df.replace({np.nan: ""})
    return df.to_dict(orient='records')

    # return pd.read_csv(edges_file, delimiter='\t').to_dict(orient='records').replace({np.nan: ""})

def parse_nodes(nodes_file):
    """Đọc file nodes.csv và trả về danh sách các node features."""
    # nodes = []
    # with open(nodes_file, 'r') as file:
    #     reader = csv.DictReader(file, delimiter='\t')
    #     for row in reader:
    #         node = {
    #             "command": row["command"],
    #             "key": row["key"],
    #             "type": row["type"],
    #             "code": row["code"],
    #             "location": row["location"],
    #             "functionId": row["functionId"],
    #             "childNum": row["childNum"],
    #             "isCFGNode": row["isCFGNode"],
    #             "operator": row["operator"],
    #             "baseType": row["baseType"],
    #             "completeType": row["completeType"],
    #             "identifier": row["identifier"]
    #         }
    #         nodes.append(node)
    df = pd.read_csv(nodes_file, delimiter='\t')
    df = df.replace({np.nan: ""})
    return df.to_dict(orient='records')
    # return pd.read_csv(nodes_file, delimiter='\t').to_dict(orient='records').replace({np.nan: ""})

def generate_json_from_folders(base_dir, output_file):
    """Duyệt qua các thư mục trong base_dir và tạo file JSON từ các thư mục đó."""
    all_data = []  # Danh sách chứa dữ liệu từ tất cả các thư mục
    
    # Duyệt qua tất cả các thư mục trong thư mục cơ sở
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        
        # Kiểm tra nếu đây là một thư mục có tên theo định dạng Name_target
        if os.path.isdir(folder_path) and "_" in folder_name:
            # Tách name và target từ tên folder
            folder_name = folder_name.rstrip(".c")
            name, target = folder_name.split('_')
            
            nodes_file = os.path.join(folder_path, "nodes.csv")
            edges_file = os.path.join(folder_path, "edges.csv")
            
            # Kiểm tra nếu cả hai file nodes.csv và edges.csv đều tồn tại
            if os.path.exists(nodes_file) and os.path.exists(edges_file):
                # Đọc dữ liệu từ các file CSV
                node_features = parse_nodes(nodes_file)
                graph = parse_edges(edges_file)
                
                # Tạo đối tượng dữ liệu cho thư mục này
                folder_data = {
                    "name": name,
                    "target": target,
                    "node_features": node_features,
                    "graph": graph
                }
                all_data.append(folder_data)
                
    # In phần đầu của dữ liệu JSON ra terminal để kiểm tra
    # print(json.dumps(all_data[:1], indent=4))  # In phần đầu tiên của dữ liệu (1 phần tử) để kiểm tra

    # Ghi kết quả vào file JSON
    with open(output_file, 'w') as json_file:
        json.dump(all_data, json_file, indent=4)

# Ví dụ sử dụng
base_dir = "D:/LTAT/Project/dataset/chrome_debian/parsed/Full"  # Đường dẫn đến thư mục chứa các thư mục Name_target
output_file = "D:/LTAT/Project/dataset/chrome_debian/parsed/Full.json"  # Đường dẫn đến file JSON đầu ra

# Tạo file JSON từ các thư mục
generate_json_from_folders(base_dir, output_file)

print(f"Đã tạo file JSON: {output_file}")
