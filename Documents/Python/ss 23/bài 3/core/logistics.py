import math

def view_flights(flights):
    if not flights:
        print("---- DANH SÁCH HIỆN TẠI ĐANG TRỐNG ----")
        return

    print("----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")

    for index, value in enumerate(flights):
        number_water_bottle = math.ceil(value["passengers"] / 10)
        print(
            f"{index +1}. Mã: {value['flight_id']} | Khởi hành: {value['depart_time']} | Số khách: {value['passengers']} | Dự phòng: {number_water_bottle} thùng nước."
        )

    