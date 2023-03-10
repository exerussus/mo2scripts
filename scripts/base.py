import time

import keyboard
import autoit
import pyautogui

import tools.jsonOper
import os


class BaseScript:

    name = file_name = os.path.basename(__file__)[:-3]
    config = {
        "activate_key": "",
        "key1": {"name": "", "value": ""},
        "key2": {"name": "", "value": ""},
        "key3": {"name": "", "value": ""},
        "key4": {"name": "", "value": ""},
        "key5": {"name": "", "value": ""},
        "key6": {"name": "", "value": ""},
    }
    description = ""
    keys = tools.jsonOper.loadKeys(name) if name != "base" else config
    ready = True if keys["activate_key"] != "" else False

    def __init__(self):

        self.name = "base"
        self.keys = BaseScript.keys
        self.keyActivate = BaseScript.config # self.keys["activate_key"]
        self.game = "Mortal Online 2  "
        self.window_w = 1920
        self.window_h = 1080
        self.exitKey = False
        self.isStop = False
        self.loop = True
        self.debug = True

    def debug_log(self, value: str, debug_show=True):
        if self.debug:
            if debug_show:
                print(f"DEBUG: {value}")
            else:
                print(value)

    def save(self):
        tools.jsonOper.saveKeys(self.keys)
        self.debug_log("Saving keys...")

    def importKeyActivation(self, name: str):
        self.keyActivate = name
        self.debug_log(f"Importing key activation from name: {name}...")

    def startFunction(self):
        self.isStop = False
        self.debug_log("Started function, self.isStop = False...")

    def hold_and_release_wait(self, key: str, hold_time: float):
        self.debug_log(f"Holding {key} for {hold_time} sec...")
        self.hold(key)
        self.wait(hold_time)
        self.release(key)
        self.debug_log(f"{key} key released...")

    def hold_and_release_sleep(self, key: str, hold_time: float):
        self.debug_log(f"Holding {key} for {hold_time} sec with sleep method...")
        self.hold(key)
        time.sleep(hold_time)
        self.release(key)
        self.debug_log(f"{key} key released with sleep method...")

    def checkExitKey(self):
        if keyboard.is_pressed("f9"):
            self.exitKey = True
            self.debug_log(f"F9 pressed...")
            exit(0)

    def checkStopKey(self):
        if keyboard.is_pressed("f7"):
            self.isStop = True
            self.debug_log(f"F7 pressed...")

    def func_repetition(self, function, repetitions, args=None):
        self.debug_log(f"func_repetition: func {function} for {repetitions} repetitions...")
        if not self.checkStopKey() and not self.checkExitKey():
            for _ in range(repetitions):

                if self.checkStopKey() or self.checkExitKey():
                    break
                if args is None:
                    function()
                else:
                    function(args)

    def wait(self, seconds, debug=True):
        if debug: self.debug_log(f"waiting {seconds} seconds...")
        if not self.isStop and not self.exitKey:
            time_out = seconds
            timer = 0
            if time_out < 1:
                while time_out > timer and not self.isStop and not self.exitKey:
                    time.sleep(0.01)
                    timer += 0.01
                    self.checkExitKey()
                    self.checkStopKey()
            else:
                while time_out > timer and not self.isStop and not self.exitKey:
                    time.sleep(0.1)
                    timer += 0.1
                    self.checkExitKey()
                    self.checkStopKey()

    def rWait(self, number):
        self.debug_log(f"waiting random time between {number * 0.9} and {number * 1.1} seconds...")
        import random
        self.wait(random.uniform(number*0.9, number*1.1))

    def press(self, key):
        self.debug_log(f"pressed {key} key...")
        if not self.isStop and not self.exitKey:
            autoit.control_send(f"[TITLE:{self.game}]", "", f"{key}")

    def hold(self, key):
        self.debug_log(f"holding {key} key...")
        if not self.isStop and not self.exitKey:
            autoit.control_send(f"[TITLE:{self.game}]", "", "{" + f"{key} down" + "}")

    def hold_and_release_sleep_pag(self, key: str, time_count: float):
        with pyautogui.hold(key):
            time.sleep(time_count)

    def hold_and_release_wait_pag(self, key: str, time_count: float):
        with pyautogui.hold(key):
            self.wait(time_count)

    def release(self, key):
        self.debug_log(f"released {key} key...")
        if not self.isStop and not self.exitKey:
            autoit.control_send(f"[TITLE:{self.game}]", "", "{" + f"{key} up" + "}")

    def clc_x(self, x):
        return round(x/1920 * self.window_w)

    def clc_y(self, y):
        return round(y/1080 * self.window_h)

    def mouse_click(self, button, x, y, speed=1):
        if not self.isStop and not self.exitKey:
            autoit.mouse_click(button, speed=speed, x=self.clc_x(x), y=self.clc_y(y))
            self.wait(0.1)

    def run(self):
        if keyboard.is_pressed(self.keyActivate): # if __name__ == "__main__" else True:
            self.startFunction()
            if self.loop:
                self.debug_log(f"{self.name} is activated with loop")
                self.customLoop()
                self.debug_log(f"{self.name} is deactivated")
            else:
                self.custom()
                self.debug_log(f"{self.name} is deactivated")


    def custom(self):
        pass

    def customLoop(self):
        while not self.exitKey and not self.isStop:
            self.custom()
            self.checkExitKey()
            self.checkStopKey()
