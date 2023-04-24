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
        time.sleep(timeoverlay)
        print(i, end='', flush=True)
    print("\n")


def fight():
    write_txt(f"Что выберите?", 0.05)
    write_txt(f"1. {RED}Фаербол{DEFAULT}", 0.05)
    write_txt(f"2. {BLUE}Магическая защита{DEFAULT}", 0.05)
    write_txt(f"3. {VIO}Элитры{DEFAULT}", 0.05)
    write_txt(f"4. {GREEN}Магические стрелы{DEFAULT}", 0.05)
    weapon = int(input())
    return weapon


def death():
    global Health
    if Health <= 0:
        write_txt(f"Вы {RED}погибли{DEFAULT}", 0.05)
        write_txt(f"{RED}DEATH{DEFAULT}", 0.05)


def death_dragon(variable):
    if Dragon_health <= 0:
        write_txt(f"Дракон {RED}умер{DEFAULT}", 0.05)
        write_txt(f"Получено {variable} опыта", 0.05)


def print_health(char):
    global damage, Health
    if char == "chara":
        write_txt(f"У вас отсталось {RED}{Health}{DEFAULT}", 0.05)
    if char == "dragon":
        write_txt(f"У {RED}дракона{DEFAULT} осталось {Dragon_health}", 0.05)


def print_damage():
    global damage
    write_txt(f"Ваш урон {damage}", 0.05)


def change_character(changer, variable):
    global damage, Health
    if changer == "damage":
        if variable > 0:
            damage += variable
            write_txt(f"Урон увеличен на {variable}", 0.05)
        elif variable < 0:
            damage += variable
            write_txt(f"Урон уменьшен на {variable}", 0.05)
    elif changer == "health":
        if variable > 0:
            Health += variable
            write_txt(f"+{variable} {RED}HP{DEFAULT}", 0.05)
        if variable < 0:
            Health += variable
            write_txt(f"-{variable} {RED}HP{DEFAULT}", 0.05)


def health_boost(variable):
    write_txt(f"Вы мгновенно применили заклинание {BLUE}магической{DEFAULT} защиты,", 0.05)
    write_txt(f"и вы почувствовали, как силы {BLUE}магии{DEFAULT} защищают вас.", 0.05)
    change_character("health", variable)
    print_health("chara")


def not_health_boost(variable):
    write_txt(f"{RED}Дракон{DEFAULT} не дал вам вылечиться и ударил вас", 0.05)
    change_character("health", -variable)
    print_health("chara")
    death()


def dragon_dodged(variable):
    write_txt(f"Вы выстрелили в {RED}дракона{DEFAULT} {RED}огненным{DEFAULT} шаром, но он увернулся, и {RED}шар{DEFAULT} разбился о скалу.", 0.05)
    write_txt(f"Огромные крылья создавали порывы {BLUE}ветра{DEFAULT}, и вы едва удерживались на своих ногах.", 0.05)
    change_character("damage", -variable)
    death()


def dragon_damage(variable, experience):
    global Dragon_health
    write_txt(f"Вы выстрелили в {RED}дракона{DEFAULT} {BLUE}магическими{DEFAULT} стрелами, которые ударили в его глаза.", 0.05)
    write_txt(f"{RED}Дракон{DEFAULT} закричал от боли и взмыл в воздух, пытаясь избежать вашей атаки.", 0.05)
    Dragon_health -= variable
    print_health("dragon")
    death_dragon(experience)


def dragon_hit(variable):
    write_txt(f"Вы отпустили {RED}огненный{DEFAULT} шар,", 0.05)
    write_txt(f"который попал в {RED}дракона{DEFAULT}, но он не показывал признаков усталости.", 0.05)
    write_txt(f"{RED}Дракон{DEFAULT} завис в воздухе, раскрыв свои крылья, и ударил по вам своими могучими лапами.", 0.05)
    change_character("health", -variable)
    print_health("chara")
    death()


def dragon_hit_two(variable):
    write_txt(f"{RED}Дракон{DEFAULT} начал вращаться, создавая вокруг себя {BLUE}вихрь{DEFAULT},", 0.05)
    write_txt(f"Вы были обездвижены, когда {RED}дракон{DEFAULT} приблизился к вам, готовясь ударить своими острыми когтями.", 0.05)
    change_character("health", -variable)
    print_health("chara")
    death()


