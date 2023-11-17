class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Linklist:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        current = self.head

        while (current.next != None):
            print("->",current.data)
            current = current.next
        
    def search(self,x):
        current = self.head

        while (current.next != None):
            if current.data == x:
                return True
            current = current.next
        return False
    
## Driving Code
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

ll = Linklist()
ll.append(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)

ll.printlist()

x = 1

if ll.search(x):
    print(f"Whooopie I found {x} in the LinkList")
else:
    print("Better Luck Next Time")

        