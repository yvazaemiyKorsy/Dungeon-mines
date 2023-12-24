# импорты
import tkinter as tk

class MenuTemplate():

    mouse_right_press = 0
    cursor_img = 0

    def __init__(self, win):
        # окно
        self.win = win

        # картинки
        self.cursor_imgs = [
            tk.PhotoImage(file="assets/textures/gui/cursor/default.png").zoom(4,4),
            tk.PhotoImage(file="assets/textures/gui/cursor/default_active.png").zoom(4,4)
            ]

        # канвас
        self.c = tk.Canvas(win, bg="DimGray", height=800, width=1200)
        self.c.place(relx=0, rely=0, anchor=tk.CENTER)

        # бинды
        self.win.bind("<ButtonPress-1>", self.mouse_right_press_toggle)
        self.win.bind("<ButtonRelease-1>", self.mouse_right_release_toggle)

    def mouse_right_press_toggle(self, event):
        self.mouse_right_press = 1
        self.cursor_img = 1
    def mouse_right_release_toggle(self, event):
        self.mouse_right_press = 0
        self.cursor_img = 0

    def tick(self):
        # вычисление коорд курсора
        self.cur_x = self.win.winfo_pointerx() - self.win.winfo_rootx() - self.c.winfo_x()
        self.cur_y = self.win.winfo_pointery() - self.win.winfo_rooty() - self.c.winfo_y()

        # перемещение курсора должно быть не в темплейте
    
    def create_cursor(self, cur_x, cur_y):
        try:
            self.c.delete(self.cursor)
        except:
            pass
        self.cursor = self.c.create_image(cur_x, cur_y, image=self.cursor_imgs[self.cursor_img], anchor=tk.NW)

    def close(self):
        del self
        self.win.unbind()