def dragon_hit_fireball(variable, experience):
    global Dragon_health
    write_txt(f"Вы попали в дракона фаерболлом", 0.05)
    Dragon_health -= variable
    print_health("dragon")
    death_dragon(experience)


def fight_variant_three():
    otvet = fight()
    if otvet == 1:
        dragon_hit(10)
    elif otvet == 2:
        health_boost(10)
    elif otvet == 3:
        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
    elif otvet == 4:
        dragon_hit_two(10)


def fight_variant_two():
    otvet = fight()
    if otvet == 1:
        dragon_dodged(3)
        if otvet == 1:
            dragon_dodged(2)
            fight_variant_three()
        elif otvet == 2:
            health_boost(10)
            fight_variant_three()
        elif otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            fight_variant_three()
        elif otvet == 4:
            dragon_hit_two(5)
            fight_variant_three()
    elif otvet == 2:
        not_health_boost(10)
        fight_variant_three()
    elif otvet == 3:
        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
        fight_variant_three()
    elif otvet == 4:
        dragon_hit_two(5)
        fight_variant_three()
    elif otvet == 4:
        dragon_hit_two(5)
        if otvet == 1:
            dragon_hit_fireball(damage, 15)
            fight_variant_three()
        elif otvet == 2:
            not_health_boost(10)
            fight_variant_three()
        elif otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            fight_variant_three()
        elif otvet == 4:
            dragon_hit_two(5)
            fight_variant_three()


def fight_variant_one():
    otvet = fight()
    if otvet == 1:
        dragon_hit_fireball(damage, 15)
        fight_variant_two()
    elif otvet == 2:
        health_boost(10)
        fight_variant_two()
    elif otvet == 3:
        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
        fight_variant_three()
    elif otvet == 4:
        dragon_hit_two(5)
        fight_variant_two()


write_txt(f"Добро пожаловать в квест {UNDERLINE}{BLUE}Magic and {RED}Dragons{DEFAULT}!", 0.07)
write_txt(f"Наша история начинается в мире, где {BLUE}магия{DEFAULT} и {RED}драконы{DEFAULT} были обычным явлением.", 0.07)
write_txt(f"Здесь, в каждом уголке мира, жители существовали в гармонии с природой,", 0.07)
write_txt(f"используя {BLUE}магические{DEFAULT} силы, чтобы выращивать урожай и строить свои дома.", 0.07)
write_txt(f"Но в последнее время, мир стал находиться во власти {VIO}тьмы{DEFAULT}.", 0.07)
character = input("Введите имя персонажа: ")
write_txt(f"Вы, {UNDERLINE}{BLUE}{character}{DEFAULT} находитесь в начале своего путешествия,", 0.07)
write_txt(f"у вас есть только несколько заклинаний и ваше мастерство владения {BLUE}магией{DEFAULT},", 0.07)
write_txt(f"но вы полны решимости и готовы сражаться.", 0.07)
write_txt(f"Вы отправляетесь в неизвестность, в надежде найти ответы и вернуть свет и мир в ваш мир.", 0.07)
# write_txt(f"Вы, {BLUE}{character}{DEFAULT} куда собираетесь?", 0.07)
write_txt(f"1. {GREEN}Лес Эльвин{DEFAULT}: Это красивый и загадочный лес, где обитают эльфы и другие {BLUE}магические{DEFAULT} создания.", 0.07)
write_txt(f"Внутри леса вы найдете ручейки, озера и водопады, а также множество {BLUE}сказочных{DEFAULT} существ.", 0.07)
write_txt(f"2. {RED}Хребет Драконьих зубов{DEFAULT}: Это высокие горы, где обитают драконы и другие магические существа.", 0.07)
write_txt(f"Здесь вы можете обнаружить драгоценные камни и драгоценные металлы,", 0.07)
write_txt(f"но будьте осторожны, драконы могут быть очень агрессивными.", 0.07)
write_txt(f"3. {BLUE}Город Шум{DEFAULT}: Это оживленный город, где живут люди и маги.", 0.07)
write_txt(f"Здесь вы можете найти торговые кварталы, где можно купить {BLUE}заклинания{DEFAULT}, {BLUE}магические{DEFAULT} артефакты и другие вещи.", 0.07)
write_txt(f"Также здесь есть кузницы и магические мастерские, где вы можете улучшить свои оружие и броню.", 0.07)
write_txt(f"4. {YELLOW}Темный лабиринт{DEFAULT}: Это {RED}опасное{DEFAULT} место, где вы можете встретить множество {YELLOW}ловушек{DEFAULT}, монстров и других {RED}опасностей{DEFAULT}.", 0.07)
write_txt(f"В центре лабиринта вы можете найти магический артефакт, который поможет вам в битве против темных сил.", 0.07)
write_txt(f"5. {VIO}Остров забытых душ{DEFAULT}: Это {VIO}таинственный{DEFAULT} остров, где обитают духи умерших и другие {BLUE}магические{DEFAULT} существа.", 0.07)
write_txt("Здесь вы можете получить советы и знания, которые помогут вам в вашем путешествии. Хоть и будет страшно.", 0.07)
location = int(input())


