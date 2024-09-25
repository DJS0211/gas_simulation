def reverse_file_content(file_path):
    try:
        # 读取文件内容
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # 倒序行内容
        lines.reverse()
        
        # 将倒序内容写回文件
        with open(file_path, 'w') as file:
            file.writelines(lines)
        
        print(f"File '{file_path}' has been reversed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# 使用示例
file_path = 'lat_MCD12C1.txt'  # 替换为你的文件路径
reverse_file_content(file_path)