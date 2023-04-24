from settings import *
import random

write_txt(f"Вы поднялись на высокую вершину {RED}Хребта Драконьих зубов{DEFAULT},", 0.07)
write_txt(f"чтобы найти дракона, который являлся причиной разрушения многих поселений в районе.", 0.07)
write_txt(f"Солнце сияло ярко на небе, когда вы увидели, как дракон выходит из пещеры.", 0.07)
write_txt(f"Его крылья были огромными, а когти и зубы были острыми как бритва.", 0.07)
write_txt(f"Вы были готовы к этой битве.", 0.07)


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
        write_txt(f"Вы {RED}{UNDERLINE}погибли{DEFAULT}", 0.05)
        write_txt(f"{RED}{UNDERLINE}DEATH{DEFAULT}", 0.05)
        exit()


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


'''
def health_boost(variable):
    write_txt(f"Вы мгновенно применили заклинание {BLUE}магической{DEFAULT} защиты,", 0.05)
    write_txt(f"и вы почувствовали, как силы {BLUE}магии{DEFAULT} защищают вас.", 0.05)
    change_character("health", variable)
    print_health("chara")
'''

'''
def not_health_boost(variable):
    write_txt(f"{RED}Дракон{DEFAULT} сломал защиту и ударил вас", 0.05)
    change_character("health", -variable)
    print_health("chara")
    death()
'''


def is_health_boost(variable):
    does = random.randint(1, 2)
    if does == 1:
        write_txt(f"Вы мгновенно применили заклинание {BLUE}магической{DEFAULT} защиты,", 0.05)
        write_txt(f"и вы почувствовали, как силы {BLUE}магии{DEFAULT} защищают вас.", 0.05)
        change_character("health", variable)
        print_health("chara")
    elif does == 2:
        write_txt(f"{RED}Дракон{DEFAULT} сломал защиту и ударил вас", 0.05)
        change_character("health", -variable)
        print_health("chara")
        death()


'''
def dragon_dodged(variable):
    write_txt(f"Вы выстрелили в {RED}дракона{DEFAULT} {RED}огненным{DEFAULT} шаром, но он увернулся, и {RED}шар{DEFAULT} разбился о скалу.", 0.05)
    write_txt(f"Огромные крылья создавали порывы {BLUE}ветра{DEFAULT}, и вы едва удерживались на своих ногах.", 0.05)
    change_character("damage", -variable)
    death()
'''


def dragon_damage(variable, experience):
    global Dragon_health
    write_txt(f"Вы выстрелили в {RED}дракона{DEFAULT} {BLUE}магическими{DEFAULT} стрелами, которые ударили в его глаза.", 0.05)
    write_txt(f"{RED}Дракон{DEFAULT} закричал от боли и взмыл в воздух, пытаясь избежать вашей атаки.", 0.05)
    Dragon_health -= variable
    print_health("dragon")
    death_dragon(experience)


'''
def dragon_hit(variable):
    write_txt(f"Вы отпустили {RED}огненный{DEFAULT} шар,", 0.05)
    write_txt(f"который попал в {RED}дракона{DEFAULT}, но он не показывал признаков усталости.", 0.05)
    write_txt(f"{RED}Дракон{DEFAULT} завис в воздухе, раскрыв свои крылья, и ударил по вам своими могучими лапами.", 0.05)
    change_character("health", -variable)
    print_health("chara")
    death()
'''


def is_dragon_fireball(variable, experience, changedamage):
    global Dragon_health
    does = random.randint(1, 3)
    if does == 1:
        write_txt(f"Вы отпустили {RED}огненный{DEFAULT} шар,", 0.05)
        write_txt(f"который попал в {RED}дракона{DEFAULT}, но он не показывал признаков усталости.", 0.05)
        write_txt(f"{RED}Дракон{DEFAULT} завис в воздухе, раскрыв свои крылья, и ударил по вам своими могучими лапами.", 0.05)
        change_character("health", -variable)
        print_health("chara")
        death()
    elif does == 2:
        write_txt(f"Вы попали в дракона фаерболлом", 0.05)
        Dragon_health -= variable
        print_health("dragon")
        death_dragon(experience)
    elif does == 3:
        write_txt(f"Вы выстрелили в {RED}дракона{DEFAULT} {RED}огненным{DEFAULT} шаром, но он увернулся, и {RED}шар{DEFAULT} разбился о скалу.", 0.05)
        write_txt(f"Огромные крылья создавали порывы {BLUE}ветра{DEFAULT}, и вы едва удерживались на своих ногах.", 0.05)
        change_character("damage", -changedamage)
        death()
        

