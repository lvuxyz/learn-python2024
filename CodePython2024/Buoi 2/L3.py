'''Câu 3: Nhập vào một list các phần tử.
- Thêm phần tử vào danh sách
- Xóa phần tử từ danh sách
- Thay thế phần tử từ danh sách
- Sắp xếp phần tử'''
li = []
danh_sach = input("Ban hay nhap phan tu bat ki: ")
li = danh_sach.split()
add = input("Ban muon them phan tu gi? ")
loca = int(input("Chon vi tri ban muon them (0-{}): ".format(len(li))))
li.insert(loca, add)
print(li)

dele = input("Ban muon xoa phan tu nao: ")
if dele in li:
    li.remove(dele)
    print("Danh sach sau khi xoa: ", li)
else:
    print("Khong co trong danh sach: ")

thay = int(input("Ban muon thay the phan tu nao?(0-{}): ".format(len(li)-1)))
thay_the = input("Ban hay nhap phan tu muon thay: ")
li[thay] = thay_the
print("Danh sach sau khi thay the", li)

li2 = list(map(int, li))
li2.sort()
print("Danh sach sau khi sap xep: ", li2)