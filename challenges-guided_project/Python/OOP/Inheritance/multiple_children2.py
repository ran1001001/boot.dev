class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


# Create the Wizard class here
class Wizard(Hero):
    def __init__(self, name, health, mana):
        self.__mana = mana
        super().__init__(name, health)

    def cast(self, target):
        if self.__mana <= 0:
            raise Exception("not enough mana")
        self.__mana -= 25
        target.take_damage(25)


def main():
    health = 30
    mana = 70
    print(f"Creating a Wizard named Harry with {health} health and {mana} mana")
    hero1 = Wizard("Harry", health, mana)
    identify(hero1)

    health = 100
    arrows = 3
    print(f"Creating an Archer named Pericles with {health} health and {arrows} arrows")
    hero2 = Archer("Pericles", health, arrows)
    identify(hero2)

    while hero1.get_health() > 0 and hero2.get_health() > 0:
        try:
            print(f"{hero1.get_name()} attempts to cast at {hero2.get_name()}")

            hero1.cast(hero2)
            identify(hero1)
            identify(hero2)
        except Exception as e:
            print(e)

        try:
            print(f"{hero2.get_name()} attempts to shoot {hero1.get_name()}")
            hero2.shoot(hero1)
            identify(hero1)
            identify(hero2)
        except Exception as e:
            print(e)


def identify(hero):
    print(f"Name: {hero.get_name()}, health: {hero.get_health()}")


main()