if location == 1:
    write_txt(f"", 0.07)
elif location == 2:
    write_txt(f"Вы поднялись на высокую вершину {RED}Хребта Драконьих зубов{DEFAULT},", 0.07)
    write_txt(f"чтобы найти дракона, который являлся причиной разрушения многих поселений в районе.", 0.07)
    write_txt(f"Солнце сияло ярко на небе, когда вы увидели, как дракон выходит из пещеры.", 0.07)
    write_txt(f"Его крылья были огромными, а когти и зубы были острыми как бритва.", 0.07)
    write_txt(f"Вы были готовы к этой битве.", 0.07)
    otvet = fight()
    if otvet == 1:
        dragon_dodged(5)
        if otvet == 1:
            dragon_hit(10)
            fight_variant_one()
        if otvet == 2:
            health_boost(10)
            fight_variant_one()
        if otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            fight_variant_one()
        elif otvet == 4:
            write_txt(f"Дракон начал вращаться, создавая вокруг себя вихрь,", 0.05)
            write_txt(f"Вы были обездвижены, когда дракон приблизился к вам, готовясь ударить своими острыми когтями.", 0.05)
            if otvet == 1:
                dragon_dodged(5)
                fight_variant_one()
            elif otvet == 2:
                health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                fight_variant_one()
            elif otvet == 4:
                Health -= 100
                print_health("chara")
                death()
    elif otvet == 2:
        health_boost(10)
        time.sleep(1)
        fight_variant_one()
    elif otvet == 3:
        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
        if otvet == 1:
            dragon_dodged(5)
            fight_variant_one()
        elif otvet == 2:
            health_boost(10)
            if otvet == 1:
                dragon_dodged(5)
                fight_variant_one()
            if otvet == 2:
                not_health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                fight_variant_one()
            elif otvet == 4:
                dragon_hit_two(5)
                fight_variant_one()
        elif otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            if otvet == 1:
                dragon_dodged(5)
                fight_variant_one()
            if otvet == 2:
                not_health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                fight_variant_one()
            elif otvet == 4:
                dragon_hit_two(5)
                fight_variant_one()
        elif otvet == 4:
            dragon_hit_two(5)
            if otvet == 1:
                dragon_dodged(5)
                fight_variant_one()
            if otvet == 2:
                not_health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                fight_variant_one()
            elif otvet == 4:
                dragon_hit_two(5)
                fight_variant_one()

    elif otvet == 4:
        dragon_damage(damage, 20)
        if otvet == 1:
            dragon_dodged(5)
            if otvet == 1:
                dragon_dodged(5)
                if otvet == 1:
                    dragon_dodged(5)
                    if otvet == 1:
                        dragon_hit_fireball(10, 15)
                        if otvet == 1:
                            dragon_dodged(3)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 2:
                    not_health_boost(10)
                    if otvet == 1:
                        dragon_dodged(3)
                        if otvet == 1:
                            dragon_dodged(3)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        if otvet == 1:
                            dragon_hit_fireball(10, 15)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    if otvet == 1:
                        dragon_dodged(3)
                        if otvet == 1:
                            dragon_dodged(3)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            if otvet == 1:
                                dragon_hit_fireball(10, 15)
                                fight_variant_one()
                            elif otvet == 2:
                                health_boost(10)
                                fight_variant_one()
                            elif otvet == 3:
                                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                                fight_variant_one()
                            elif otvet == 4:
                                dragon_hit_two(5)
                                fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    if otvet == 1:
                        dragon_hit_fireball(10, 15)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        if otvet == 1:
                            dragon_hit_fireball(10, 15)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()

            elif otvet == 2:
                not_health_boost(10)
                if otvet == 1:
                    dragon_hit_fireball(10, 15)
                    if otvet == 1:
                        dragon_dodged(3)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        if otvet == 1:
                            dragon_hit_fireball(10, 15)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()

                elif otvet == 2:
                    not_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    if otvet == 1:
                        dragon_hit_fireball(10, 15)
                        if otvet == 1:
                            dragon_dodged(3)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            if otvet == 1:
                                dragon_hit_fireball(10, 15)
                                fight_variant_one()
                            elif otvet == 2:
                                health_boost(10)
                                fight_variant_one()
                            elif otvet == 3:
                                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                                fight_variant_one()
                            elif otvet == 4:
                                dragon_hit_two(5)
                                fight_variant_one()

                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        if otvet == 1:
                            dragon_hit_fireball(10, 15)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()

            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                if otvet == 1:
                    dragon_hit_fireball(10, 15)
                    if otvet == 1:
                        dragon_dodged(3)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 2:
                    health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    if otvet == 1:
                        dragon_hit_fireball(10, 15)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()

            elif otvet == 4:
                dragon_hit_two(5)
                if otvet == 1:
                    dragon_hit_fireball(10, 15)
                    if otvet == 1:
                        dragon_dodged(3)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 2:
                    not_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    if otvet == 1:
                        dragon_hit_fireball(10, 15)
                        if otvet == 1:
                            dragon_dodged(3)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        if otvet == 1:
                            dragon_hit_fireball(10, 15)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()

        elif otvet == 2:
            not_health_boost(10)
            if otvet == 1:
                dragon_hit_fireball(10, 15)
                if otvet == 1:
                    dragon_dodged(3)
                    fight_variant_one()
                elif otvet == 2:
                    health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    fight_variant_one()
            elif otvet == 2:
                health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                if otvet == 1:
                    dragon_hit_fireball(10, 15)
                    if otvet == 1:
                        dragon_dodged(3)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 2:
                    not_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    if otvet == 1:
                        dragon_hit_fireball(10, 15)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        if otvet == 1:
                            dragon_hit_fireball(10, 15)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()

        elif otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            if otvet == 1:
                dragon_hit_fireball(10, 15)
                if otvet == 1:
                    dragon_dodged(3)
                    fight_variant_one()
                elif otvet == 2:
                    not_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    fight_variant_one()
                    if otvet == 1:
                        dragon_hit_fireball(10, 15)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()

            elif otvet == 2:
                health_boost(10)
                if otvet == 1:
                    dragon_hit_fireball(10, 15)
                    if otvet == 1:
                        dragon_dodged(3)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                        if otvet == 1:
                            dragon_hit_fireball(10, 15)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                elif otvet == 2:
                    health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    if otvet == 1:
                        dragon_hit_fireball(10, 15)
                        if otvet == 1:
                            dragon_dodged(3)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                    elif otvet == 2:
                        not_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        if otvet == 1:
                            dragon_hit_fireball(10, 15)
                            fight_variant_one()
                        elif otvet == 2:
                            health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()

            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                if otvet == 1:
                    dragon_hit_fireball(10, 15)
                    if otvet == 1:
                        dragon_dodged(3)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 2:
                    health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    if otvet == 1:
                        dragon_hit_fireball(10, 15)
                        fight_variant_one()
                    elif otvet == 2:
                        health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
            elif otvet == 4:
                dragon_hit_two(5)
                fight_variant_one()

        elif otvet == 4:
            dragon_damage(damage, 15)
            if otvet == 1:
                dragon_hit_fireball(10, 15)
                if otvet == 1:
                    dragon_dodged(3)
                    fight_variant_one()
                elif otvet == 2:
                    health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    fight_variant_one()
            elif otvet == 2:
                health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                fight_variant_one()
            elif otvet == 4:
                dragon_hit_two(5)
                if otvet == 1:
                    dragon_hit_fireball(10, 15)
                    fight_variant_one()
                elif otvet == 2:
                    health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    fight_variant_one()


elif location == 3:
    write_txt(f"", 0.07)
elif location == 4:
    write_txt(f"", 0.07)
elif location == 5:
    write_txt(f"", 0.07)