danh_sach = []
with open("NgoLongVu.txt", "w", encoding='utf-8') as file:
    file.write("Nhập danh sách thư mời:\n")

    while True:
        khach_moi = input("Nhập tên khách mời: ")
        if not khach_moi:
            break
        file.write(f"- {khach_moi}\n")
        danh_sach.append(khach_moi)

    print("Danh sách thư mời:")
    for khach_moi in danh_sach:
        print(f"- {khach_moi}")

    danh_sach_xoa = input("Nhập tên thành viên muốn xóa khỏi thư mời: ")
    if danh_sach_xoa in danh_sach:
        danh_sach.remove(danh_sach_xoa)
        file.write(f"\nĐã xóa ({danh_sach_xoa}) khỏi danh sách thư mời.\n")
        print(f"Đã xóa {danh_sach_xoa} khỏi danh sách thư mời.")
    else:
        file.write(f"\n{danh_sach_xoa} không có trong danh sách thư mời.\n")
        print(f"{danh_sach_xoa} không có trong danh sách thư mời.")

    file.write("\nDanh sách thư mời sau khi xóa:\n")
    for khach_moi in danh_sach:
        file.write(f"- {khach_moi}\n")

print("Hoàn thành việc cập nhật danh sách thư mời.")

