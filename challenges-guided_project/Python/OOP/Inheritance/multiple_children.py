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


# Create Archer class here
class Archer(Hero):
    def __init__(self, name, health, num_of_arrows):
        self.__num_of_arrows = num_of_arrows
        super().__init__(name, health)

    def shoot(self, target):
        if self.__num_of_arrows <= 0:
            raise Exception("not enough arrows")
        else:
            self.__num_of_arrows -= 1
            target.take_damage(10)


def main():
    try:
        print("Creating a hero named Hercules with 200 health")
        human1 = Hero("Hercules", 200)
        identify(human1)

        print("creating an Archer named Pericles with 100 health and 2 arrows")
        human2 = Archer("Pericles", 100, 2)
        identify(human2)

        while human1.get_health() > 0 and human2.get_health() > 0:
            print(f"{human2.get_name()} attempts to shoot {human1.get_name()}")
            human2.shoot(human1)
            identify(human1)
            identify(human2)

    except Exception as e:
        print(e)


def identify(human):
    print(f"Name: {human.get_name()}, health: {human.get_health()}")


main()
