import validate.validates as validate

def add_flight(flight_list) :
  print("---- TIẾP NHẬN CHUYẾN BAY MỚI ----")
  id_flight = validate.input_not_emtry("Nhập mã chuyển bay: ").upper()
  
  if validate.index_id(id_flight , flight_list) != -1 :
    print("Chuyến bay đã tồn tại !!!")
    return
  
  number_guests = validate.input_not_smaller("Nhập số lượng hành khách: ")
  
  times = validate.input_not_emtry("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ")
  
  time_flight = validate.input_not_smaller("Nhập số phút bay: ")
  
  new_flight = {
     "flight_id": id_flight,
      "passengers": number_guests,
      "depart_time": times,
      "duration_min": time_flight,
  }
  
  flight_list.append(new_flight)
  
  print(f">> Thêm chuyến bay {id_flight} thành công!")