def menu():
    print("Chọn một tùy chọn:")
    print("1. Tính tổng số tiền mua gà vào mỗi mùa")
    print("2. Tính tổng và hiệu của các số chẵn và lẻ")
    print("3. Tính số lượng gà và chuột")
    print("4. Tính số lượng chó và gà")
    print("5. Chuyển đổi nhiệt độ C sang F và ngược lại")
    print("6. Kiểm tra năm nhuận và tính tuổi")
    print("7. Tìm ƯCLN và BCNN của 2 số")
    print("8. Chuyển đổi giữa hệ thập phân và nhị phân")
    print("9. Tìm giao điểm của 2 đường thẳng")
    print("10. Tìm số xuất hiện nhiều và ít nhất trong danh sách")
    print("11. Tìm số lớn thứ 2 và nhỏ thứ 2 trong một danh sách")
    print("12. Tính toán diện tích và chu vi các hình học khác như hình thang, hình bình hành")
    print("13. Tính tổng, tích, trung bình của các số trong một danh sách")
    print("14. Đọc số")
    print("15. Giải phương trình bậc nhất")
    print("16. Giải phương trình bậc hai")
    print("17. Kiểm tra một chuỗi có chứa chữ số hay không")
    print("18. Tìm số lớn nhất trong 3 số")
    print("19. Đảo ngược một chuỗi")
    print("20. Diện tích hình chữ nhật")
    print("21. In ra bảng cửu chương theo phong cách dí dỏm")
    print("0. Thoát")
    while True:
        try:
            chon = int(input("Nhập lựa chọn của bạn: "))
            if chon not in range(0, 22):
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 0 đến 21.")
                continue
            else:
                return chon
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập một số nguyên.")
def tinh_ga():
    so_ga = 250000
    gia_ga = 15000
    mua = {
        "Xuân": 1.15,
        "Hè": 0.90,
        "Thu": 1.25,
        "Đông": 0.60
    }
    tong = {}
    for season, factor in mua.items():
        tong[season] = so_ga * gia_ga * factor
    mua_v = min(tong, key=tong.get)
    print("Tổng chi phí mua gà vào mỗi mùa:")
    for season, cost in tong.items():
        print(f"{season}: {cost:.0f} VND")
    print(f"Mua gà vào mùa {mua_v} là hợp lý nhất với chi phí {tong[mua_v]:.0f} VND")
#2.Tính Tổng và Hiệu của các số chắn và số lẻ được nhập từ bàn phím với 10 số.
def tinh_tong_hieu():
    nhap_so = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(10)]
    tong_so_chan = sum(x for x in nhap_so if x % 2 == 0)
    tong_so_le = sum(x for x in nhap_so if x % 2 != 0)
    hieu = tong_so_chan - tong_so_le
    print(f"Tổng các số chẵn: {tong_so_chan}")
    print(f"Tổng các số lẻ: {tong_so_le}")
    print(f"Hiệu giữa tổng số chẵn và tổng số lẻ: {hieu}")
#3. Tính số lượng gà và chuột biết có tổng 50 con và 100 chân.
def tinh_ga_chuot():
    tong_ga_va_chuot = 50
    so_chan = 100
    for ga in range(tong_ga_va_chuot + 1):
        chuot = tong_ga_va_chuot - ga
        if ga * 2 + chuot * 4 == so_chan:
            print(f"Số lượng gà: {ga}, Số lượng chuột: {chuot}")
            return
    print("Không tìm thấy đáp án phù hợp")
