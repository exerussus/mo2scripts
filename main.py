
from scripts.destroyerPickaxe import DestroyerPickAxe
from scripts.base import BaseScript
from scripts.domination import Domination
from scripts.attackspam import AttackSpam
from scripts.attacker import Attacker
from scripts.feintRightAttackOverhead import FeintRightAttackOverhead
from scripts.spacer import Spacer
from scripts.mentalTraining import MentalTraining



class MortalScripts(BaseScript):

    def __init__(self):
        super().__init__()

        # Подключенные скрипты
        self.scripts_pack = {
            # Domination(),
            # AttackSpam(),
            # Attacker(),
            # Spacer(),
            # MentalTraining(),
            DestroyerPickAxe(),
        }

    def run(self):
        while not self.exitKey:
            for script in self.scripts_pack:
                script.run()
            self.checkExitKey()
            self.wait(0.01)


def run():
    mortal_script = MortalScripts()
    mortal_script.run()


if __name__ == "__main__":
    run()
