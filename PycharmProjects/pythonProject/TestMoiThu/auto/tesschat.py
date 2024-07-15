import pyautogui
import time
"""
print("Di chuyển chuột đến vị trí cần lấy tọa độ và nhấn Ctrl+C để dừng lại.")

try:
    while True:
        # Lấy vị trí hiện tại của con trỏ chuột
        x, y = pyautogui.position()
        print(f"Tọa độ hiện tại của con trỏ chuột là: ({x}, {y})", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nĐã dừng.")"""


# Tọa độ của entry chat mà bạn đã lấy từ đoạn mã trên
entry_chat_x = 543  # Thay bằng tọa độ x thực tế
entry_chat_y = 877  # Thay bằng tọa độ y thực tế

# Click vào entry chat để focus
pyautogui.click(entry_chat_x, entry_chat_y)

# Đợi một chút trước khi bắt đầu gõ
time.sleep(0.4)

count = 0
while count < 100:
    # Gõ nội dung và nhấn enter
    pyautogui.typewrite("ahihi do ngoc")
    pyautogui.press("enter")
    count += 1
