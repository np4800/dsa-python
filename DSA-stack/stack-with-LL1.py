class StackNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.root = None
        print(f"{self.root}")

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        print(f"Root: {self.root}")
        print(f"NewNode Next: {newNode.next}")
        self.root = newNode
        print(f"NeNode: {newNode} : {newNode.data} : {newNode.next}")
        print(f"{data} is pushed to stack!")

    def peek(self):
        if (self.isEmpty()):
            return float("-inf")
        print(f"Top of Stacks Next pointer value: ${self.root.next}")
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
