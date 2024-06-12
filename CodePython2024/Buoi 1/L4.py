"""nhap vao cac canh cua tu giac, tinh chu vi, dien tich cua tu giac do"""
a = int(input("Nhập vào cạnh a: "))
b = int(input("Nhập vào cạnh b: "))
c = int(input("Nhập vào cạnh c: "))
d = int(input("Nhập vào cạnh d: "))
ah = int(input("Nhập vào đường cao AH từ đỉnh A đến đường AB: "))

chu_vi = a + b + c + d
print("Chu vi của tứ giác là:", chu_vi)

dien_tich = a * ah
print("Diện tích của tứ giác là:", dien_tich)
