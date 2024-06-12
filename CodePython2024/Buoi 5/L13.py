def nhan_xuat_thong_tin():
    with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
        ten_ban = input("Nhập Họ Tên của bạn: ")
        tuoi = input("Nhập ngày tháng năm sinh: ")
        que_quan = input("Nhập quê quán của bạn: ")

        file.write("Họ và tên: " + ten_ban + "\n")
        file.write("Ngày tháng năm sinh: " + tuoi + "\n")
        file.write("Quê quán: " + que_quan + "\n")

def doc_file():
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

def doc_thong_tinab():
    with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
        nhap_a = int(input("Nhập số a: "))
        nhap_b = int(input("Nhập số b: "))
        tinh_tong = nhap_a + nhap_b
        tinh_hieu = nhap_a - nhap_b
        tinh_tich = nhap_a * nhap_b
        tinh_thuong = nhap_a / nhap_b

        file.write('Tổng của 2 số là: ' + str(tinh_tong) + '\n')
        file.write('Hiệu của 2 số là: ' + str(tinh_hieu) + '\n')
        file.write('Tích của 2 số là: ' + str(tinh_tich) + '\n')
        file.write('Thương của 2 số là: ' + str(tinh_thuong) + '\n')

def ve_hinh():
    with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
        file.write("           *******      \n")
        file.write("       *              *    \n")
        file.write("     *      @   @      *   \n")
        file.write("     *                 *  \n")
        file.write("      *       3       *  \n")
        file.write("        *           *    \n")
        file.write("           *******     \n")

def day_so_tu_dong():
    with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
        nhap_so = input("Nhập dãy số: ").split()
        for so in nhap_so:
            file.write(so + "\n")

    tong_so_chan = 0
    tong_so_le = 0
    tich_so_chan = 1
    tich_so_le = 1

    with open("NgoLongVu.txt", "r", encoding='utf-8') as file:
        for line in file:
            number = int(line.strip())
            if number % 2 == 0:
                tong_so_chan += number
                tich_so_chan *= number
            else:
                tong_so_le += number
                tich_so_le *= number

    with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
        file.write("Tổng các số chẵn là: " + str(tong_so_chan) + "\n")
        file.write("Tích các số chẵn là: " + str(tich_so_chan) + "\n")
        file.write("Tổng các số lẻ là: " + str(tong_so_le) + "\n")
        file.write("Tích các số lẻ là: " + str(tich_so_le) + "\n")

def dem_ki_tu():
    with open("NgoLongVu.txt", "a", encoding='utf-8')as file:
        ho_ten = input("Nhập họ tên của bạn: ")
        age = input("Nhập tuổi của bạn: ")
        dia_chi = input("Nhập địa chỉ của bạn: ")

        file.write("Họ tên: "+ ho_ten + "\n")
        file.write("Tuổi: " + age + "\n")
        file.write("Địa chỉ: " + dia_chi + "\n")

    with open("NgoLongVu.txt", "r", encoding='utf-8')as file:
        ky_tu = file.read()
        so_ky_tu = len(ky_tu)
    with open("NgoLongVu.txt", "a", encoding='utf-8')as file:
        file.write("Số Kí tự: " +str(so_ky_tu)+ "\n")

def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua

def giai_thua():
    with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
        n = int(input("Nhập số tự nhiên n: "))
        giai_thua_n = tinh_giai_thua(n)
        file.write("Số tự nhiên n: " + str(n) + "\n")
def nhap_diem_sinh_vien():
   diem_sinh_vien = []
   for i in range(5):
       ten_sinh_vien = input(f"Nhập tên sinh viên {i+1}: ")
       diem = []
       for j in range(5):
           diem_mon = float(input(f"Nhập điểm môn {j+1} của {ten_sinh_vien}: "))
           diem.append(diem_mon)
       diem_sinh_vien.append((ten_sinh_vien, diem))

   with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
       file.write("Tính điểm trung bình của các sinh viên \n")
       file.write("Bảng điểm sinh viên: \n")

       diem_trung_binh_cao_nhat = 0
       diem_trung_binh_thap_nhat = float('inf')
       sinh_vien_cao_nhat = ""
       sinh_vien_thap_nhat = ""

       for sinh_vien, diem in diem_sinh_vien:
           tong_diem = sum(diem)
           diem_trung_binh = tong_diem / 5
           file.write(f"{sinh_vien}: Tổng điểm={tong_diem}, Điểm trung bình={diem_trung_binh:.2f}\n")
           if diem_trung_binh > diem_trung_binh_cao_nhat:
               diem_trung_binh_cao_nhat = diem_trung_binh
               sinh_vien_cao_nhat = sinh_vien
           if diem_trung_binh < diem_trung_binh_thap_nhat:
               diem_trung_binh_thap_nhat = diem_trung_binh
               sinh_vien_thap_nhat = sinh_vien

       file.write(f"\nSinh viên có điểm trung bình cao nhất: {sinh_vien_cao_nhat} ({diem_trung_binh_cao_nhat:.2f}) \n")
       file.write(f"Sinh viên có điểm trung bình thấp nhất: {sinh_vien_thap_nhat} ({diem_trung_binh_thap_nhat:.2f}) \n \n")

   print("Hoàn thành việc tính toán và ghi kết quả.")

