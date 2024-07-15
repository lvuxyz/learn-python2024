with open("NgoLongVu.txt", "w", encoding='utf-8')as file:
    ho_ten = input("Nhập họ tên của bạn: ")
    age = input("Nhập tuổi của bạn: ")
    dia_chi = input("Nhập địa chỉ của bạn: ")

    file.write("Họ tên: "+ ho_ten + "\n")
    file.write("Tuổi: " + age + "\n")
    file.write("Địa chỉ: " + dia_chi + "\n")

with open("NgoLongVu.txt", "r", encoding='utf-8')as file:
    ky_tu = file.read()
    so_ky_tu = len(ky_tu)
with open("NgoLongVu.txt", "a", encoding='utf-8')as file:
    file.write("Số Kí tự: " +str(so_ky_tu)+ "\n")