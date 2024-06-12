with open("NgoLongVu.txt", "w", encoding='utf-8') as file:
    nhap_a = int(input("Nhập số a: "))
    nhap_b = int(input("Nhập số b: "))
    tinh_tong = nhap_a + nhap_b
    tinh_hieu = nhap_a - nhap_b
    tinh_tich = nhap_a * nhap_b
    tinh_thuong = nhap_a / nhap_b

    file.write('Tổng của 2 số là: ' + str(tinh_tong) + '\n')
    file.write('Hiệu của 2 số là: ' + str(tinh_hieu) + '\n')
    file.write('Tích của 2 số là: ' + str(tinh_tich) + '\n')
    file.write('Thương của 2 số là: ' + str(tinh_thuong) + '\n')
