with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
    # Thông tin của bạn của bạn
    ten_ban_cua_ban = input("Nhập Họ Tên của bạn của bạn: ")
    ngay_thang_nam_sinh_ban= input("Nhập ngày tháng năm sinh của bạn của bạn: ")
    dia_chi_nha = input("Nhập quê quán của bạn của bạn: ")

    file.write('\nThông tin bạn của bạn:\n')
    file.write('Họ và tên: ' + ten_ban_cua_ban + '\n')
    file.write('Ngày tháng năm sinh: ' + ngay_thang_nam_sinh_ban + '\n')
    file.write('Quê Quán: ' + dia_chi_nha + '\n')

with open("NgoLongVu.txt", "r", encoding='utf-8') as file:
    noi_dung = file.read()
    print("Nội dung của file:")
    print(noi_dung)