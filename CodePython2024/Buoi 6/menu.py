import os
import shutil
import random
import re
import csv

def tep_tin_so_ngau_nhien():
    ran_dom = random.randint(1, 100)
    ten_file = f"{ran_dom}.txt"
    with open(ten_file, 'w') as file:
        file.write(str(ran_dom))
    with open(ten_file, 'r') as file:
        content = file.read()
        print(f'Nội dung tệp tin {ten_file}: {content}')

def tep_tin_van_ban_h5():
    with open("NgoLongVu.h5", "w", encoding='utf-8') as file:
        ten_ban = input("Nhập Họ Tên của bạn: ")
        tuoi = input("Nhập ngày tháng năm sinh: ")
        que_quan = input("Nhập quê quán của bạn: ")

        file.write("Họ và tên: " + ten_ban + "\n")
        file.write("Ngày tháng năm sinh: " + tuoi + "\n")
        file.write("Quê quán: " + que_quan + "\n")

def nhap_bang_cuu_chuong():
    while True:
        try:
            bang_cuu_chuong = int(input("Nhập bảng cửu chương (1-9): "))
            if 1 <= bang_cuu_chuong <= 9:
                break
            else:
                print("Vui lòng nhập số từ 1 đến 9.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

    with open("bangCuuChuong.txt", "w", encoding='utf-8') as file:
        file.write(f"Bảng cửu chương {bang_cuu_chuong}\n")
        for i in range(1, 10):
            ket_qua = bang_cuu_chuong * i
            dong = f"{bang_cuu_chuong} x {i} = {ket_qua}\n"
            file.write(dong)

    with open("bangCuuChuong.txt", "r", encoding='utf-8') as file:
        noi_dung = file.read()
        print(f"Nội dung của file:\n{noi_dung}")

def sao_chep_ND_vb():
    file_moi = "copy_bangCuuChuong.txt"
    if os.path.exists("bangCuuChuong.txt"):
        shutil.copy("bangCuuChuong.txt", file_moi)
        print(f"Đã sao chép nội dung sang {file_moi}")
    else:
        print("Tệp tin bangCuuChuong.txt không tồn tại để sao chép.")

def di_chuyen_tap_tin():
    new_name = "thu_muc_chuyen.txt"
    thu_mucms = "file_1"
    os.makedirs(thu_mucms, exist_ok=True)

    if os.path.exists("copy_bangCuuChuong.txt"):
        shutil.move("copy_bangCuuChuong.txt", os.path.join(thu_mucms, new_name))
        print(f"Đã di chuyển tệp tin {new_name} vào thư mục {thu_mucms}")
    else:
        print("Tệp tin copy_bangCuuChuong.txt không tồn tại để di chuyển.")

def xoa_nd():
    file_to_delete = "file_1/thu_muc_chuyen.txt"
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
        print(f"Đã xóa tệp tin {file_to_delete}")
    else:
        print("Tệp tin cần xóa không tồn tại.")

def check_thong_tin_tep():
    if os.path.exists("bangCuuChuong.txt"):
        with open("bangCuuChuong.txt", "r", encoding='utf-8') as f:
            content = f.read()
            if "5 x 5 = 25" in content:
                print("Tệp tin có bảng cửu chương 5")
            else:
                print("Tệp tin không có bảng cửu chương 5")
    else:
        print("Tệp tin bangCuuChuong.txt không tồn tại để kiểm tra.")

def ten_tep_yeu_thich():
    doi_ten = input("Nhập tên tệp bạn muốn đổi: ")
    ten_moi = input("Nhập tên mới cho tệp: ")
    if os.path.exists(doi_ten):
        os.rename(doi_ten, ten_moi)
        print(f"Đã đổi tên tệp từ '{doi_ten}' thành '{ten_moi}'.")
    else:
        print(f"Tệp '{doi_ten}' không tồn tại để đổi tên.")

def check_file_ton_tai():
    check_file = input("Nhập tên tệp bạn muốn kiểm tra: ")
    if os.path.isfile(check_file):
        print(f"Tệp tin {check_file} tồn tại")
    else:
        print(f"Tệp tin {check_file} không tồn tại")

def randon_100so():
    with open("file_100_so.txt", 'w', encoding='utf-8') as file:
        so_tu_dong = [random.randint(1, 1000) for _ in range(100)]
        for num in so_tu_dong:
            file.write(str(num) + "\n")

    with open("file_100_so.txt", "r") as file:
        numbers = [int(line.strip()) for line in file.readlines()]
        lon_nhat = max(numbers)
        nho_nhat = min(numbers)
        trung_binh = sum(numbers) / len(numbers)

        print(f"Số lớn nhất: {lon_nhat}")
        print(f"Số nhỏ nhất: {nho_nhat}")
        print(f"Trung bình: {trung_binh}")

def nhap_thong_tin_file():
    with open('thong_tin.txt', 'w', encoding='utf-8') as file:
        while True:
            info = input("Nhập thông tin (nhấn Enter để kết thúc): ")
            if not info:
                break
            file.write(info + '\n')

    with open('thong_tin.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        email_pattern = r'\b[\w.-]+@gmail\.com\b'
        emails = re.findall(email_pattern, content)
        if emails:
            print("Các email trong file:")
            for email in emails:
                print(email)
        else:
            print("Không có email trong file.")



def hai_hang():
    data = [['Tên', 'Tuổi']]
    while True:
        ten = input("Nhập tên (nhấn Enter để kết thúc): ")
        if not ten:
            break
        tuoi = input("Nhập tuổi: ")
        data.append([ten, tuoi])
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(data)

    print("Dữ liệu trong file data.csv:")
    with open('data.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        for row in reader:
            print(f'{row[0].strip()} | {row[1].strip()}')
def nhap_thong_tin_chi_tieu():
    # Mở file để ghi với encoding là utf-8
    with open('chi_tieu.txt', 'w', encoding='utf-8') as file:
        print("Nhập thông tin chi tiêu hàng tháng:")
        while True:
            print("Tiền điện nước (nhấn Enter để dừng): ", end="")
            tien_dien_nuoc = input()
            print("Tiền ăn (nhấn Enter để dừng): ", end="")
            tien_an = input()
            print("Tiền kí túc xá (nhấn Enter để dừng): ", end="")
            tien_ki_tuc_xa = input()
            print("Tiền xăng xe (nhấn Enter để dừng): ", end="")
            tien_xang_xe = input()
            print("Tiền uống rượu (nhấn Enter để dừng): ", end="")
            tien_uong_ruou = input()

            if not tien_dien_nuoc and not tien_an and not tien_ki_tuc_xa and not tien_xang_xe and not tien_uong_ruou:
                break

            file.write(f"Tiền điện nước: {tien_dien_nuoc}\n")
            file.write(f"Tiền ăn: {tien_an}\n")
            file.write(f"Tiền kí túc xá: {tien_ki_tuc_xa}\n")
            file.write(f"Tiền xăng xe: {tien_xang_xe}\n")
            file.write(f"Tiền uống rượu: {tien_uong_ruou}\n")

    print("Nội dung file chi_tieu.txt:")
    # Mở file để đọc với encoding là utf-8
    with open('chi_tieu.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
def xoa_thong_tin_cau13():
    with open('chi_tieu.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    print("Nhập dòng muốn xóa (nhập 'exit' để kết thúc):")
    while True:
        line_number = input()
        if line_number.lower() == 'exit':
            break
        try:
            line_number = int(line_number)
            if 1 <= line_number <= len(lines):
                del lines[line_number - 1]
                print(f"Đã xóa dòng {line_number}.")
            else:
                print("Số dòng không hợp lệ.")
        except ValueError:
            print("Đầu vào không hợp lệ.")

    with open('chi_tieu.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)

    print("Nội dung file chi_tieu.txt sau khi xóa:")
    with open('chi_tieu.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
def menu():
   while True:
       print("===== MENU =====")
       print("1. Tạo tệp tin số ngẫu nhiên")
       print("2. Tạo một tệp tin văn bản mới có phần mở rộng là h5n")
       print("3. Thêm nhập và thêm bảng cửu chương vào tệp tin mới với tên file là bangCuuChuong.txt")
       print("4. Sao chép nội dung của một tệp tin văn bản câu 3 sang một tệp tin khác bất kỳ")
       print("5. Di chuyển một tệp tin từ thư mục này sang thư mục khác")
       print("6. Xóa một tệp tin khỏi một thư mục di chuyển ở câu 5")
       print("7. Kiểm tra thông tin tệp tin ở câu 3 và cho biết có bảng cửu chương 5 không")
       print("8. Đổi tên một tệp tin câu 1 thành tên yêu thích của em")
       print("9. Kiểm tra xem một tệp tin có tồn tại hay không")
       print("10. nhập tự động 100 số vào file và tìm xem số lớn nhất và nhỏ nhất và từ đó tính trung bình giữa chúng")
       print("11. Đọc và ghi dữ liệu vào một tệp tin CSV với thôn tin là hai cột và 2 dòng.")
       print("12. Nhập thông tin vào file và kiểm tra có tồn tại thông tin nào là email không? (Email có phần mở rộng là gmail.com).")
       print("13. Đưa toàn bộ thông tin về chi tiêu hàng tháng của em vào file, hãy đọc thông tin theo yêu cầu từ bàn phím.")
       print("14.  Xóa thông tin từ câu 13 theo yêu cầu.")
       print("16. Thoát")
       choice = input("Hãy Nhập Lựa Chọn Của Bạn: ")

       if choice == "1":
           tep_tin_so_ngau_nhien()
       elif choice == "2":
           tep_tin_van_ban_h5()
       elif choice == "3":
           nhap_bang_cuu_chuong()
       elif choice == "4":
           sao_chep_ND_vb()
       elif choice == "5":
           di_chuyen_tap_tin()
       elif choice == "6":
           xoa_nd()
       elif choice == "7":
           check_thong_tin_tep()
       elif choice == "8":
           ten_tep_yeu_thich()
       elif choice == "9":
           check_file_ton_tai()
       elif choice == "10":
           randon_100so()
       elif choice == "11":
           hai_hang()
       elif choice == "12":
           nhap_thong_tin_file()
       elif choice == "13":
           nhap_thong_tin_chi_tieu()
       elif choice == "14":
           xoa_thong_tin_cau13()
       elif choice == "16":
           print("Goodbye!")
           break
       else:
           print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

menu()


