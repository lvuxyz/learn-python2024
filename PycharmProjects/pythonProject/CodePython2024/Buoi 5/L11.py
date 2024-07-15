import os

if not os.path.exists("NgoLongVu1.txt"):
    noi_dung_bai_tho = input("File NgoLongVu1.txt không tồn tại. Vui lòng nhập nội dung của một bài thơ:\n")
    with open("NgoLongVu1.txt", "w", encoding='utf-8') as file:
        file.write(noi_dung_bai_tho)
else:
    with open("NgoLongVu1.txt", "r", encoding='utf-8') as file:
        noi_dung_bai_tho = file.read()
        print("Nội dung của bài thơ trong file poem.txt:")
        print(noi_dung_bai_tho)
