from tkinter import Tk, Label, Button
import tools.jsonOper
from settings import baseGUI
from functools import partial


class Settings_GUI:

    def __init__(self):
        self.data = tools.jsonOper.loadKeysGui()
        self.scripts = [i for i in self.data if i != "base"]
        self.window_gui = Tk()
        self.window_gui.title("Mortal Online 2 Scripts HUB")
        self.window_gui.geometry(f'250x{100 + len(self.scripts) * 25}')

    def do(self):
        count = 0
        for i in self.scripts:
            lbl_name = Label(self.window_gui, text=f'{i}')
            lbl_name.grid(column=0, row=count)

            lbl_key = Button(self.window_gui, text=f'Настройка', command=partial(self.call, i))
            lbl_key.grid(column=1, row=count)

            lbl_action_key = Label(self.window_gui, text=f'{self.data[i][0]["activate_key"]}')
            lbl_action_key.grid(column=2, row=count)
            count += 1

        lbl_pass = Label(text=" "*14)
        lbl_pass.grid(column=5)
        btn = Button(self.window_gui, text="Закрыть", command=self.close)
        btn.grid(column=1, row=count+1)

        self.window_gui.mainloop()

    def close(self):
        exit(0)

    def call(self, name):
        baseGUI.run(name, self.window_gui)


def main():
    class_gui = Settings_GUI()
    class_gui.do()


if __name__ == "__main__":
    main()



