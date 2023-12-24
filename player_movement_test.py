# импорты
import tkinter as tk
import menu_template

class Menu(menu_template.MenuTemplate):

    def __init__(self, win):
        super(Menu, self).__init__(win)

        self.player = self.c.create_rectangle(0, 0, 40, 40, fill="olive", outline="olive")
        self.player_speed = 10
        self.camera_smooth = 8

    def tick(self):
        super(Menu, self).tick()
        # self.move_player("sins")

        # ходить если кнопка зажата
        if self.mouse_right_press == 1:
            self.move_player("sisi")

        # планове перемещение камеры
        self.c.place(x=round(self.c.winfo_x()-(self.win.winfo_width()/(self.camera_smooth*2)) + (-self.c.coords(self.player)[0]-self.c.winfo_x()+self.win.winfo_width())/(self.camera_smooth)),
                     y=round(self.c.winfo_y()-self.win.winfo_height()/(self.camera_smooth*2) + (-self.c.coords(self.player)[1]-self.c.winfo_y())/self.camera_smooth + self.win.winfo_height()/self.camera_smooth), 
                     anchor="nw")

        # курсор
        self.create_cursor(self.cur_x, self.cur_y)

    def move_player(self, event):
        # вычисление дистанции до курсора по 2м осям
        self.player_to_cur_distance_x = self.cur_x - self.c.coords(self.player)[0]
        self.player_to_cur_distance_y = self.cur_y - self.c.coords(self.player)[1]

        # теорема пифогора для вычисления векторного расстояния (настоящего)
        self.player_vector = (self.player_to_cur_distance_x**2 + self.player_to_cur_distance_y**2)**0.5

        # вычисление отношения вектора до мышы со скоростью игрока и вычисление скорости по 2м осям
        if not self.player_vector == 0:
            self.player_x_movement = round((self.player_speed/self.player_vector)*self.player_to_cur_distance_x)
            self.player_y_movement = round((self.player_speed/self.player_vector)*self.player_to_cur_distance_y)
        else:
            self.player_x_movement, self.player_y_movement = 0

        # само перемещение
        self.c.move(self.player, self.player_x_movement, self.player_y_movement)

    def close(self):
        super(Menu, self).close()