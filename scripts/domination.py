from scripts.base import BaseScript


class Domination(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "domination"
        self.keyActivate = self.keys[self.name]

    def custom(self):

        print("16 domination")
        # self.press("{CTRLDOWN}")
        self.wait(0.1)
        self.hold("r")
        self.wait(5)
        # self.press("{CTRLUP}")
        self.wait(0.1)
        self.release("r")


def run():
    script_class = Domination()
    script_class.custom()


if __name__ == "__main__":
    run()

