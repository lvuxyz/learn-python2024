'''Nhập vào một Dictionary các phần tử.
- Thêm phần tử vào Dictionary
- Xóa phần tử từ Dictionary
- Thay thế phần tử từ Dictionary
- Sắp xếp phần tử theo key của Dictionary'''
dictionary = {}

def them_phan_tu():
    key = input("Nhập key của phần tử: ")
    value = input("Nhập value của phần tử: ")
    dictionary[key] = value

def xoa_phan_tu():
    key = input("Nhập key của phần tử bạn muốn xóa: ")
    if key in dictionary:
        del dictionary[key]
        print("Danh sách sau khi xóa:", dictionary)
    else:
        print("Không có phần tử có key là '{}' trong Dictionary.".format(key))

def thay_the_phan_tu():
    key = input("Nhập key của phần tử bạn muốn thay thế: ")
    if key in dictionary:
        new_value = input("Nhập giá trị mới cho phần tử: ")
        dictionary[key] = new_value
        print("Danh sách sau khi thay thế:", dictionary)
    else:
        print("Không có phần tử có key là '{}' trong Dictionary.".format(key))

def sap_xep():
    sorted_dict = dict(sorted(dictionary.items()))
    print("Danh sách sau khi sắp xếp theo key của Dictionary:", sorted_dict)

while True:
    print("\nChọn chức năng:")
    print("1. Thêm phần tử vào Dictionary")
    print("2. Xóa phần tử từ Dictionary")
    print("3. Thay thế phần tử từ Dictionary")
    print("4. Sắp xếp phần tử theo key của Dictionary")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")

    if choice == '1':
        them_phan_tu()
    elif choice == '2':
        xoa_phan_tu()
    elif choice == '3':
        thay_the_phan_tu()
    elif choice == '4':
        sap_xep()
    elif choice == '5':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

