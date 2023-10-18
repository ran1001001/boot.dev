class LLQueue:
    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


n1 = Node("I am head")
n2 = Node("BODY")
n3 = Node("BODY")
n4 = Node("BODY")
n5 = Node("BODY")
n6 = Node("I am tail")
n7 = Node("Insert me Here")

ll = LLQueue()

ll.add_to_tail(n1)
print(ll)
print('==========================================')
print("Enqueue items in Linked List:")
ll.add_to_tail(n2)
ll.add_to_tail(n3)
ll.add_to_tail(n4)
ll.add_to_tail(n5)
ll.add_to_tail(n6)
print(ll)
print('==========================================')
print("Dequeue item in Linked List:")
ll.remove_from_head()
print(ll)
print('==========================================')
print("Enqueue item in Linked List:")
ll.add_to_tail(n7)
print(ll)
