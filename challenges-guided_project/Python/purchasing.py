def purchase(price, money_available):
    if price > money_available:
        raise Exception("not enough money")
    leftover = money_available - price
    return leftover


def test(price, money_available):
    try:
        print(f"Attempting to purchase an item for ${price} with ${money_available}")
        leftover = purchase(price, money_available)
        print(f"Success! There is ${leftover} leftover")
    except Exception as e:
        print(f"Purchase exception: {e}")
    print("---")


test(10.00, 20.00)
test(30.00, 20.00)
test(15.10, 15.10)
test(1430.00, 69.00)
