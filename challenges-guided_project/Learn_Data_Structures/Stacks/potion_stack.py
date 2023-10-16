import random


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


class PotionStack(Stack):
    def __init__(self):
        super().__init__()

    def push(self, value):
        if super().peek() == value:
            pass
        else:
            super().push(value)


def main():
    stack = PotionStack()
    fill_stack(stack, 2)
    pop_stack(stack)
    pop_stack(stack)

    fill_stack(stack, 6)
    peek_stack(stack)
    peek_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)


def pop_stack(stack):
    print("popping: " + str(stack.pop()))
    print(f"potions: {stack.items}")
    print("=================================")
    return stack


def peek_stack(stack):
    print("peeking: " + str(stack.peek()))
    print(f"potions: {stack.items}")
    print("=================================")
    return stack


def push_stack(stack, val):
    print("pushing: " + val)
    stack.push(val)
    print(f"potions: {stack.items}")
    print("=================================")
    return stack


def fill_stack(stack, num):
    random.seed(0)
    options = ["Mana Potion", "Health Potion", "Stamina Potion"]
    for i in range(num):
        optionI = random.randint(0, len(options) - 1)
        push_stack(stack, options[optionI])
    return stack


main()
