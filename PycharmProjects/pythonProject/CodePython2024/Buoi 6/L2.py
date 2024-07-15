with open("NgoLongVu.h5", "a", encoding='utf-8') as file:
    ten_ban = input("Nhập Họ Tên của bạn: ")
    tuoi = input("Nhập ngày tháng năm sinh: ")
    que_quan = input("Nhập quê quán của bạn: ")

    file.write("Họ và tên: " + ten_ban + "\n")
    file.write("Ngày tháng năm sinh: " + tuoi + "\n")
    file.write("Quê quán: " + que_quan + "\n")
