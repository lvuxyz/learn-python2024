#  Nhập vào một danh sách và cho biết danh sách đó có bao nhiêu số lẻ và số chẵn?
danhsach = input("Nhập danh sách các số: ").split()

so_chan = 0
so_le = 0

for so in danhsach:
    if int(so) % 2 == 0:
        so_chan += 1
    else:
        so_le += 1

print("Số chẵn có trong danh sách:", so_chan)
print("Số lẻ có trong danh sách:", so_le)
