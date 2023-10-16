def is_balanced(input_str):
    parentheses = Stack()
    for p in input_str:
        parentheses.push(p)

    counter = 0
    for i in range(len(parentheses.items)):
        if i == 0:
            last_item = parentheses.pop()
            counter += 1
            continue
        else:
            last_item = parentheses.pop()

        if last_item == ")":
            counter += 1
        else:
            counter -= 1

    if counter == 0:
        return True
    else:
        return False


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


def test(input_str):
    print(f"Input: {input_str}")
    print(f"Output: {is_balanced(input_str)}")
    print("=================================")


def main():
    test("(")
    test("()")
    test("(())")
    test("()()")
    test("(()))")
    test("((())())")


main()
