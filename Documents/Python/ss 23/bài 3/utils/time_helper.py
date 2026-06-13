import datetime
import validate.validates as validate


def time(flights):
    print("----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
    id_flight = validate.input_not_emtry("Nhập mã chuyển bay: ").upper()

    if validate.index_id(id_flight, flights) == -1:
        print("Chuyến bay không tồn tại !!!")
        return

    index = validate.index_id(id_flight, flights)

    for value in flights:
        if value["flight_id"] == id_flight:

            depart_time = datetime.datetime.strptime(value["depart_time"], "%Y-%m-%d %H:%M:%S")

            eta = depart_time + datetime.timedelta(minutes=value["duration_min"])
          
    print(f"""-> Chuyến bay {id_flight} cất cánh lúc: {flights[index]['depart_time']}
-> Thời gian hạ cánh dự kiến (ETA): {eta}""")
