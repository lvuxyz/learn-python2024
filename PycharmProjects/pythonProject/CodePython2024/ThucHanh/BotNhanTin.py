'''import pyautogui
import pyperclip
import time

# Đoạn text bạn muốn gửi, có thể thay đổi để gửi các ký tự tiếng Việt
message = "Xin chào, đây là tin nhắn tự động bằng tiếng Việt."
# Số lần bạn muốn gửi tin nhắn
repeat = 5
# Khoảng thời gian chờ giữa mỗi lần gửi (giây)
interval = 2

# Chờ 5 giây để bạn có thời gian chọn cửa sổ chat
print("Bạn có 5 giây để chọn cửa sổ chat.")
time.sleep(5)

for _ in range(repeat):
    pyperclip.copy(message)  # Sao chép tin nhắn vào clipboard
    pyautogui.hotkey('ctrl', 'v')  # Dán tin nhắn từ clipboard
    pyautogui.press('enter')
    time.sleep(interval)
'''

import pyautogui
import pyperclip
import time

# Đoạn text cơ bản bạn muốn gửi
base_message = "Xin chào, đây là tin nhắn tự động bằng tiếng Việt."
# Số lần bạn muốn gửi tin nhắn
repeat = 5
# Khoảng thời gian chờ giữa mỗi lần gửi (giây)
interval = 2

# Chờ 5 giây để bạn có thời gian chọn cửa sổ chat
print("Bạn có 5 giây để chọn cửa sổ chat.")
time.sleep(5)

for i in range(1, repeat + 1):
    message = f"{i}. {base_message}"  # Thêm số thứ tự vào đầu tin nhắn
    pyperclip.copy(message)  # Sao chép tin nhắn vào clipboard
    pyautogui.hotkey('ctrl', 'v')  # Dán tin nhắn từ clipboard
    pyautogui.press('enter')
    time.sleep(interval)
