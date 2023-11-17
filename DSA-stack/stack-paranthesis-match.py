"""
Problem: 2 - Implement Paranthesis matching in a given algebric expression using stack data structure
e.g ((a+b)*(b+c))
Return: True if opening and closing parenthesis match
"""

class StackNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self,data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print(f"{data} is pushed to stack")

    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        print(f"{popped} is popped")
    
    def peek(self):
        if(self.isEmpty()):
            return float("-inf")
        return self.root.data

def isParanthesisMatch():
    pass

stack = Stack()
expression = "((a+b)*(b-c)))"

for char in expression:
    if char == '(' or char == '{' or char == '[':
        stack.push(char)

    if char == ')' or char == '}' or char == ']':
        if (stack.isEmpty()):
            print(f"Stack is empty, hence no matching parenthesis")
        else:
            print(f"{expression} has matching paranthesis: {stack.isEmpty()}")
        stack.pop()






