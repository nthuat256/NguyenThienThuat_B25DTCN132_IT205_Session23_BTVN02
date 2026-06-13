from datetime import datetime


STANDARD_HOURS = 9


def convert_time(time_string):
    return datetime.strptime(
        time_string,
        "%H:%M"
    )


def evaluate_flex_time(attendance_book):
    print("\n--- ĐÁNH GIÁ FLEX-TIME ---")

    for employee in attendance_book:
        employee_id = employee["id"]

        clock_in, clock_out = employee["times"]

        if clock_out is None:
            print(
                f"{employee_id} - "
                "Chưa đủ dữ liệu để đánh giá."
            )
            continue

        clock_in_obj = convert_time(clock_in)
        clock_out_obj = convert_time(clock_out)

        latest_allowed = convert_time("10:00")

        if clock_in_obj > latest_allowed:
            print(
                f"{employee_id} - "
                "Vi phạm: Đến muộn quá 90 phút."
            )
            continue

        worked_hours = (
            clock_out_obj - clock_in_obj
        ).seconds / 3600

        if worked_hours < STANDARD_HOURS:
            print(
                f"{employee_id} - "
                "Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ."
            )
        else:
            print(
                f"{employee_id} - "
                "Hợp lệ: Hoàn thành ca làm việc."
            )