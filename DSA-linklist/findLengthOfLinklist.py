class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Linklist:
    def __init__(self, head=None ) -> None:
        self.head = head

    def push(self, new_element):
        new_element.next  = self.head
        self.head = new_element

    def getCount(self):
        current = self.head
        count = 0
        while (current):
            count +=1
            current = current.next
        return count

    def getCountRecursive(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getCountRecursive(node.next)
        
if __name__ == "__main__":
    ll = Linklist()

    n1 = Node(1)
    n2 = Node(20)
    n3 = Node(40)
    n4 = Node(50)
    n5 = Node(100)

    ll.push(n1)
    ll.push(n2)
    ll.push(n3)
    ll.push(n4)
    ll.push(n5)


    print(f"Total number element (Iterator  Method) in LL: {ll.getCount()}")
    print(f"Total number element (Recursive Method) in LL: {ll.getCountRecursive(ll.head)}")