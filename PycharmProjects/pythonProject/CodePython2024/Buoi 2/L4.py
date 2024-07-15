#Câu 4: Nhập vào số tự nhiên a từ 1-10, hiển thị bảng cửu chương của nó.
a = int(input("nhap so tu nhien tu 1 den 10: "))
if a < 1 or a > 10:
    print("So khong nam trong khoang tu 1 den 10.")
else:
    print("Bang cuu chuong cua", a, ":")
    for i in range(11):
        print(a, "x", i,"=", a * i)
