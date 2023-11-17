class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Linklist:
    def __init__(self,head=None):
        self.head = head

    def insertAtFront(self, new_node):
        if self.head:
            # if head node is created already then insert here
            new_node.next = self.head
            self.head = new_node
        else:
            # Head is the first node itself
            self.head = new_node
    
    def insert_after(self, prev_node, new_node):
        if prev_node is None:
            print(f"The previous node should be in linklist")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            print(f"First: {new_node.data}")
            self.head = new_node

    def printList(self):
        current = self.head
        while (current != None):
            print(f"{current.data}")
            current = current.next
        

# Main Code
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node('A')

ll = Linklist()
ll.append(n1)
ll.append(n2)
ll.append(n3)

ll.insertAtFront(n4)
ll.insert_after(n2,n5)


ll.printList()