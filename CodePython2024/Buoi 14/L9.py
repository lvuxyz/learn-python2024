import csv

filename = input("Nhập tên file (.csv): ")

with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)

    while True:
        name = input("Nhập tên (nhấn Enter để dừng): ")
        if not name:
            break

        age = input("Nhập tuổi: ")

        writer.writerow([name, age])

print(f"Dữ liệu đã được lưu vào file {filename}")
