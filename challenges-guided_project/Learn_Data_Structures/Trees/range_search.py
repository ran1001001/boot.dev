import random


class BSTNode:
    def traverse(self, list, low, up):
        gamertag = self.val.gamertag
        if gamertag < low:
            if self.right:
                self.right.traverse(list, low, up)
        else:
            if gamertag >= low and gamertag <= up:
                list.append(self.val)
            if self.left:
                self.left.traverse(list, low, up)
            if self.right:
                self.right.traverse(list, low, up)

    def search_range(self, lower_bound, upper_bound):
        list = []
        self.traverse(list, lower_bound, upper_bound)
        return list

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def __repr__(self):
        lines = []
        print_tree(self, lines)
        return "\n".join(lines)


class Character:
    def __init__(self, gamertag):
        self.gamertag = gamertag
        character_names = [
            "Ebork",
            "Astram",
            "Elian",
            "Tarlock",
            "Grog",
            "Myra",
            "Sullivan",
            "Marlo",
            "Jax",
            "Anthony",
            "Bhurdan",
            "Thoreuth",
            "Bob",
            "Varis",
            "Nyx",
            "Luna",
            "Ash",
            "Rhogar",
            "Ember",
            "Mikel",
            "Yamil",
            "Velithria",
        ]
        self.character_name = (
            f"{character_names[gamertag%len(character_names)]}#{gamertag}"
        )

    def __eq__(self, other):
        return self.gamertag == other.gamertag

    def __lt__(self, other):
        return self.gamertag < other.gamertag

    def __gt__(self, other):
        return self.gamertag > other.gamertag

    def __repr__(self):
        return "".join(self.character_name)


def print_tree(bst_node, lines, level=0):
    if bst_node != None:
        print_tree(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        print_tree(bst_node.left, lines, level + 1)


def get_characters(num):
    characters = []
    for _ in range(num):
        character = Character(random.randint(0, num - 1))
        characters.append(character)
    return characters


def test(num_characters, lower_bound, upper_bound):
    characters = get_characters(num_characters)
    bst = BSTNode()
    for character in characters:
        bst.insert(character)
    print("Tree:")
    print(bst)
    print("-------------------------------------")
    print(f"Searching for characters between {lower_bound} and {upper_bound}:")
    result = bst.search_range(lower_bound, upper_bound)
    for character in sorted(result):
        print(f" - {character}")
    print("=====================================")


def main():
    random.seed(1)
    test(10, 2, 6)
    test(20, 8, 14)
    test(30, 12, 24)


main()
