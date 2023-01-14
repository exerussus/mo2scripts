from tkinter import Tk, Label, Entry, Button
from main import MortalScripts
import tools.jsonOper
#
#


def show():
    print(activate.get())


def setting():

    if activate.get() != "":
        settings["activate_key"] = activate.get()
    if overhead.get() != "":
        settings["key1"]["value"] = overhead.get()
    if weapon_up.get() != "":
        settings["key2"]["value"] = weapon_up.get()
    if jump.get() != "":
        settings["key3"]["value"] = jump.get()
    if forward.get() != "":
        settings["key4"]["value"] = forward.get()
    if backward.get() != "":
        settings["key5"]["value"] = backward.get()
    if attack_charge.get() != "":
        settings["key6"]["value"] = attack_charge.get()
    if after_attack.get() != "":
        settings["key7"]["value"] = after_attack.get()
    if move_backward.get() != "":
        settings["key8"]["value"] = move_backward.get()
    if move_forward.get() != "":
        settings["key9"]["value"] = move_forward.get()

    data["destroyerPickaxe"] = settings
    tools.jsonOper.saveKeys(data)


def run():
    mortal = MortalScripts()
    mortal.run()


def do():
    setting()
    exit(0)


data = tools.jsonOper.loadKeys()
settings = data["destroyerPickaxe"]

window = Tk()
window.title("Mortal Online 2 Scripts")
window.geometry('400x250')


count_row = 0
for i in settings:
    if i != "base":
        if count_row == 0:

            lbl_name = Label(window, text="Активация")
            lbl_name.grid(column=0, row=count_row)

            lbl_key = Label(window, text=settings[i])
            lbl_key.grid(column=1, row=count_row)
            count_row += 1

        else:

            lbl_name = Label(window, text=settings[i]["name"])
            lbl_name.grid(column=0, row=count_row)

            lbl_key = Label(window, text=settings[i]["value"])
            lbl_key.grid(column=1, row=count_row)
            count_row += 1

activate = Entry(window, width=10)
activate.grid(column=2, row=0)

overhead = Entry(window, width=10)
overhead.grid(column=2, row=1)

weapon_up = Entry(window, width=10)
weapon_up.grid(column=2, row=2)

jump = Entry(window, width=10)
jump.grid(column=2, row=3)

forward = Entry(window, width=10)
forward.grid(column=2, row=4)

backward = Entry(window, width=10)
backward.grid(column=2, row=5)

attack_charge = Entry(window, width=10)
attack_charge.grid(column=2, row=6)

after_attack = Entry(window, width=10)
after_attack.grid(column=2, row=7)

move_backward = Entry(window, width=10)
move_backward.grid(column=2, row=8)

move_forward = Entry(window, width=10)
move_forward.grid(column=2, row=9)


lbl_pass = Label(text="               ")
lbl_pass.grid(column=5)
btn = Button(window, text="Принять настройки", command=do)
btn.grid(column=6, row=0)



#
# lbl = Label(window, text="Привет")
# lbl.grid(column=0, row=0)
# txt = Entry(window, width=10, show="as")
# txt.grid(column=1, row=0)
# btn = Button(window, text="Не нажимать!", command=clicked)
# btn.grid(column=2, row=0)

window.mainloop()




