class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result = self.__result + a

    def subtract(self, a):
        self.__result = self.__result - a

    def multiply(self, a):
        self.__result = self.__result * a

    def divide(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result = self.__result / a

    def modulo(self, a):
        if a == 0:
            raise ValueError("Cannot divie by zero")
        self.__result = self.__result % a

    def power(self, a):
        self.__result = self.__result ** a

    def square_root(self):
        self.__result = self.__result ** 0.5

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result

def test(starting_num):
    calculator = Calculator()
    calculator.add(starting_num)
    print(f"Starting number: {starting_num}")
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Adding 5...")
    calculator.add(5)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Modulo 7...")
    calculator.modulo(7)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Power 2...")
    calculator.power(2)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Square root...")
    calculator.square_root()
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Subtracting 3...")
    calculator.subtract(3)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Multiplying by 2...")
    calculator.multiply(2)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Dividing by 6...")
    calculator.divide(6)
    print(f"Result: {calculator.get_result():.2f}")
    print(f"Clearing...")
    calculator.clear()
    print(f"Result: {calculator.get_result():.2f}")
    print("=====================================")


def main():
    test(11.0)
    test(6.0)
    test(0.0)


main()