def dragon_hit_two(variable):
    write_txt(f"{RED}Дракон{DEFAULT} начал вращаться, создавая вокруг себя {BLUE}вихрь{DEFAULT},", 0.05)
    write_txt(f"Вы были обездвижены, когда {RED}дракон{DEFAULT} приблизился к вам, готовясь ударить своими острыми когтями.", 0.05)
    change_character("health", -variable)
    print_health("chara")
    death()

'''
def dragon_hit_fireball(variable, experience):
    global Dragon_health
    write_txt(f"Вы попали в дракона фаерболлом", 0.05)
    Dragon_health -= variable
    print_health("dragon")
    death_dragon(experience)
'''


def fight_variant_four():
    otvet = fight()
    if otvet == 1:
        is_dragon_fireball(10, 15, 3)
        otvet = fight()
        if otvet == 1:
            is_dragon_fireball(10, 15, 3)
            fight_variant_three()
        elif otvet == 2:
            is_health_boost(10)
            fight_variant_three()
        elif otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            fight_variant_three()
        elif otvet == 4:
            dragon_hit_two(5)
            fight_variant_three()
    elif otvet == 2:
        is_health_boost(10)
        fight_variant_three()
    elif otvet == 3:
        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
        fight_variant_three()
    elif otvet == 4:
        dragon_hit_two(5)
        otvet = fight()
        if otvet == 1:
            is_dragon_fireball(10, 15, 3)
            fight_variant_three()
        elif otvet == 2:
            is_health_boost(10)
            fight_variant_three()
        elif otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            fight_variant_three()
        elif otvet == 4:
            dragon_hit_two(5)
            fight_variant_three()


def fight_variant_three():
    otvet = fight()
    if otvet == 1:
        is_dragon_fireball(10, 15, 3)
        fight_variant_four()
    elif otvet == 2:
        is_health_boost(10)
        fight_variant_four()
    elif otvet == 3:
        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
        fight_variant_four()
    elif otvet == 4:
        dragon_hit_two(10)
        fight_variant_four()


def fight_variant_two():
    global otvet
    otvet = fight()
    if otvet == 1:
        is_dragon_fireball(10, 15, 3)
        otvet = fight()
        if otvet == 1:
            is_dragon_fireball(10, 15, 3)
            fight_variant_three()
        elif otvet == 2:
            is_health_boost(10)
            fight_variant_three()
        elif otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            fight_variant_three()
        elif otvet == 4:
            dragon_hit_two(5)
            fight_variant_three()
    elif otvet == 2:
        is_health_boost(10)
        fight_variant_three()
    elif otvet == 3:
        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
        fight_variant_three()
    elif otvet == 4:
        dragon_hit_two(5)
        otvet = fight()
        if otvet == 1:
            is_dragon_fireball(10, 15, 3)
            fight_variant_three()
        elif otvet == 2:
            is_health_boost(10)
            fight_variant_three()
        elif otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            fight_variant_three()
        elif otvet == 4:
            dragon_hit_two(5)
            fight_variant_three()


def fight_variant_one():
    global otvet
    otvet = fight()
    if otvet == 1:
        is_dragon_fireball(10, 15, 3)
        fight_variant_two()
    elif otvet == 2:
        is_health_boost(10)
        fight_variant_two()
    elif otvet == 3:
        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
        fight_variant_three()
    elif otvet == 4:
        dragon_hit_two(5)
        fight_variant_two()


