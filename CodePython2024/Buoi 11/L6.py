from tkinter import *
from PIL import Image, ImageTk

window = Tk()

image_label = Label(window)
image_label.pack()

gif_paths = ["meomeosung.gif", "meomeongu.gif", "meomeokis.gif"]

current_gif_index = 0

def load_gif(gif_path):
    gif = Image.open(gif_path)
    frames = []
    for frame in range(gif.n_frames):
        gif.seek(frame)
        frames.append(ImageTk.PhotoImage(gif))
    return frames

gif_frames = load_gif(gif_paths[current_gif_index])

def update(index):
    frame = gif_frames[index]
    image_label.configure(image=frame)
    window.after(50, update, (index + 1) % len(gif_frames))

if gif_frames:
    window.after(0, update, 0)
else:
    print("Không thể tải ảnh GIF.")

def next_gif():
    global current_gif_index, gif_frames
    current_gif_index = (current_gif_index + 1) % len(gif_paths)
    gif_frames = load_gif(gif_paths[current_gif_index])
    update(0)

next_button = Button(window, text="Next GIF", command=next_gif)
next_button.pack()

window.mainloop()