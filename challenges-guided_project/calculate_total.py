def calculate_total(items_purchased, grocery_list):
    unpurchased_items = []
    receipt = {}
    total = 0
    for grocery in grocery_list:
        if grocery in items_purchased:
            price = item_prices[grocery]
            receipt[grocery] = price
            total = total + price
            continue
        else:
            unpurchased_items.append(grocery)
    return unpurchased_items, receipt, total


item_prices = {
    "milk": 2.50,
    "eggs": 3.25,
    "bread": 1.21,
    "cheese": 3.50,
    "apples": 7.44,
    "bananas": 3.88,
    "carrots": 3.89,
    "lettuce": 1.12,
    "potatoes": 32.21,
    "cereal": 5.99,
}


def test(items_purchased, grocery_list):
    unpurchased_items, receipt, total = calculate_total(items_purchased, grocery_list)

    print("=" * 40)
    print("SHOPPING SUMMARY")
    print("=" * 40)

    print("\nItems Not Purchased:")
    print("-" * 20)
    print(", ".join(sorted(unpurchased_items)))

    print("\nReceipt:")
    print("-" * 20)
    for item, price in receipt.items():
        print(f"{item.ljust(15)} ${price:.2f}")

    print("-" * 20)
    print(f"{'Total:'.ljust(15)} ${total:.2f}")
    print("=" * 40)
    print("\n")


# Test the function
test(
    ["milk", "eggs", "bread", "cheese", "apples", "bananas", "lettuce", "cereal"],
    [
        "milk",
        "eggs",
        "bread",
        "cheese",
        "apples",
        "bananas",
        "carrots",
        "lettuce",
        "potatoes",
        "cereal",
    ],
)

test(
    ["milk", "bread", "cheese", "lettuce", "cereal"],
    [
        "milk",
        "eggs",
        "bread",
        "cheese",
        "apples",
        "bananas",
        "carrots",
        "lettuce",
        "potatoes",
        "cereal",
    ],
)

test(
    ["milk", "bread", "lettuce", "cereal"],
    [
        "milk",
        "eggs",
        "bread",
        "cheese",
        "apples",
        "bananas",
        "carrots",
        "lettuce",
        "potatoes",
        "cereal",
    ],
)