#4.Tính số lượng Chó và Gà biết có Hiệu giữa chúng là 72 con và có 100 chân với Số Gà nhiều hơn Chó.
def cho_va_ga():
    total_legs = 100
    difference = 72
    for dogs in range((total_legs - 2 * difference) // 2 + 1):
        chickens = dogs + difference
        if chickens * 2 + dogs * 4 == total_legs:
            print(f"Số lượng gà: {chickens}, Số lượng chó: {dogs}")
            return
    print("Không tìm thấy đáp án phù hợp")
#5.Chuyển đổi nhiệt độ từ độ C sang độ F và ngược lại.
def chuyen_do_c_f():
    chon = input("Chọn (C) hoặc (F): ").strip().upper()
    if chon == "C":
        c = int(input("Nhập nhiệt độ C: "))
        f = c * 9/5 + 32
        print(f"Nhiệt độ Fahrenheit: {f:.2f}")
    elif chon == "F":
        f = int(input("Nhập nhiệt độ F: "))
        c = (f - 32) * 5/9
        print(f"Nhiệt độ C: {c:.2f}")
    else:
        print("Lựa chọn không hợp lệ")
#6.Kiểm tra xem một năm sinh của bạn có phải là năm nhuận hay không và cho biết tuổi của bạn.
def nam_sinh_va_tuoi():
    nam_sinh = int(input("Nhập năm sinh của bạn: "))
    chon_nam = 2024
    tuoi = chon_nam - nam_sinh
    is_leap = (nam_sinh % 4 == 0 and chon_nam % 100 != 0) or (nam_sinh % 400 == 0)
    print(f"Năm sinh của bạn {'là' if is_leap else 'không phải là'} năm nhuận")
    print(f"Tuổi của bạn là: {tuoi}")
#7.Tìm ước số chung lớn nhất và bội số chung nhỏ nhất của 2 số.
def gcd_and_lcm():
    import math
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    gcd = math.gcd(a, b)
    lcm = abs(a*b) // gcd
    print(f"Ước số chung lớn nhất của {a} và {b} là: {gcd}")
    print(f"Bội số chung nhỏ nhất của {a} và {b} là: {lcm}")
#8.Chuyển đổi giữa hệ thập phân sang nhị phân, và ngược lại.
def nhi_phan(so_thap_phan):
    if so_thap_phan == 0:
        return "0"

    so_nhi_phan = ""
    while so_thap_phan > 0:
        remainder = so_thap_phan % 2  # Tìm phần dư khi chia cho 2
        so_nhi_phan = str(remainder) + so_nhi_phan  # Thêm phần dư vào trước chuỗi kết quả
        so_thap_phan = so_thap_phan // 2  # Lấy phần nguyên của phép chia cho 2

    return so_nhi_phan
so_thap_phan = 10
so_nhi_phan = nhi_phan(so_thap_phan)
print(f"Số thập phân {so_thap_phan} chuyển sang nhị phân là {so_nhi_phan}")

#9.Viết chương trình tìm giao điểm của 2 đường thẳng
def giao_diem():
    print("Đường thẳng thứ nhất: y = m1*x + b1")
    m1 = float(input("Nhập m1: "))
    b1 = float(input("Nhập b1: "))
    print("Đường thẳng thứ hai: y = m2*x + b2")
    m2 = float(input("Nhập m2: "))
    b2 = float(input("Nhập b2: "))
    if m1 == m2:
        if b1 == b2:
            print("Hai đường thẳng trùng nhau")
        else:
            print("Hai đường thẳng song song, không có giao điểm")
    else:
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        print(f"Giao điểm của hai đường thẳng: ({x:.2f}, {y:.2f})")
#10.Tìm số xuất hiện nhiều và ít nhất trong một danh sách.
def nhieu_it():
    so = int(input("Nhập số lượng phần tử trong danh sách: "))
    lst = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(so)]
    from collections import Counter  # Sử dụng đúng thư viện collections
    counter = Counter(lst)
    nhieu_nhat = counter.most_common(1)[0]
    it_nhat = counter.most_common()[-1]
    print(f"Số xuất hiện nhiều nhất: {nhieu_nhat[0]} với {nhieu_nhat[1]} lần")
    print(f"Số xuất hiện ít nhất: {it_nhat[0]} với {it_nhat[1]} lần")
#11. Tìm số lớn thứ 2 và nhỏ thứ 2 trong một danh sách.
def so_lon_so_nho(numbers):
    if len(numbers) < 2:
        return None, None
    numbers_duy_nhat = list(set(numbers))
    if len(numbers_duy_nhat) < 2:
        return None, None
    numbers_duy_nhat.sort()
    return numbers_duy_nhat[-2], numbers_duy_nhat[1]

#12. Tính toán diện tích và chu vi các hình học khác như hình thang, hình bình hành.
def dien_tich_hcm_hbh():
    hinh = input("Nhập loại hình (1 là hình thang, 2 là hình chữ nhật): ")
    if hinh == "1":
        a = int(input("Nhập cạnh đáy lớn: "))
        b = int(input("Nhập cạnh đáy nhỏ: "))
        h = int(input("Nhập chiều cao: "))
        dien_tich = (a + b) * h / 2
        chu_vi = a + b + (((a - b) ** 2 + h ** 2) ** 0.5) * 2
    elif hinh == "2":
        a = int(input("Nhập chiều dài: "))
        b = int(input("Nhập chiều rộng: "))
        dien_tich = a * b
        chu_vi = 2 * (a + b)
    else:
        print("Loại hình không hợp lệ")
        return
    print(f"Diện tích: {dien_tich}, Chu vi: {chu_vi}")
#13. Viết chương trình tính tổng, tích, trung bình của các số trong một danh sách.
def trung_binh_ds(numbers):
    tong = sum(numbers)
    so_ds = 1
    for num in numbers:
        so_ds *= num
    trung_binh = tong / len(numbers)
    return tong, so_ds, trung_binh
