def input_not_emtry(mesage):
    while True:
        value = input(mesage).strip()
        if not value:
            print(" [CẢNH BÁO] : Không được để trống !!")
            continue

        return value


def index_id(id, attendance_book):
    return next(
        (index for index, value in enumerate(attendance_book) if id == value["flight_id"]), -1
    )

def input_not_smaller(message , type = int , item_name = "số nguyên"):
    while True:
        value = input_not_emtry(message)

        try:
            value = type(value)

            if value <= 0:
                print("Phải nhâp lớn hơn hoặc bằng 0 !")
                continue

            return value
        except ValueError:
            print(f"Vui lòng nhập kiểu dữ liệu {item_name} !!")