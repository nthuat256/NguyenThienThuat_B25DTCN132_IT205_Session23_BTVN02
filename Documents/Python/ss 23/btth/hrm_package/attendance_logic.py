def find_employee(attendance_book, employee_id):
    return next(
        (
            employee
            for employee in attendance_book
            if employee["id"] == employee_id
        ),
        None
    )


def clock_in(attendance_book):
    employee_id = input("Nhập mã nhân viên: ").strip().upper()

    if find_employee(attendance_book, employee_id):
        print("Lỗi: Mã nhân viên đã tồn tại!")
        return

    employee_name = input("Nhập tên nhân viên: ").strip()
    clock_in_time = input("Nhập giờ vào (HH:MM): ").strip()

    attendance_book.append(
        {
            "id": employee_id,
            "name": employee_name,
            "times": (clock_in_time, None)
        }
    )

    print(
        f"Thành công: Đã ghi nhận {employee_id} "
        f"chấm công vào lúc {clock_in_time}!"
    )


def clock_out(attendance_book):
    employee_id = input("Nhập mã nhân viên: ").strip().upper()

    employee = find_employee(attendance_book, employee_id)

    if not employee:
        print("Không tìm thấy nhân viên!")
        return

    clock_out_time = input("Nhập giờ ra (HH:MM): ").strip()

    old_clock_in, _ = employee["times"]

    employee["times"] = (
        old_clock_in,
        clock_out_time
    )

    print(
        f"Thành công: {employee_id} "
        f"đã chấm công ra lúc {clock_out_time}!"
    )