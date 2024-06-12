with open("NgoLongVu.txt", "w", encoding='utf-8') as file:
    nhap_so = input("Nhập dãy số: ").split()
    for so in nhap_so:
        file.write(so + "\n")

tong_so_chan = 0
tong_so_le = 0
tich_so_chan = 1
tich_so_le = 1

with open("NgoLongVu.txt", "r", encoding='utf-8') as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            tong_so_chan += number
            tich_so_chan *= number
        else:
            tong_so_le += number
            tich_so_le *= number

with open("NgoLongVu.txt", "a", encoding='utf-8') as file:
    file.write("Tổng các số chẵn là: " + str(tong_so_chan) + "\n")
    file.write("Tích các số chẵn là: " + str(tich_so_chan) + "\n")
    file.write("Tổng các số lẻ là: " + str(tong_so_le) + "\n")
    file.write("Tích các số lẻ là: " + str(tich_so_le) + "\n")
