import time

RED = "\033[31m"
BLUE = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
VIO = "\033[35m"
UNDERLINE = "\033[4m"
DEFAULT = "\033[0m"
Health = 100
damage = 20
Dragon_health = 200


def write_txt(txt, timeoverlay):
    for i in txt:  # этот цикл будет брать по 1 буковке из тхт
        time.sleep(0)
        print(i, end='', flush=True)
    print("\n")