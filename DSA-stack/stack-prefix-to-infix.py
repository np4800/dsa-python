"""
Given a Prefix expression, convert it into a Infix expression.

Input :  Prefix :  *+AB-CD
Output : Infix : ((A+B)*(C-D))

Input :  Prefix :  *-A/BC-/AKL
Output : Infix : ((A-(B/C))*((A/K)-L))
"""

class StackNode:
    def __init__(self,data) -> None:
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
        # print(f"{data} is pushed to the stack!")
    
    def peek(self):
        if (self.isEmpty()):
            return float("-inf")
        return self.root.data
    
    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        # print(f"{popped} is popped!")
        return popped

def prefixToInfix(prefix):
    infix = ""
    for ch in reversed(prefix):
        if ch.isalpha():
            stack.push(ch)
        else:
            tempinfix = "("
            tempinfix += stack.pop()
            tempinfix += ch
            tempinfix += stack.pop()
            tempinfix += ")"
            stack.push(tempinfix)
    
    while not stack.isEmpty():
        infix += stack.pop()

    return infix


## Main Driver Code
if __name__=="__main__":
    stack = Stack()
    prefix = "*+AB-CD"
    print(f"Prefix String: {prefix}")
    print(f"Infix  String: {prefixToInfix(prefix)}")

    # stack.push("A")
    # stack.push("B")
    # print(f"Top of Stack: {stack.peek()}")
    # stack.pop()



