from scripts.base import BaseScript


class Script(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "fluxing"
        self.keys = self.keys_data[self.name][0]
        self.keyActivate = self.keys["activate_key"]
        self.ready = False

    def custom(self):
        pass


def run():
    script_class = Script()
    script_class.custom()


if __name__ == "__main__":
    run()
