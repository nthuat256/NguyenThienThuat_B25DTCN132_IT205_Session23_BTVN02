import os


def create_folder():
    print("----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")
    if os.path.exists("aviation_logs "):
        print("Thư mục đã tồn tại !!")
        return

    os.mkdir("aviation_logs")

    print("""[SYSTEM] Thư mục 'aviation_logs' chưa tồn tại. Đang tiến hành khởi tạo...
[SYSTEM] Tạo thư mục thành công!""")
