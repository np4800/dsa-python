class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
                # print(f"{current.data}")
            current.next = new_element
        else:
            self.head = new_element

    def reverseLLByIteration(self):
        prev = None
        current = self.head

        while (current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverseUtil(next, curr)
    
    def reverseLLByRecursion(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def printLinklist(self):
        current = self.head
        while (current != None):
            print(current.data, "->", end=" ")
            current = current.next

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

ll = Linkedlist()
ll.append(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

print("Linklist Before Reverse:")
ll.printLinklist()

# ll.reverseLLByIteration()
ll.reverseLLByRecursion()

print("\nLinklist After Reverse:")
ll.printLinklist()