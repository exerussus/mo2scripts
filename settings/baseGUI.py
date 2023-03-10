from tkinter import Tk, Label, Entry, Button
import tools.jsonOper
from GUI import main as main_run


SCRIPT_NAME = "base"
DESCRIPTION = "Описание"


class GUI:
    def __init__(self, script_name, window):
            self.NAME = script_name
            self.main_mode = True if __name__ == "__main__" else False
            self.data = tools.jsonOper.loadKeysGuiMainMod() if self.main_mode else tools.jsonOper.loadKeysGui()
            self.settings = self.data[self.NAME]
            self.descriptions = tools.jsonOper.get_description(self.NAME)
            self.window = Tk()
            self.window.title(f"Mortal Online 2 Scripts {self.NAME} Settings")
            self.GRID_COUNT = len(self.settings)
            self.window.geometry(f'650x{150+self.GRID_COUNT*30 if 150+self.GRID_COUNT*30 < 750 else 750}')
            self.grid_list = [Entry(self.window, width=10) for _ in range(self.GRID_COUNT)]
            self.main_window = window


    def setting(self):
        count = 0
        for i in self.grid_list:
            if count == 0:
                if i.get() != "":
                    self.settings["activate_key"] = i.get()

            if count != 0:
                if i.get() != "":
                    self.settings[f"key{count}"]["value"] = i.get()

            count += 1

        self.data[self.NAME] = self.settings
        tools.jsonOper.saveKeysMainMod(self.data) if self.main_mode else tools.jsonOper.saveKeys(self.data)
        self.destroy()

    def destroy(self):
        self.window.destroy()
        self.main_window.destroy()
        main_run()

    def reset(self):
        standard_data = tools.jsonOper.standard_keys(self.NAME)  # tools.jsonOper.reset_all()
        self.data[self.NAME] = standard_data
        tools.jsonOper.onlySaveKeys(self.data) if self.main_mode else tools.jsonOper.saveKeys(self.data)
        self.destroy()

    def do(self):

        count_row = 0
        for i in self.settings:
            if i != "base":
                if count_row == 0:

                    lbl_name = Label(self.window, text="Активация")
                    lbl_name.grid(column=0, row=count_row)

                    lbl_key = Label(self.window, text=f"    {self.settings[i]}")
                    lbl_key.grid(column=1, row=count_row)
                    count_row += 1

                else:
                    _name = self.settings[i]["name"]
                    lbl_name = Label(self.window, text=f'{_name}  ')
                    lbl_name.grid(column=0, row=count_row)

                    lbl_key = Label(self.window, text=f'    {self.settings[i]["value"]}')
                    lbl_key.grid(column=1, row=count_row)
                    count_row += 1

        row = 0
        for i in self.grid_list:
            i.grid(column=2, row=row)
            row += 1

        lbl_pass = Label(self.window, text="               ")
        lbl_pass.grid(column=5)
        btn = Button(self.window, text="Принять настройки", command=self.setting)
        btn.grid(column=6, row=0)
        btn = Button(self.window, text="Сбросить", command=self.reset)
        btn.grid(column=6, row=2)
        btn = Label(self.window, text=self.descriptions)
        btn.grid(column=2, row=self.GRID_COUNT+2)

        self.window.mainloop()


def name():
    return SCRIPT_NAME


def run(script_name, main_window):
    gui_class_run = GUI(script_name, main_window)
    gui_class_run.do()


if __name__ == "__main__":

    gui_class = GUI(SCRIPT_NAME)
    gui_class.do()




