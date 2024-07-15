# chu vi , dien tixch hình tròn, tam giác
import math
# Chu vi và diện tích hình tròn
try:
    r = int(input("Nhập vào bán kính của hình tròn: "))
    if r > 0:
      pi = math.pi
# Tính chu vi hình tròn
    chu_vi_hinh_tron = 2 * pi * r
    print(f"Chu vi hình tròn là: {chu_vi_hinh_tron}")
    # Tính diện tích hình tròn
    dien_tich_hinh_tron = pi * r ** 2
    print(f"Diện tích hình tròn là: {dien_tich_hinh_tron}")
except:
    print("Vui lòng nhập r lớn hơn 0")
# chu vi và diện tích tam giac
try:
    a = int(input("Nhap vao canh a: "))
    b = int(input("Nhap vao canh b: "))
    c = int(input("Nhap vao canh c: "))
    if (a > 0) and ( b > 0) and ( c >0) and (a + b >c) and (b  + c>a) and (a +c>b):
        cv = a + b + c
        p = cv / 2
        dt = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print("CHu vi tam giac la", cv)
        print("Dien tich tam giac la",dt)
except:
    print("Vui lòng nhập cạnh tam giác hợp lý")


