from tkinter import *
from PIL import ImageTk, Image
import itertools

window = Tk()
window.geometry("1080x720")
window.title("from cua vu dep trai")
window.configure(background="yellow")

data_list = []
gif_paths = ["meomeosung.gif"]

meomeo_gif = Image.open("meomeosung.gif")
meomeo_frames = []

for frame in range(meomeo_gif.n_frames):
    meomeo_gif.seek(frame)
    meomeo_frames.append(ImageTk.PhotoImage(meomeo_gif))

def animate_meomeo(delay=50):
    global meomeo_frames, meomeo_iter
    try:
        meomeo_label.configure(image=next(meomeo_iter))
    except StopIteration:
        meomeo_iter = itertools.cycle(meomeo_frames)
        meomeo_label.configure(image=next(meomeo_iter))
    window.after(delay, animate_meomeo)

def add_to_list():
    value = entry_text.get()
    if value:
        data_list.append(value)
        list_danh_sach.insert(END, value)
        entry_text.delete(0, END)

def clear_list():
    data_list.clear()
    list_danh_sach.delete(0, END)

def save_list():
    with open("data.txt", "w") as file:
        for item in data_list:
            file.write(item + "\n")

def exit_program():
    window.quit()

tien_anh_image = ImageTk.PhotoImage(Image.open("tienanh.jpg"))
chien_anh_image = ImageTk.PhotoImage(Image.open("chien.jpg"))
tung_duong_image = ImageTk.PhotoImage(Image.open("tungduong.png"))
trung_dung_image = ImageTk.PhotoImage(Image.open("trungdung.jpg"))
tien_dat_image = ImageTk.PhotoImage(Image.open("tiendat.jpg"))

con_cho = ImageTk.PhotoImage(Image.open("concho.png"))
con_meo = ImageTk.PhotoImage(Image.open("conmeo.png"))
con_ca = ImageTk.PhotoImage(Image.open("conca.png"))

image_dict = {
    "Tiến anh": tien_anh_image,
    "Huy Chiến": chien_anh_image,
    "Tùng Dương": tung_duong_image,
    "Trung Dũng": trung_dung_image,
    "Tiến Đạt": tien_dat_image,
}

image_label = None

def show_image(option):
    global image_label

    if image_label:
        image_label.destroy()

    if option in image_dict:
        image_label = Label(window, image=image_dict[option])
        image_label.place(x=20, y=300)

def show_dog_picture():
    global image_label

    if image_label:
        image_label.destroy()

    image_label = Label(window, image=con_cho)
    image_label.place(x=20, y=300)

def show_cat_picture():
    global image_label

    if image_label:
        image_label.destroy()

    image_label = Label(window, image=con_meo)
    image_label.place(x=20, y=300)

def show_fish_picture():
    global image_label

    if image_label:
        image_label.destroy()

    image_label = Label(window, image=con_ca)
    image_label.place(x=20, y=300)

label_ten = Label(window, text="Enter a number:")
label_ten.place(x=10, y=20)

label_danh_sach = Label(window, text="Lists:")
label_danh_sach.place(x=10, y=60)

entry_text = Entry(window)
entry_text.place(x=100, y=20)

list_danh_sach = Listbox(window)
list_danh_sach.place(x=100, y=60)

button_add = Button(window, text="Add to list", command=add_to_list)
button_add.place(x=300, y=20, width=100, height=25)

button_clear = Button(window, text="Clear list", command=clear_list)
button_clear.place(x=300, y=60, width=100, height=25)

button_save = Button(window, text="Save list", command=save_list)
button_save.place(x=300, y=100, width=100, height=25)

button_exit = Button(window, text="Exit", command=exit_program)
button_exit.place(x=300, y=140, width=100, height=25)

select_anh = StringVar(window)
select_anh.set("Chọn ảnh của bạn bè")
nameList = OptionMenu(window, select_anh, "Tiến anh", "Huy Chiến", "Tùng Dương", "Trung Dũng", "Tiến Đạt")
nameList.place(x=30, y=250)

button_hien_anh = Button(window, text="Open ảnh", command=lambda: show_image(select_anh.get()))
button_hien_anh.place(x=200, y=250)

button_anh_con_cho = Button(window, text="Open Picture Dog", command=show_dog_picture)
button_anh_con_cho.place(x=380, y=250)

button_anh_con_meo = Button(window, text="Open Picture Cat", command=show_cat_picture)
button_anh_con_meo.place(x=500, y=250)

button_anh_con_ca = Button(window, text="Open Picture Fish", command=show_fish_picture)
button_anh_con_ca.place(x=620, y=250)

meomeo_label = Label(window)
meomeo_label.place(x=20, y=300)

meomeo_iter = itertools.cycle(meomeo_frames)

button_anh_con_meo = Button(window, text="Open Picture Cat", command=animate_meomeo)
button_anh_con_meo.place(x=500, y=250)

window.mainloop()