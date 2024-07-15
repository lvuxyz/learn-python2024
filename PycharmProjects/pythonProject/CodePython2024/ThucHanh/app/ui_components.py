from tkinter import Frame, Canvas, Button, Entry, PhotoImage, BOTH
from pathlib import Path

# Đường dẫn tới thư mục chứa tài nguyên
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path

class MainFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#F9F9F9")
        self.canvas = Canvas(
            self,
            bg="#F9F9F9",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill=BOTH, expand=True)
        self.load_images()
        self.create_widgets()

    def load_images(self):
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
        self.button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
        self.button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))

    def create_widgets(self):
        self.canvas.create_image(156.0, 512.0, image=self.image_image_1)
        self.canvas.create_text(
            115.0,
            938.0,
            anchor="nw",
            text="Ngô Long Vũ",
            fill="#000000",
            font=("Itim Regular", 20 * -1)
        )
        self.canvas.create_text(
            112.0,
            962.0,
            anchor="nw",
            text="20210463@eaut.edu.vn",
            fill="#000000",
            font=("Itim Regular", 15 * -1)
        )
        self.canvas.create_text(
            37.0,
            27.0,
            anchor="nw",
            text="Quản Lý Dịch Vụ Chăm Sóc Máy Tính",
            fill="#000000",
            font=("Itim Regular", 30)
        )

        self.button_in_bc = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("in bao cao clicked"),
            relief="flat"
        )
        self.button_in_bc.place(x=1295.0, y=104.0, width=77.0, height=24.0)

        self.button_quan_ly_kh = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("quan ly khach hang clicked"),
            relief="flat"
        )
        self.button_quan_ly_kh.place(x=47.0, y=264.0, width=217.0, height=41.0)

        self.button_quan_ly_bao_cao = Button(
            self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("quan ly bao cao clicked"),
            relief="flat"
        )
        self.button_quan_ly_bao_cao.place(x=47.0, y=374.0, width=217.0, height=41.0)

        self.button_quan_ly_san_pham = Button(
            self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("quan ly san pham clicked"),
            relief="flat"
        )
        self.button_quan_ly_san_pham.place(x=47.0, y=209.0, width=217.0, height=41.0)

        self.button_quan_ly_don_hang = Button(
            self.canvas,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("quan ly don hang clicked"),
            relief="flat"
        )
        self.button_quan_ly_don_hang.place(x=47.0, y=319.0, width=217.0, height=41.0)

        self.entry_search = Entry(
            self.canvas,
            image=self.entry_image_1,
            bd=0,
            bg="#F0F0F0",
            highlightthickness=0
        )
        self.entry_search.place(x=1155.5, y=235.0, width=178.0, height=37.0)

        self.button_add = Button(
            self.canvas,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("add clicked"),
            relief="flat"
        )
        self.button_add.place(x=476.0, y=426.0, width=114.0, height=38.0)

        self.button_edit = Button(
            self.canvas,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("edit clicked"),
            relief="flat"
        )
        self.button_edit.place(x=670.0, y=426.0, width=114.0, height=38.0)

        self.button_delete = Button(
            self.canvas,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("delete clicked"),
            relief="flat"
        )
        self.button_delete.place(x=845.0, y=422.0, width=114.0, height=38.0)

        self.button_search = Button(
            self.canvas,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("tim kiem clicked"),
            relief="flat"
        )
        self.button_search.place(x=1193.0, y=426.0, width=114.0, height=38.0)