def dragon_fight():
    global Health
    otvet = fight()
    if otvet == 1:
        is_dragon_fireball(10, 15, 3)
        otvet = fight()
        if otvet == 1:
            is_dragon_fireball(10, 15, 3)
            fight_variant_one()
        if otvet == 2:
            is_health_boost(10)
            fight_variant_one()
        if otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            fight_variant_one()
        elif otvet == 4:
            write_txt(f"Дракон начал вращаться, создавая вокруг себя вихрь,", 0.05)
            write_txt(f"Вы были обездвижены, когда дракон приблизился к вам, готовясь ударить своими острыми когтями.", 0.05)
            otvet = fight()
            if otvet == 1:
                is_dragon_fireball(10, 15, 3)
                fight_variant_one()
            elif otvet == 2:
                is_health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                fight_variant_one()
            elif otvet == 4:
                Health -= 100
                print_health("chara")
                death()
    elif otvet == 2:
        is_health_boost(10)
        fight_variant_one()
    elif otvet == 3:
        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
        otvet = fight()
        if otvet == 1:
            is_dragon_fireball(10, 15, 3)
            fight_variant_one()
        elif otvet == 2:
            is_health_boost(10)
            otvet = fight()
            if otvet == 1:
                is_dragon_fireball(10, 15, 3)
                fight_variant_one()
            if otvet == 2:
                is_health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                fight_variant_one()
            elif otvet == 4:
                dragon_hit_two(5)
                fight_variant_one()
        elif otvet == 3:
            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
            otvet = fight()
            if otvet == 1:
                is_dragon_fireball(10, 15, 3)
                fight_variant_one()
            if otvet == 2:
                is_health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                fight_variant_one()
            elif otvet == 4:
                dragon_hit_two(5)
                fight_variant_one()
        elif otvet == 4:
            dragon_hit_two(5)
            otvet = fight()
            if otvet == 1:
                is_dragon_fireball(10, 15, 3)
                fight_variant_one()
            if otvet == 2:
                is_health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                fight_variant_one()
            elif otvet == 4:
                dragon_hit_two(5)
                fight_variant_one()

    elif otvet == 4:
        dragon_damage(damage, 20)
        otvet = fight()
        if otvet == 1:
            is_dragon_fireball(10, 15, 3)
            otvet = fight()
            if otvet == 1:
                is_dragon_fireball(10, 15, 3)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 2:
                    is_health_boost(10)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                elif otvet == 3:
                    otvet = fight()
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            if otvet == 1:
                                is_dragon_fireball(10, 15, 3)
                                fight_variant_one()
                            elif otvet == 2:
                                is_health_boost(10)
                                fight_variant_one()
                            elif otvet == 3:
                                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                                fight_variant_one()
                            elif otvet == 4:
                                dragon_hit_two(5)
                                fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()

            elif otvet == 2:
                is_health_boost(10)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()

                elif otvet == 2:
                    is_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    otvet = fight()
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            otvet = fight()
                            if otvet == 1:
                                is_dragon_fireball(10, 15, 3)
                                fight_variant_one()
                            elif otvet == 2:
                                is_health_boost(10)
                                fight_variant_one()
                            elif otvet == 3:
                                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                                fight_variant_one()
                            elif otvet == 4:
                                dragon_hit_two(5)
                                fight_variant_one()

                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()

            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 2:
                    is_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()

            elif otvet == 4:
                dragon_hit_two(5)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 2:
                    is_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()

        elif otvet == 2:
            is_health_boost(10)
            otvet = fight()
            if otvet == 1:
                is_dragon_fireball(10, 15, 3)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    fight_variant_one()
                elif otvet == 2:
                    is_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    fight_variant_one()
            elif otvet == 2:
                is_health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 2:
                    is_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
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
            otvet = fight()
            if otvet == 1:
                is_dragon_fireball(10, 15, 3)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    fight_variant_one()
                elif otvet == 2:
                    is_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    fight_variant_one()
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()

            elif otvet == 2:
                is_health_boost(10)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                elif otvet == 2:
                    is_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                        fight_variant_one()
                    elif otvet == 4:
                        dragon_hit_two(5)
                        otvet = fight()
                        if otvet == 1:
                            is_dragon_fireball(10, 15, 3)
                            fight_variant_one()
                        elif otvet == 2:
                            is_health_boost(10)
                            fight_variant_one()
                        elif otvet == 3:
                            write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                            fight_variant_one()
                        elif otvet == 4:
                            dragon_hit_two(5)
                            fight_variant_one()

            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
                        fight_variant_one()
                    elif otvet == 3:
                        write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    elif otvet == 4:
                        dragon_hit_two(5)
                        fight_variant_one()
                elif otvet == 2:
                    is_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    otvet = fight()
                    if otvet == 1:
                        is_dragon_fireball(10, 15, 3)
                        fight_variant_one()
                    elif otvet == 2:
                        is_health_boost(10)
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
            otvet = fight()
            if otvet == 1:
                is_dragon_fireball(10, 15, 3)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    fight_variant_one()
                elif otvet == 2:
                    is_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    fight_variant_one()
            elif otvet == 2:
                is_health_boost(10)
                fight_variant_one()
            elif otvet == 3:
                write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                fight_variant_one()
            elif otvet == 4:
                dragon_hit_two(5)
                otvet = fight()
                if otvet == 1:
                    is_dragon_fireball(10, 15, 3)
                    fight_variant_one()
                elif otvet == 2:
                    is_health_boost(10)
                    fight_variant_one()
                elif otvet == 3:
                    write_txt(f"Элитры недоступны, купите их Городе Шума", 0.05)
                    fight_variant_one()
                elif otvet == 4:
                    dragon_hit_two(5)
                    fight_variant_one()