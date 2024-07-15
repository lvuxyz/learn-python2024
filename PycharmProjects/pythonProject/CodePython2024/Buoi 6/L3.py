bang_cuu_chuong = int(input("ban hay nhap bang cuu chuong: "))
with open("bangCuuChuong.txt", "w", encoding='utf-8') as file:
    file.write(f"Bảng cửu chương {bang_cuu_chuong}\n")
    for i in range(1, 10):
        ket_qua = bang_cuu_chuong * i
        dong = f"{bang_cuu_chuong} x {i} = {ket_qua}\n"
        file.write(dong)

with open("bangCuuChuong.txt", "r", encoding='utf-8') as file:
    noi_dung = file.read()
    print(f"Nội dung của file:\n{noi_dung}")
