from core.logistics import view_flights
from core.manager import add_flight
from utils.time_helper import time
from utils.file_helper import create_folder
            
def main():

    flights = [
        {
            "flight_id": "RA001",
            "passengers": 154,
            "depart_time": "2026-06-15 08:00:00",
            "duration_min": 120,
        },  # Hà Nội - TP.HCM
        {
            "flight_id": "RA002",
            "passengers": 85,
            "depart_time": "2026-06-15 13:30:00",
            "duration_min": 45,
        },  # Hà Nội - Vinh
    ]

    while True:
        choice = input("""\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====
    1. Hiển thị lịch trình và Thống kê hậu cần
    2. Tiếp nhận chuyến bay mới
    3. Tính thời gian hạ cánh dự kiến (ETA)
    4. Khởi tạo thư mục lưu trữ log hệ thống
    5. Thoát chương trình
==================================================
Nhập lựa chọn của bạn: """)
        match choice:
            case "1":
                view_flights(flights)
            case "2":
                add_flight(flights)
            case "3":
                time(flights)
            case "4":
                create_folder()
            case "5":
                print("Thoát")
                break
            case _:
                print("""Cảm ơn bạn đã sử dụng phân mêm 
[Chương trình ket thúc]""")
                continue


if __name__ == "__main__":
    main()