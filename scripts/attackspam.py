from scripts.base import BaseScript


class AttackSpam(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "attackspam"
        self.keyActivate = self.keys[self.name]

    def custom(self):
        self.press('q')
        self.wait(0.3)


def run():
    attack_spam = AttackSpam()
    attack_spam.custom()


if __name__ == "__main__":
    run()
