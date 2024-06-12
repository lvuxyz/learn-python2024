'''def menu():
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
    print("0. Thoát")
    chon = int(input("Nhập lựa chọn của bạn: "))
    return chon
#1
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
#2
def tinh_tong_hieu():
    nhap_so = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(10)]
    tong_so_chan = sum(x for x in nhap_so if x % 2 == 0)
    tong_so_le = sum(x for x in nhap_so if x % 2 != 0)
    hieu = tong_so_chan - tong_so_le
    print(f"Tổng các số chẵn: {tong_so_chan}")
    print(f"Tổng các số lẻ: {tong_so_le}")
    print(f"Hiệu giữa tổng số chẵn và tổng số lẻ: {hieu}")

#3
def tinh_ga_chuot():
    tong_ga_va_chuot = 50
    so_chan = 100
    for ga in range(tong_ga_va_chuot + 1):
        chuot = tong_ga_va_chuot - ga
        if ga * 2 + chuot * 4 == so_chan:
            print(f"Số lượng gà: {ga}, Số lượng chuột: {chuot}")
            return
    print("Không tìm thấy đáp án phù hợp")
#4
def dogs_and_chickens():
    total_legs = 100
    difference = 72
    for dogs in range((total_legs - 2 * difference) // 2 + 1):
        chickens = dogs + difference
        if chickens * 2 + dogs * 4 == total_legs:
            print(f"Số lượng gà: {chickens}, Số lượng chó: {dogs}")
            return
    print("Không tìm thấy đáp án phù hợp")
#5
def celsius_fahrenheit_conversion():
    choice = input("Chọn (C->F) hoặc (F->C): ").strip().upper()
    if choice == "C->F":
        c = float(input("Nhập nhiệt độ Celsius: "))
        f = c * 9/5 + 32
        print(f"Nhiệt độ Fahrenheit: {f:.2f}")
    elif choice == "F->C":
        f = float(input("Nhập nhiệt độ Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"Nhiệt độ Celsius: {c:.2f}")
    else:
        print("Lựa chọn không hợp lệ")
#6
def leap_year_and_age():
    birth_year = int(input("Nhập năm sinh của bạn: "))
    current_year = 2024  # Cập nhật năm hiện tại nếu cần
    age = current_year - birth_year
    is_leap = (birth_year % 4 == 0 and birth_year % 100 != 0) or (birth_year % 400 == 0)
    print(f"Năm sinh của bạn {'là' if is_leap else 'không phải là'} năm nhuận")
    print(f"Tuổi của bạn là: {age}")
#7
def gcd_and_lcm():
    import math
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    gcd = math.gcd(a, b)
    lcm = abs(a*b) // gcd
    print(f"Ước số chung lớn nhất của {a} và {b} là: {gcd}")
    print(f"Bội số chung nhỏ nhất của {a} và {b} là: {lcm}")
#8
def nhi_phan(so_thap_phan):
    if so_thap_phan == 0:
        return "0"

    so_nhi_phan = ""
    while so_thap_phan > 0:
        remainder = so_thap_phan % 2
        so_nhi_phan = str(remainder) + so_nhi_phan
        so_thap_phan = so_thap_phan // 2

    return so_nhi_phan

# Thêm giá trị khi gọi hàm
so_thap_phan = int(input("Nhập số thập phân: "))
so_nhi_phan = nhi_phan(so_thap_phan)
print(f"Số thập phân {so_thap_phan} chuyển sang nhị phân là {so_nhi_phan}")

#9
def line_intersection():
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
#10
def most_and_least_frequent():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    lst = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
    from collections import Counter
    counter = Counter(lst)
    most_common = counter.most_common(1)[0]
    least_common = counter.most_common()[-1]
    print(f"Số xuất hiện nhiều nhất: {most_common[0]} với {most_common[1]} lần")
    print(f"Số xuất hiện ít nhất: {least_common[0]} với {least_common[1]} lần")

while True:
    choice = menu()
    if choice == 1:
        tinh_ga()
    elif choice == 2:
        tinh_tong_hieu()
    elif choice == 3:
        tinh_ga_chuot()
    elif choice == 4:
        dogs_and_chickens()
    elif choice == 5:
        celsius_fahrenheit_conversion()
    elif choice == 6:
        leap_year_and_age()
    elif choice == 7:
        gcd_and_lcm()
    elif choice == 8:
        so_thap_phan = int(input("Nhập số thập phân: "))  # Nhập số thập phân từ người dùng
        nhi_phan(so_thap_phan)  # Truyền số thập phân vào hàm nhi_phan()
    elif choice == 9:
        line_intersection()
    elif choice == 10:
        most_and_least_frequent()
    elif choice == 0:
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")'''
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

while True:
    choice = int(input("Nhập số 4 để tính số lượng Chó và Gà: "))
    if choice == 4:
        cho_va_ga()
        break
