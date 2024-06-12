#Viết chương trình chuyển đôi qua lại giữ Km -> mm

print("1. Km -> mm")
print("2. Mm -> km")
print("3. km -> m")
print("4. m -> km")
print("5. cm -> m")
while True:
    choice = int(input("Nhập lựa chọn: "))

    if choice == 1:
        km = float(input("Nhập số kilomet cần chuyển đổi: "))
        mm = float(km * 1000000)
        print(f"{km} kilomet = {mm} milimét")
    elif choice == 2:
        mm_input = float(input("Nhập số milimét cần chuyển đổi: "))
        mm = mm_input /1000000
        print(f"{mm_input} milimét = {mm} kilomet")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")