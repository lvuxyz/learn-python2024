# Hàm tính giai thừa của một số nguyên dương n
# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập số nguyên dương n: "))

giai_thua = 1
for i in range(1, n + 1):
     giai_thua *= i

print(f"giai thua cua {n} la:",giai_thua)