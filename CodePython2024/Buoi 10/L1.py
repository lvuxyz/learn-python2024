from tkinter import *
window = Tk()
window.title("form cua vu dz")
window.geometry("720x480")

label_nhap_a = Label(window, text="Nhập số a: ")
label_nhap_a.place(x=10, y = 20)

label_nhap_b = Label(window, text="Nhập số b: ")
label_nhap_b.place(x=10, y = 40)

label_ket_qua = Label(window, text="Kết quả: ")
label_ket_qua.place(x= 10, y = 60)

entry_nhap_a = Entry()
entry_nhap_a.place(x = 100, y= 20)

entry_nhap_b = Entry()
entry_nhap_b.place(x = 100, y = 40)

entry_ket_qua = Entry()
entry_ket_qua.place(x=100, y=40)

list_box = Listbox()
list_box.place(x = 250, y = 20)

button_cong = Button(window, text="+")
button_cong.place(x = 10, y = 80, width=100, height=25)

button_tru = Button(window, text="-")
button_tru.place(x = 100, y = 80, width=100, height=25)

button_nhan = Button(window, text="*")
button_nhan.place(x = 10, y = 120, width=100, height=25)

button_chia = Button(window, text="/")
button_chia.place(x = 100, y = 120, width=100, height=25)

button_thoat = Button(window, text="thoat")
button_thoat.place(x = 10, y = 200, width=100, height=25)

window.mainloop()