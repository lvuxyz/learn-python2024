diem_sinh_vien = []
for i in range(5):
    ten_sinh_vien = input(f"Nhập tên sinh viên {i+1}: ")
    diem = []
    for j in range(5):
        diem_mon = float(input(f"Nhập điểm môn {j+1} của {ten_sinh_vien}: "))
        diem.append(diem_mon)
    diem_sinh_vien.append((ten_sinh_vien, diem))

with open("NgoLongVu.txt", "w", encoding='utf-8') as file:
    file.write("Tính điểm trung bình của các sinh viên \n")
    file.write("Bảng điểm sinh viên: \n")

    diem_trung_binh_cao_nhat = 0
    diem_trung_binh_thap_nhat = float('inf')
    sinh_vien_cao_nhat = ""
    sinh_vien_thap_nhat = ""

    for sinh_vien, diem in diem_sinh_vien:
        tong_diem = sum(diem)
        diem_trung_binh = tong_diem / 5
        file.write(f"{sinh_vien}: Tổng điểm={tong_diem}, Điểm trung bình={diem_trung_binh:.2f}\n")
        if diem_trung_binh > diem_trung_binh_cao_nhat:
            diem_trung_binh_cao_nhat = diem_trung_binh
            sinh_vien_cao_nhat = sinh_vien
        if diem_trung_binh < diem_trung_binh_thap_nhat:
            diem_trung_binh_thap_nhat = diem_trung_binh
            sinh_vien_thap_nhat = sinh_vien

    file.write(f"\nSinh viên có điểm trung bình cao nhất: {sinh_vien_cao_nhat} ({diem_trung_binh_cao_nhat:.2f}) \n")
    file.write(f"Sinh viên có điểm trung bình thấp nhất: {sinh_vien_thap_nhat} ({diem_trung_binh_thap_nhat:.2f}) \n \n")

print("Hoàn thành việc tính toán và ghi kết quả.")
