#!C:\Users\sokol\PycharmProjects\mo2scripts\venv\Scripts\python
from tkinter import Tk, Label, Button
import tools.jsonOper
from settings import baseGUI
from functools import partial
from tools.name_translater import do as normalize


class Settings_GUI:

    def __init__(self):
        self.window_bg = "#66CCFF"
        self.data = tools.jsonOper.loadKeysGui()
        self.scripts = [i for i in self.data if i != "base"]
        self.window_gui = Tk()
        self.window_gui.title("Mortal Online 2 Scripts HUB")
        self.window_gui.geometry(f'280x{200 + len(self.scripts) * 25}')
        self.window_gui.configure(bg=self.window_bg)

    def do(self):
        count = 0
        for i in self.scripts:

            norm_name = normalize(i)
            name = i if norm_name is None else norm_name

            lbl_name = Label(self.window_gui, text=f'{name}', font='sans 9')
            lbl_name.grid(column=0, row=count)

            lbl_key = Button(self.window_gui, text=f'Настройка', command=partial(self.call, i))
            lbl_key.grid(column=1, row=count)

            lbl_action_key = Label(self.window_gui, text=f'{self.data[i]["activate_key"]}')
            lbl_action_key.grid(column=2, row=count)
            count += 1

        lbl_pass = Label(text=" ", bg=self.window_bg)
        lbl_pass.grid(column=5)
        btn = Button(self.window_gui, text="Закрыть", command=self.close, bg="#FF9999", font='sans 10 bold')
        btn.grid(column=1, row=count+1)

        lbl_pass = Label(text=" ", bg=self.window_bg)
        lbl_pass.grid(column=1, row=count + 2)

        start_btn = Button(self.window_gui, text="Сбросить ключи", command=self.reinit_key, bg="yellow", font='sans 10 bold')
        start_btn.grid(column=1, row=count + 3)

        lbl_pass = Label(text=" ", bg=self.window_bg)
        lbl_pass.grid(column=1, row=count + 4)

        start_btn = Button(self.window_gui, text="Запустить", command=self.start, bg="#99ff66", font='sans 10 bold')
        start_btn.grid(column=1, row=count + 5)

        self.window_gui.mainloop()

    def reinit_key(self):
        tools.jsonOper.reset_all()
        self.data = tools.jsonOper.loadKeysGui()
        self.window_gui.destroy()
        main()

    def start(self):
        from main import run as program_run
        self.data = tools.jsonOper.loadKeysGui()
        self.window_gui.destroy()
        program_run()

    def close(self):
        exit(0)

    def call(self, name):
        baseGUI.run(name, self.window_gui)


def main():
    class_gui = Settings_GUI()
    class_gui.do()


if __name__ == "__main__":
    main()



