import os
check_file = "Vudeptrai.txt"
if os.path.isfile(check_file):
    print(f"Tệp tin {check_file} tồn tại")
else:
    print(f"Tệp tin {check_file} không tồn tại")