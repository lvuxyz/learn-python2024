import random

with open("file_100_so.txt", 'w', encoding='utf-8') as file:
    so_tu_dong = [random.randint(1, 1000) for _ in range(100)]
    for num in so_tu_dong:
        file.write(str(num) + "\n")

with open("file_100_so.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]
    lon_nhat = max(numbers)
    nho_nhat = min(numbers)
    trung_binh = sum(numbers) / len(numbers)

    print(f"Số lớn nhất: {lon_nhat}")
    print(f"Số nhỏ nhất: {nho_nhat}")
    print(f"Trung bình: {trung_binh}")
