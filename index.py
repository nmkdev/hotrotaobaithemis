import os
import subprocess
import random

def cls():
    os.system('cls')

def generate_random_name(existing_names, length=5):
    """Hàm để tạo tên ngẫu nhiên gồm các chữ số, không trùng với tên đã có."""
    while True:
        new_name = ''.join(random.choices('0123456789', k=length))
        if new_name not in existing_names:
            return new_name

def create_test_directories():
    # Đường dẫn thư mục gốc
    base_dir = "BAIKIEMTRA"
    
    # Kiểm tra xem thư mục gốc đã tồn tại chưa
    if os.path.exists(base_dir):
        rename = input(f"Thư mục '{base_dir}' đã tồn tại. Bạn có muốn đổi tên nó thành 5 số ngẫu nhiên không? (y/n): ")
        if rename.lower() == 'y':
            existing_names = [name for name in os.listdir('.') if os.path.isdir(name)]
            new_name = generate_random_name(existing_names)
            os.rename(base_dir, new_name)
            print(f"Đã đổi tên thư mục thành '{new_name}'.")
            input("Nhấn phím 'Enter' để tiếp tục...")
            cls()
        else:
            print("Không thực hiện việc tạo thư mục.")
            return
    
    # Tạo thư mục gốc
    os.makedirs(base_dir)

    # Nhập số lượng các thư mục bài test cần tạo
    test_folder_count = int(input("Nhập số lượng các bài: "))
    cls()
    for i in range(test_folder_count):
        folder_name = input(f"Nhập tên thư mục bài thứ {i + 1}: ")
        cls()
        test_folder_path = os.path.join(base_dir, folder_name)
        
        # Tạo thư mục bài test
        os.makedirs(test_folder_path)
        
        # Nhập số lượng các thư mục con cần tạo
        sub_folder_count = int(input(f"Nhập số lượng bài test cho '{folder_name}': "))
        cls()
        
        # Nhập tên file input và output cho TEST1
        input_file_name = input(f"Nhập tên file input (kèm đuôi mở rộng): ")
        cls()
        output_file_name = input(f"Nhập tên file output (kèm đuôi mở rộng): ")
        cls()
        
        for j in range(sub_folder_count):
            sub_folder_name = f"TEST{j + 1}"
            sub_folder_path = os.path.join(test_folder_path, sub_folder_name)
            os.makedirs(sub_folder_path)
            
            # Tạo file input và output với cùng tên cho tất cả các TEST
            with open(os.path.join(sub_folder_path, input_file_name), 'w') as f:
                pass  # Tạo file rỗng
            with open(os.path.join(sub_folder_path, output_file_name), 'w') as f:
                pass  # Tạo file rỗng
            
            print(f"Đã tạo thư mục '{sub_folder_name}' và các file '{input_file_name}', '{output_file_name}' của thư mục '{folder_name}'.")
            
            # Mở từng file trong thư mục TEST đó
            input_file_path = os.path.join(sub_folder_path, input_file_name)
            output_file_path = os.path.join(sub_folder_path, output_file_name)
            print(f"Đang mở tệp '{input_file_path}'...")
            subprocess.Popen(['notepad.exe', input_file_path])
            input("Nhấn phím 'Enter' để tiếp tục...")
            cls()
            print(f"Đang mở tệp '{input_file_path}'...")
            subprocess.Popen(['notepad.exe', output_file_path])
            input("Nhấn phím 'Enter' để tiếp tục...")
            cls()

if __name__ == "__main__":
    cls()
    create_test_directories()
    os.startfile("")