import time

import keyboard
import autoit
import tools.jsonOper


class BaseScript:

    def __init__(self):
        self.keys_data = tools.jsonOper.loadKeys()
        self.name = "base"
        self.keys = self.keys_data[self.name]
        self.keyActivate = self.keys["activate_key"]
        self.game = "Mortal Online 2  "
        self.exitKey = False
        self.isStop = False
        self.loop = True
        self.debug = True

    def _debug(self, value: str):
        if self.debug:
            print(value)

    def save(self):
        tools.jsonOper.saveKeys(self.keys)
        self._debug("DEBUG: Saving keys...")

    def importKeyActivation(self, name: str):
        self.keyActivate = name
        self._debug(f"DEBUG: Importing key activation from name: {name}...")

    def startFunction(self):
        self.isStop = False
        self._debug("DEBUG: Started function, self.isStop = False...")

    def hold_and_release_wait(self, key: str, hold_time: float):
        self._debug(f"DEBUG: Holding {key} for {hold_time} sec...")
        self.hold(key)
        self.wait(hold_time)
        self.release(key)
        self._debug(f"DEBUG: {key} key released...")

    def hold_and_release_sleep(self, key: str, hold_time: float):
        self._debug(f"DEBUG: Holding {key} for {hold_time} sec with sleep method...")
        self.hold(key)
        time.sleep(hold_time)
        self.release(key)
        self._debug(f"DEBUG: {key} key released with sleep method...")

    def checkExitKey(self):
        if keyboard.is_pressed("f9"):
            self.exitKey = True
            self._debug(f"DEBUG: F9 pressed...")

    def checkStopKey(self):
        if keyboard.is_pressed("f7"):
            self.isStop = True
            self._debug(f"DEBUG: F7 pressed...")

    def func_repetition(self, function, repetitions, args=None):
        self._debug(f"DEBUG: func_repetition: func {function} for {repetitions} repetitions...")
        if not self.checkStopKey() and not self.checkExitKey():
            for _ in range(repetitions):

                if self.checkStopKey() or self.checkExitKey():
                    break
                if args is None:
                    function()
                else:
                    function(args)

    def wait(self, seconds):
        if seconds != 0.01: self._debug(f"DEBUG: waiting {seconds} seconds...")
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
        self._debug(f"DEBUG: waiting random time between {number*0.9} and {number*1.1} seconds...")
        import random
        self.wait(random.uniform(number*0.9, number*1.1))

    def press(self, key):
        self._debug(f"DEBUG: pressed {key} key...")
        if not self.isStop and not self.exitKey:
            autoit.control_send(f"[TITLE:{self.game}]", "", f"{key}")

    def hold(self, key):
        self._debug(f"DEBUG: holding {key} key...")
        if not self.isStop and not self.exitKey:
            autoit.control_send(f"[TITLE:{self.game}]", "", "{" + f"{key} down" + "}")

    def release(self, key):
        self._debug(f"DEBUG: released {key} key...")
        if not self.isStop and not self.exitKey:
            autoit.control_send(f"[TITLE:{self.game}]", "", "{" + f"{key} up" + "}")

    def run(self):
        if keyboard.is_pressed(self.keyActivate):
            self._debug(f"DEBUG: {self.name} is activated")
            self.startFunction()
            if self.loop:
                self.customLoop()
                self._debug(f"DEBUG: {self.name} is deactivated")
            else:
                self.custom()
                self._debug(f"DEBUG: {self.name} is deactivated")


    def custom(self):
        pass

    def customLoop(self):
        while not self.exitKey and not self.isStop:
            self.custom()
            self.checkExitKey()
            self.checkStopKey()
