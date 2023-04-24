import time
RED = "\033[31m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
VIO = "\033[35m"
UNDERLINE = "\033[4m"
DEFAULT = "\033[0m"


def write_txt(txt, timeoverlay):
    for i in txt:  # этот цикл будет брать по 1 буковке из тхт
        time.sleep(timeoverlay)
        print(i, end='', flush=False)
    print("\n")


write_txt(f"Добро пожаловать в квест {UNDERLINE}{BLUE}Magic and {RED}Dragons{DEFAULT}!", 0.3)
write_txt(f"Наша история начинается в мире, где {BLUE}магия{DEFAULT} и {RED}драконы{DEFAULT} были обычным явлением.", 0.1)
write_txt(f"Здесь, в каждом уголке мира, жители существовали в гармонии с природой,", 0.1)
write_txt(f"используя {BLUE}магические{DEFAULT} силы, чтобы выращивать урожай и строить свои дома.", 0.1)
write_txt(f"Но в последнее время, мир стал находиться во власти {VIO}тьмы{DEFAULT}.", 0.1)
character = input("Введите имя персонажа: ")
write_txt(f"Вы, {UNDERLINE}{BLUE}{character}{DEFAULT} находитесь в начале своего путешествия,", 0.1)
write_txt(f"у вас есть только несколько заклинаний и ваше мастерство владения {BLUE}магией{DEFAULT},", 0.1)
write_txt(f"но вы полны решимости и готовы сражаться.", 0.1)
write_txt(f"Вы отправляетесь в неизвестность, в надежде найти ответы и вернуть свет и мир в ваш мир.", 0.1)
# write_txt(f"Вы, {BLUE}{character}{DEFAULT} куда собираетесь?", 0.1)
write_txt(f"1. {GREEN}Лес Эльвин{DEFAULT}: Это красивый и загадочный лес, где обитают эльфы и другие {BLUE}магические{DEFAULT} создания.", 0.1)
write_txt(f"Внутри леса вы найдете ручейки, озера и водопады, а также множество {BLUE}сказочных{DEFAULT} существ.", 0.1)
write_txt(f"2. {RED}Хребет Драконьих зубов{DEFAULT}: Это высокие горы, где обитают драконы и другие магические существа.", 0.1)
write_txt(f"Здесь вы можете обнаружить драгоценные камни и драгоценные металлы,", 0.1)
write_txt(f"но будьте осторожны, драконы могут быть очень агрессивными.", 0.1)
write_txt(f"3. {BLUE}Город Шум{DEFAULT}: Это оживленный город, где живут люди и маги.", 0.1)
write_txt(f"Здесь вы можете найти торговые кварталы, где можно купить {BLUE}заклинания{DEFAULT}, {BLUE}магические{DEFAULT} артефакты и другие вещи.", 0.1)
write_txt(f"Также здесь есть кузницы и магические мастерские, где вы можете улучшить свои оружие и броню.", 0.1)
write_txt(f"4. {YELLOW}Темный лабиринт{DEFAULT}: Это {RED}опасное{DEFAULT} место, где вы можете встретить множество {YELLOW}ловушек{DEFAULT}, монстров и других {RED}опасностей{DEFAULT}.", 0.1)
write_txt(f"В центре лабиринта вы можете найти магический артефакт, который поможет вам в битве против темных сил.", 0.1)
write_txt(f"5. {VIO}Остров забытых душ{DEFAULT}: Это {VIO}таинственный{DEFAULT} остров, где обитают духи умерших и другие {BLUE}магические{DEFAULT} существа.", 0.1)
write_txt("Здесь вы можете получить советы и знания, которые помогут вам в вашем путешествии. Хоть и будет страшно.", 0.1)
location = input()