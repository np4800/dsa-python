class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Linklist:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def searchByRecursion(self, node, key):
        if (not node):
            return False
        if (node.data == key):
            return True
        return self.searchByRecursion(node.next, key)
    
    def printByRecursion(self, node):
        if (not node):
            return False
        self.printByRecursion(node.next)
        print(f"{node.data}", end = "-> ")
            

n1 = Node(1)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)

ll = Linklist()

ll.append(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)

found = ll.searchByRecursion(ll.head, 6)

if found:
    print(f"Element Found")
else:
    print(f"Element Not Found!")

ll.printByRecursion(ll.head)