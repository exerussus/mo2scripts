from tkinter import Tk, Label, Entry, Button
import tools.jsonOper
#
#

def main():

    def setting():

        if activate.get() != "":
            settings["activate_key"] = activate.get()
        if press_1.get() != "":
            settings["key1"]["value"] = press_1.get()
        if wait_1.get() != "":
            settings["key2"]["value"] = wait_1.get()
        if hold_2.get() != "":
            settings["key3"]["value"] = hold_2.get()
        if holding_time_2.get() != "":
            settings["key4"]["value"] = holding_time_2.get()
        if press_3.get() != "":
            settings["key5"]["value"] = press_3.get()
        if wait_3.get() != "":
            settings["key6"]["value"] = wait_3.get()
        if hold_4.get() != "":
            settings["key7"]["value"] = hold_4.get()
        if holding_time_4.get() != "":
            settings["key8"]["value"] = holding_time_4.get()

        data["spam"] = settings
        tools.jsonOper.saveKeys(data)

    def reset():
        tools.jsonOper.reset()
        exit(0)

    def do():
        setting()
        exit(0)

    data = tools.jsonOper.loadKeysGui()
    settings = data["spam"]

    window1 = Tk()
    window1.title("Mortal Online 2 Scripts Spam Settings")
    window1.geometry('600x400')

    count_row = 0
    for i in settings:
        if i != "base":
            if count_row == 0:

                lbl_name = Label(window1, text="Активация")
                lbl_name.grid(column=0, row=count_row)

                lbl_key = Label(window1, text=f"|    {settings[i]}")
                lbl_key.grid(column=1, row=count_row)
                count_row += 1

            else:

                lbl_name = Label(window1, text=f'{settings[i]["name"]}  ')
                lbl_name.grid(column=0, row=count_row)

                lbl_key = Label(window1, text=f'|    {settings[i]["value"]}')
                lbl_key.grid(column=1, row=count_row)
                count_row += 1

    activate = Entry(window1, width=10)
    activate.grid(column=2, row=0)

    press_1 = Entry(window1, width=10)
    press_1.grid(column=2, row=1)

    wait_1 = Entry(window1, width=10)
    wait_1.grid(column=2, row=2)

    hold_2 = Entry(window1, width=10)
    hold_2.grid(column=2, row=3)

    holding_time_2 = Entry(window1, width=10)
    holding_time_2.grid(column=2, row=4)

    press_3 = Entry(window1, width=10)
    press_3.grid(column=2, row=5)

    wait_3 = Entry(window1, width=10)
    wait_3.grid(column=2, row=6)

    hold_4 = Entry(window1, width=10)
    hold_4.grid(column=2, row=7)

    holding_time_4 = Entry(window1, width=10)
    holding_time_4.grid(column=2, row=8)

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
    return "spam"


if __name__ == "__main__":
    main()



