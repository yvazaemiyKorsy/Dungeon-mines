# импорты
import tkinter as tk
import time
import player_movement_test

class Main():
    # переменные
    win = tk.Tk()

    fullscreen = False

    def __init__(self):
        # конфиг win
        self.win.geometry("1200x800")
        self.win.title("Dungeons mines")
        self.win.config(bg = "black", cursor="none")
        self.win.attributes("-fullscreen", self.fullscreen)
        try:
            self.win.iconbitmap()
        except:
            pass

        # бинды
        self.win.bind("<F11>", self.fullscreen_toggle)

    def cycle(self):
        while 1:
            current_menu.tick()
            time.sleep(0.025)
            self.win.update()

    def fullscreen_toggle(self, event):
        self.fullscreen = not self.fullscreen
        self.win.attributes("-fullscreen", self.fullscreen)

if __name__ == "__main__":
    main_session = Main()
    current_menu = player_movement_test.Menu(main_session.win)
    main_session.cycle()
