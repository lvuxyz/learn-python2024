import re
with open('thong_tin.txt', 'w') as file:
    while True:
        info = input("Nhập thông tin (nhấn Enter để kết thúc): ")
        if not info:
            break
        file.write(info + '\n')

with open('thong_tin.txt', 'r') as file:
    content = file.read()
    email_pattern = r'\b[\w.-]+@gmail\.com\b'
    emails = re.findall(email_pattern, content)
    if emails:
        print("Các email trong file:")
        for email in emails:
            print(email)
    else:
        print("Không có email trong file.")