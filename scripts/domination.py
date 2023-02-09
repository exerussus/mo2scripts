from scripts.base import BaseScript


class Script(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "domination"
        self.keys = self.keys_data[self.name][0]
        self.keyActivate = self.keys["activate_key"]
        self.action_key = self.keys["key1"]["value"]
        self.holding_time = float(self.keys["key2"]["value"])
        self.domination = True if self.keys["key3"]["value"] == "1" else False

    def hold_or_release(self, mode: str):
        """ mode - hold or release """
        if self.domination and mode == "hold":
            self.hold("lctrl")
            self.wait(0.1)
            self.hold("lctrl")
            self.wait(0.1)
        if self.domination and mode == "release":
            self.release("lctrl")
            self.wait(0.1)
            self.release("lctrl")
            self.wait(0.1)

    def action_pressing(self):
        self.hold(self.action_key)
        self.wait(self.holding_time)
        self.wait(0.1)
        self.release(self.action_key)
        self.wait(0.2)

    def custom(self):

        self.hold_or_release("hold")
        self.action_pressing()
        self.hold_or_release("release")


def run():
    script_class = Script()
    script_class.custom()


if __name__ == "__main__":
    run()

