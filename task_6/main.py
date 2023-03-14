"""
У цій грі ви ходите по Львову.
Можна зустріти двох типів персонажів: друзів і ворогів.
Головне вбити всіх ворогів та дійти до останньої вулиці.
"""
import game2 as game


Stryyska = game.Street("вулиця Стрийська")
Stryyska.set_description("Одна з найдовших (близько 7,5 км), \
одна з вулиць із найстарішими назвами (поточна назва — з 1626 року) \
та одна з вулиць із найбільшою кількістю населення.")

Kozelnytska = game.Street("вулиця Козельницька")
Kozelnytska.set_description("На цій вулиці розташований найкращий університет України - УКУ.")

Franka = game.Street("вулиця І.Франка")
Franka.set_description("Одна з перших серед вулиць Львова за \
кількістю пам'яток архітектури. На вулиці розташовано \
52 кам'яниці, що є пам'ятками архітектури місцевого значення та містобудування міста Львова.")

Shevchenka = game.Street("вулиця Шевченка")
Shevchenka.set_description("Одна із семи важливих транспортних магістралей Львова, \
яку так і не можуть доремонтувати.")

Krakivska = game.Street("вулиця Краківська")
Krakivska.set_description("вулиця в історичному центрі Львова, одна з найдавніших вулиць міста.")

Stryyska.link_street(Kozelnytska, "east")
Kozelnytska.link_street(Stryyska, "west")
Kozelnytska.link_street(Franka, "north")
Franka.link_street(Kozelnytska, "south")
Franka.link_street(Shevchenka, "west")
Shevchenka.link_street(Franka, "east")
Shevchenka.link_street(Krakivska, "west")
Krakivska.link_street(Shevchenka, "east")


siriy = game.Enemy("Сєрий", "Розбійник, краще не стикатися.")
siriy.set_conversation("Гони сіги, або кабіну не збереш!")
siriy.set_weakness("самогонка")
Kozelnytska.set_character(siriy)

cavalier = game.Friend("Кавалєр", "А що я пороблю, якщо каблук?")
cavalier.set_conversation("Привіт, я Кавалєр!")
Franka.set_character(cavalier)

vasya = game.Enemy("Вася", "Типічний Вася")
vasya.set_conversation("Не будьте свинями, лушпиння від сємок кидайте на землю\
лишіть курам")
vasya.set_weakness("сємки")
Shevchenka.set_character(vasya)

vanya = game.Enemy("Ваня", "Хто ту батя?")
vanya.set_conversation("За базаром дивись")
vanya.set_weakness("Нокіа 3310")
Krakivska.set_character(vanya)


hooch = game.Item("самогонка")
hooch.set_description("Бабка таке нагнала, шо на голову не налазить")
Stryyska.set_item(hooch)

sevens = game.Item("сємки")
sevens.set_description("В полі зірвав і жуй на здоровля")
Kozelnytska.set_item(sevens)

nokia = game.Item("Нокіа 3310")
nokia.set_description("Невбиваєма телефонка")
Franka.set_item(nokia)

hammer = game.Item("Молоток")
hammer.set_description("ГОловне, щоб не було серпа")
Shevchenka.set_item(hammer)

sickle = game.Item("Серп")
sickle.set_description("ГОловне, щоб не було молотка")
Krakivska.set_item(sickle)

current_street = Stryyska
backpack = []

dead = False
win = False
defeat = 0
friend = False

while dead is False or win is False:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_street = current_street.move(command)

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "help":
        friend = current_street.get_character()
        if friend is not None:
            # try:
                friend.help()
            # except 
        friend = True
        current_street.character = None

    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("Чим будеш його гамселити?")
            print(f"Вибери зі свого рюкзаку: {backpack}")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) is True:
                    # What happens if you win?
                    print("Та ти машина!")
                    current_street.character = None
                    defeat += 1
                else:
                    # What happens if you lose?
                    if friend is True:
                        friend = False
                        print("Ну і не дивно, каблуки слабкі")
                    else:
                        print("Ти навіть не зміг вбити ворога, ти просто сміття")
                        dead = True
            else:
                print(f"В тебе нема {fight_with}. йти шукай")
        else:
            print("Нема з ким битися")
    elif command == "take":
        if item is not None:
            print("Ти жостко поклав " + item.get_name() + " в плахту")
            backpack.append(item.get_name())
            current_street.set_item(None)

        else:
            print("Нема чого брати")
    else:
        print("Я тебе не розумію " + command)
    if defeat == 3:
        win = True
        print("Ти хто такий? Ти вбив всіх ворогів")
