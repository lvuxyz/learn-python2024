def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua

with open("NgoLongVu.txt", "w", encoding='utf-8') as file:
    n = int(input("Nhập số tự nhiên n: "))
    giai_thua_n = tinh_giai_thua(n)
    file.write("Số tự nhiên n: " + str(n) + "\n")
    file.write("Giai thừa của số tự nhiên n là: " + str(giai_thua_n) + "\n")
    file.write("Giai thừa là: " + str(giai_thua_n) + "\n")