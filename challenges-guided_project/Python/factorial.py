def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


def test(num):
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")


test(0)
test(4)
test(5)
test(7)
test(9)
test(13)
test(15)
test(14)
