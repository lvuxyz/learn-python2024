# 13. Đưa toàn bộ thông tin về chi tiêu hàng tháng của em vào file, hãy đọc thông tin theo yêu cầu từ bàn phím
with open('chi_tieu.txt', 'w') as file:
    print("Nhập thông tin chi tiêu hàng tháng (nhấn Enter để kết thúc):")
    while True:
        chi_tieu = input()
        if not chi_tieu:
            break
        file.write(chi_tieu + '\n')

print("Nội dung file chi_tieu.txt:")
with open('chi_tieu.txt', 'r') as file:
    content = file.read()
    print(content)