
from scripts.base import BaseScript
import os



class MortalScripts(BaseScript):

    def __init__(self):
        super().__init__()
        # Подключенные скрипты
        self.scripts_pack = []
        for filename in os.listdir("scripts"):
            if filename[-2:] == "py":
                filename = filename[:-3]
                if filename != "base":
                    exec(f"import scripts.{filename}")
                    script_class = eval(f"scripts.{filename}.Script()")
                    if script_class.name != "base":
                        if script_class.ready:
                            self.scripts_pack.append(script_class)
                            print(f"Скрипт {script_class.name} инициализирован...")
                        else:
                            print(f"Скрипт {script_class.name} не инициализирован - self.ready = False...")


    def run(self):

        while not self.exitKey:
            for script in self.scripts_pack:
                script.run()
            self.checkExitKey()
            self.wait(0.1, debug=False)


def run():
    mortal_script = MortalScripts()
    mortal_script.run()


if __name__ == "__main__":
    run()
