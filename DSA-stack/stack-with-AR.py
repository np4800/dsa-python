"""
Problem: Implementing Stacks using Arrays
"""

def isEmpty(stack):
    return len(stack) == 0

def createStack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)
    print(f"{item} Item Pushed")

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)
    return stack.pop()

def peek(stack):
    if (isEmpty(stack)):
        return str(- maxsize -1)
    return stack[len(stack)-1]

## Driver Code
stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(40))

print(f"{peek(stack)} - Is the Top Element in the Stack")
print(f"{pop(stack)} - Popped an Element")




