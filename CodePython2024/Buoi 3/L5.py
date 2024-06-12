#Tìm số lớn nhất trong 3 số được nhập từ bàn phím

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

max_num = a

if b > max_num:
    max_num = b

if c > max_num:
    max_num = c

print(f"Số lớn nhất trong ba số là: {max_num}")
