"""
Problem:
Infix expression: The expression of the form “a operator b” (a + b) i.e., when an operator is in-between every pair of operands.
Postfix expression: The expression of the form “a b operator” (ab+) i.e., When every pair of operands is followed by an operator.

Example:
Input: A + B * C + D
Output: ABC*+D+
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
    
    def peek(self):
        if (self.isEmpty()):
            return float("-inf")
        return self.root.data
    
    def pop(self):
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        print(f"{popped} is popped from the stack!")


## Main Driver Code
stack = Stack()
infix = "a+b*c-d"
postfix = ""
popped = ""
precedence = { "{": 5, "/":4, "*": 3, "+": 2, "-": 1 } ## BODMAS Rule: 

print("")

for ch in infix:
    if not ch.isalpha():    
        print(f"Precedence Value of scanned {ch}: {precedence[ch]} : Top of Stack is {stack.peek()}")
        if ( stack.isEmpty() or precedence[ch] > precedence[stack.peek()]):
            stack.push(ch)
        # if the precedence of scanned operator is == precendece of top of stack then due to left associativity,
        # top of the stack element has high priority then it has to be popped.
        else:
            while ( not stack.isEmpty() and (precedence[ch] == precedence[stack.peek()] or precedence[ch] < precedence[stack.peek()])): 
                postfix += stack.peek()
                stack.pop()
            stack.push(ch)
    else:
        postfix += ch

while (not stack.isEmpty()):
    postfix += stack.peek()
    stack.pop()

print(f"Postfix Expression: {postfix}")