def danh_sach_thu_moi():
   danh_sach = []
   with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
       file.write("Nhập danh sách thư mời:\n")

       while True:
           khach_moi = input("Nhập tên khách mời: ")
           if not khach_moi:
               break
           file.write(f"- {khach_moi}\n")
           danh_sach.append(khach_moi)

       print("Danh sách thư mời:")
       for khach_moi in danh_sach:
           print(f"- {khach_moi}")

       danh_sach_xoa = input("Nhập tên thành viên muốn xóa khỏi thư mời: ")
       if danh_sach_xoa in danh_sach:
           danh_sach.remove(danh_sach_xoa)
           file.write(f"\nĐã xóa ({danh_sach_xoa}) khỏi danh sách thư mời.\n")
           print(f"Đã xóa {danh_sach_xoa} khỏi danh sách thư mời.")
       else:
           file.write(f"\n{danh_sach_xoa} không có trong danh sách thư mời.\n")
           print(f"{danh_sach_xoa} không có trong danh sách thư mời.")

       file.write("\nDanh sách thư mời sau khi xóa:\n")
       for khach_moi in danh_sach:
           file.write(f"- {khach_moi}\n")

   print("Hoàn thành việc cập nhật danh sách thư mời.")

def doc_file_random():
   import random
   with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
       day_so = [random.randint(1, 100) for _ in range(10)]
       file.write(" ".join(map(str, day_so)))

   with open("NgoLongVu.txt", "r", encoding='utf-8') as file:
       noi_dung = file.read()
       cac_so = list(map(int, noi_dung.split()))
       tong = sum(cac_so)
       print(f"Nội dung của file: {noi_dung}")
       print(f"Tổng các số trong dãy số: {tong}")

def infile_docfile():
   import os

   if not os.path.exists("NgoLongVu1.txt"):
       noi_dung_bai_tho = input("File NgoLongVu1.txt không tồn tại. Vui lòng nhập nội dung của một bài thơ:\n")
       with open("NgoLongVu1.txt", "w", encoding='utf-8') as file:
           file.write(noi_dung_bai_tho)
   else:
       with open("NgoLongVu1.txt", "r", encoding='utf-8') as file:
           noi_dung_bai_tho = file.read()
           print("Nội dung của bài thơ trong file poem.txt:")
           print(noi_dung_bai_tho)

def menu():
   while True:
       print("===== MENU =====")
       print("1. Nhập xuất thông tin")
       print("2. Đọc thông tin bạn của bạn")
       print("3. Nhập và tính toán 2 số")
       print("4. Vẽ hình")
       print("5. Nhập dãy số và tính toán")
       print("6. Đếm kí tự")
       print("7. Tính giai thừa")
       print("8. Nhập điểm sinh viên")
       print("9. Danh sách thư mời")
       print("10. Đọc file random")
       print("11. Đọc file bài thơ")
       print("12. Thoát")
       choice = input("Hãy Nhập Lựa Chọn Của Bạn: ")

       if choice == "1":
           nhan_xuat_thong_tin()
       elif choice == "2":
           doc_file()
       elif choice == "3":
           doc_thong_tinab()
       elif choice == "4":
           ve_hinh()
       elif choice == "5":
           day_so_tu_dong()
       elif choice == "6":
           dem_ki_tu()
       elif choice == "7":
           giai_thua()
       elif choice == "8":
           nhap_diem_sinh_vien()
       elif choice == "9":
           danh_sach_thu_moi()
       elif choice == "10":
           doc_file_random()
       elif choice == "11":
           infile_docfile()
       elif choice == "12":
           print("Tạm biệt!")
           break
       else:
           print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
menu()