a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))

chu_vi = a + b + c
print("Chu vi cua tam giac la:", chu_vi)

p = chu_vi / 2
dien_tich = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print("Dien tich cua tam giac la:", dien_tich)
