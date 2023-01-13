import time

import keyboard
import autoit
import tools.jsonOper


class BaseScript:

    def __init__(self):
        self.keys = tools.jsonOper.loadKeys()
        self.name = "base"
        self.keyActivate = self.keys[self.name]
        self.game = "Mortal Online 2  "
        self.exitKey = False
        self.isStop = False
        self.loop = True
        self.debug = True

    def save(self):
        tools.jsonOper.saveKeys(self.keys)

    def importKeyActivation(self, name: str):
        self.keyActivate = name

    def startFunction(self):
        self.isStop = False

    def hold_and_release(self, key: str, hold_time: float):
        self.hold(key)
        time.sleep(hold_time)
        self.release(key)

    def checkExitKey(self):
        if keyboard.is_pressed("f9"):
            self.exitKey = True

    def checkStopKey(self):
        if keyboard.is_pressed("f7"):
            self.isStop = True

    def func_repetition(self, function, repetitions, args=None):
        if not self.checkStopKey() and not self.checkExitKey():
            for _ in range(repetitions):

                if self.checkStopKey() or self.checkExitKey():
                    break
                if args is None:
                    function()
                else:
                    function(args)

    def wait(self, seconds):
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
        import random
        self.wait(random.uniform(number*0.9, number*1.1))

    def press(self, key):
        if not self.isStop and not self.exitKey:
            autoit.control_send(f"[TITLE:{self.game}]", "", f"{key}")

    def hold(self, key):
        if not self.isStop and not self.exitKey:
            autoit.control_send(f"[TITLE:{self.game}]", "", "{" + f"{key} down" + "}")

    def release(self, key):
        if not self.isStop and not self.exitKey:
            autoit.control_send(f"[TITLE:{self.game}]", "", "{" + f"{key} up" + "}")

    def run(self):
        if keyboard.is_pressed(self.keyActivate):
            if self.debug:
                print(f"{self.name} is activated")
            self.startFunction()
            if self.loop:
                self.customLoop()
                if self.debug:
                    print(f"{self.name} is deactivated")
            else:
                self.custom()
                if self.debug:
                    print(f"{self.name} is deactivated")

    def custom(self):
        pass

    def customLoop(self):
        while not self.exitKey and not self.isStop:
            self.custom()
            self.checkExitKey()
            self.checkStopKey()
