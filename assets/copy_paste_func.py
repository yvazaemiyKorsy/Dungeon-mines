# импорты
import tkinter as tk
import menu_template

class Menu(menu_template.MenuTemplate):

    def __init__(self, win):
        super(Menu, self).__init__(win)
        # делать чтт

    def tick(self):
        super(Menu, self).tick()
        # делать чтт
        self.create_cursor(self.cur_x, self.cur_y)

    def close(self):
        super(Menu, self).close()
        # делать чтт