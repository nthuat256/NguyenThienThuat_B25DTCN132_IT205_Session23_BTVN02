from tabulate import tabulate


def display_records(attendance_book):
    if not attendance_book:
        print("\nDanh sách chấm công đang trống!")
        return

    table_data = []

    for employee in attendance_book:
        clock_in, clock_out = employee["times"]

        table_data.append([
            employee["id"],
            employee["name"],
            clock_in,
            clock_out if clock_out else "[Đang làm việc]"
        ])

    print("\n--- BẢNG CHẤM CÔNG ---")

    print(
        tabulate(
            table_data,
            headers=["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"],
            tablefmt="grid"
        )
    )