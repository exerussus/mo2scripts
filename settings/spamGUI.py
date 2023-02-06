from tkinter import Tk, Label, Entry, Button
import tools.jsonOper
#
#
NAME = "spam"
def main(main_mod=False):

    def setting():
        count = 0
        for i in grid_list:
            if count == 0:
                if i.get() != "":
                    settings["activate_key"] = i.get()

            if count != 0:
                if i.get() != "":
                    settings[f"key{count}"]["value"] = i.get()

            count += 1

        data[NAME] = settings
        tools.jsonOper.saveKeys(data) if not main_mod else tools.jsonOper.saveKeysMainMod(data)

    def reset():
        standart_data = tools.jsonOper.reset()  # tools.jsonOper.reset_all()
        custom_path = standart_data[NAME]
        data[NAME] = custom_path
        tools.jsonOper.saveKeys(data) if __name__ != "__main__" else tools.jsonOper.onlySaveKeys(data)
        exit(0)


    def do():
        setting()
        exit(0)

    data = tools.jsonOper.loadKeysGui() if not main_mod else tools.jsonOper.loadKeysGuiMainMod()
    settings = data[NAME]

    window1 = Tk()
    window1.title(f"Mortal Online 2 Scripts {NAME} Settings")
    window1.geometry('650x400')

    count_row = 0
    for i in settings:
        if i != "base":
            if count_row == 0:

                lbl_name = Label(window1, text="Активация")
                lbl_name.grid(column=0, row=count_row)

                lbl_key = Label(window1, text=f"    {settings[i]}")
                lbl_key.grid(column=1, row=count_row)
                count_row += 1


            else:

                lbl_name = Label(window1, text=f'{settings[i]["name"]}  ')
                lbl_name.grid(column=0, row=count_row)

                lbl_key = Label(window1, text=f'    {settings[i]["value"]}')
                lbl_key.grid(column=1, row=count_row)
                count_row += 1

    grid_list = [
                 Entry(window1, width=10),
                 Entry(window1, width=10),
                 Entry(window1, width=10),
                 Entry(window1, width=10),
                 Entry(window1, width=10),
                 Entry(window1, width=10),
                 Entry(window1, width=10),
                 Entry(window1, width=10),
                 Entry(window1, width=10),
                 Entry(window1, width=10),
                 Entry(window1, width=10)
                 ]

    row = 0
    for i in grid_list:
        i.grid(column=2, row=row)
        row += 1

    lbl_pass = Label(window1, text="               ")
    lbl_pass.grid(column=5)
    btn = Button(window1, text="Принять настройки", command=do)
    btn.grid(column=6, row=0)
    btn = Button(window1, text="Сбросить", command=reset)
    btn.grid(column=6, row=2)
    btn = Label(window1, text="Если оставить поля пустыми, то они\n"
                              "будут пропущены. Назначайте кнопки\n"
                              "на те функции, которые нужны, не забывая\n"
                              "указывать время.")
    btn.grid(column=2, row=11)

    window1.mainloop()


def name():
    return NAME


if __name__ == "__main__":
    main(main_mod=True)