#14. Viết chương trình đọc số, ví dụ nhập 1 hiển thị là Một (sử dụng switch).
def doc_so():
    nhap_so = int(input("Nhập số: "))
    so = {
        0: "Không", 1: "Một", 2: "Hai", 3: "Ba", 4: "Bốn", 5: "Năm",
        6: "Sáu", 7: "Bảy", 8: "Tám", 9: "Chín"
    }
    chu = ""
    for digit in str(nhap_so):
        chu += so[int(digit)] + " "
    print(chu.strip())
#15. Viết chương trình để giải bậc nhất
def giai_phuong_trinh_b1():
    a = int(input("Nhập hệ số a: "))
    b = int(input("Nhập hằng số b: "))
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print("Nghiệm của phương trình là: ", x)
#16. Viết chương trình để giải phương trình bậc 2
def giai_phuong_trinh_b2():
    a = int(input("Nhập hệ số a: "))
    b = int(input("Nhập hệ số b: "))
    c = int(input("Nhập hằng số c: "))
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phương trình có nghiệm kép: {x}")
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
#17.Kiểm tra một chuỗi có chứa chữ số hay không
def chua_chu_so(string):
    for char in string:
        if char.isdigit():
            return True
    return False

nhap = input("Nhập một chuỗi: ")
if chua_chu_so(nhap):
    print(f"Chuỗi '{nhap}' chứa chữ số")
else:
    print(f"Chuỗi '{nhap}' không chứa chữ số")
#18Tìm số lớn nhất trong 3 số
def toi_da(a, b, c):
    return max(a, b, c)

a = float(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
lon_nhat = toi_da(a, b, c)
print(f"Số lớn nhất trong {a}, {b}, {c} là: {lon_nhat}")
#19. Đảo ngược một chuỗi
def dao_nguoc(nhap_chuoi):
    return nhap_chuoi[::-1]

nhap_chuoi = input("Nhập một chuỗi: ")
dao_nguoc = dao_nguoc(nhap_chuoi)
print(f"Chuỗi đảo ngược: {dao_nguoc}")
#20. diện tích hình chữ nhật
def dien_tich_hcn(dai, rong):
    return dai * rong
dai = int(input("Nhập chiều dài hình chữ nhật: "))
rong = int(input("Nhập chiều rộng hình chữ nhật: "))
dien_tích = dien_tich_hcn(dai, rong)
print(f"Diện tích hình chữ nhật là: {dien_tích}")
#21. in ra bảng cửu chương theo phong cách dí dỏm
def bang_cuu_chuong(num):
    print(f"Cửu chương của {num} là như sau:")
    for i in range(1, 11):
        result = num * i
        print(f"{num} quả cóc, {i} con vịt, hỏi có bao nhiêu cái...")
        print(f"Đáp: {result} cái!")
        print("Hì hì hì...")

print("Hãy nhập một con số từ 1 đến 9, tôi sẽ đọc cửu chương cho bạn!")
num = int(input("Nhập số: "))

if num < 1 or num > 9:
    print("Bạn phải nhập một số từ 1 đến 9!")
else:
    bang_cuu_chuong(num)

while True:
    choice = menu()
    if choice == 0:
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
    elif choice == 1:
        tinh_ga()
    elif choice == 2:
        tinh_tong_hieu()
    elif choice == 3:
        tinh_ga_chuot()
    elif choice == 4:
        cho_va_ga()
    elif choice == 5:
        chuyen_do_c_f()
    elif choice == 6:
        nam_sinh_va_tuoi()
    elif choice == 7:
        gcd_and_lcm()
    elif choice == 8:
        so_thap_phan = int(input("Nhập số thập phân: "))
        so_nhi_phan = nhi_phan(so_thap_phan)
        print(f"Số thập phân {so_thap_phan} chuyển sang nhị phân là {so_nhi_phan}")
    elif choice == 9:
        giao_diem()
    elif choice == 10:
        nhieu_it()
    elif choice == 11:
        numbers = [int(x) for x in input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()]
        second_largest, second_smallest = so_lon_so_nho(numbers)
        if second_largest is None or second_smallest is None:
            print("Danh sách không đủ các số khác nhau để tìm số lớn thứ 2 và nhỏ thứ 2")
        else:
            print(f"Số lớn thứ 2 là: {second_largest}, Số nhỏ thứ 2 là: {second_smallest}")
    elif choice == 12:
        dien_tich_hcm_hbh()
    elif choice == 13:
        numbers = [int(x) for x in input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()]
        total, product, average = trung_binh_ds(numbers)
        print(f"Tổng: {total}, Tích: {product}, Trung bình: {average}")
    elif choice == 14:
        doc_so()
    elif choice == 15:
        giai_phuong_trinh_b1()
    elif choice == 16:
        giai_phuong_trinh_b2()
    elif choice == 17:
        chua_chu_so()
    elif choice == 18:
        toi_da()
    elif choice == 19:
        dao_nguoc()
    elif choice == 20:
        dien_tich_hcn()
    elif choice == 21:
        bang_cuu_chuong()