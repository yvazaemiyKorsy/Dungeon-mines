# импорты
import tkinter as tk

class MenuTemplate():
    # переменные

    # картинки
    # cursor_imgs = [
    #     tk.PhotoImage(file="assets/textures/gui/default.png").zoom(4,4)
    #     ]

    def __init__(self, win):
        # окно
        self.win = win

        # канвас
        self.c = tk.Canvas(win, bg="red")
        self.c.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor=tk.CENTER)

        # бинды
        self.win.bind("<Return>", lambda event: print("mish"))

    def tick(self):
        # вычисление коорд курсора
        cur_x = self.win.winfo_pointerx() - self.win.winfo_rootx()
        cur_y = self.win.winfo_pointery() - self.win.winfo_rooty()

        # перемещение курсора
        # print(f"Коорды курсора {cur_x, cur_y}")

    def close(self):
        del self