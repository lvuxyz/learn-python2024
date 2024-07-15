with open("bangCuuChuong.txt", "r") as f:
    content = f.read()
    if "5 x 5 = 25" in content:
        print("Tệp tin có bảng cửu chương 5")
    else:
        print("Tệp tin không có bảng cửu chương 5")