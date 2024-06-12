import os
import shutil

new_name = "thu_muc_chuyen.txt"
thu_mucms = "file_1"
os.makedirs(thu_mucms)

shutil.move("Vudeptrai.txt", os.path.join(thu_mucms, new_name))
print(f"Đã di chuyển tệp tin {new_name} vào thư mục {thu_mucms}")
