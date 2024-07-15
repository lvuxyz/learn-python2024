import random
with open("NgoLongVu.txt", "w", encoding='utf-8') as file:
    day_so = [random.randint(1, 100) for _ in range(10)]
    file.write(" ".join(map(str, day_so)))

with open("NgoLongVu.txt", "r", encoding='utf-8') as file:
    noi_dung = file.read()
    cac_so = list(map(int, noi_dung.split()))
    tong = sum(cac_so)
    print(f"Nội dung của file: {noi_dung}")
    print(f"Tổng các số trong dãy số: {tong}")
