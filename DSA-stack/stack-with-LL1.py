class StackNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print(f"{data} is pushed to stack!")

    def peek(self):
        if (self.isEmpty()):
            return float("-inf")
        return self.root.data

    def pop(self):
        if(self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        print(f"{popped} is popped out fromt the stack")

print(f"Input the Elements")
stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")

print(f"{stack.peek()} is the top Element in the Stack")
stack.pop()
stack.pop()
stack.pop()
print(f"{stack.peek()} is the top Element in the Stack")
