#Câu 2: Nhập một danh sách các phần tử (nhập số), và tính tổng và tích của các phần tử đó.
danh_sach = input("Nhap danh sach cac phan tu: ")
danh_sach = [int(x) for x in danh_sach.split()]

tong = sum(danh_sach)
tich = 1
for num in danh_sach:
    tich *= num

print("Tong cac phan tu:", tong)
print("Tich cac phan tu:", tich)
