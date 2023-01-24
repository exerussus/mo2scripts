from scripts.base import BaseScript


class AttackSpam(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "attackspam"
        self.keys = self.keys_data[self.name]
        self.keyActivate = self.keys["activate_key"]

    def custom(self):
        self.press('q')
        self.wait(0.2)
        # self.wait(1)
        # self.hold_and_release_wait('v', 7)





def run():
    attack_spam = AttackSpam()
    attack_spam.custom()


if __name__ == "__main__":
    run()
