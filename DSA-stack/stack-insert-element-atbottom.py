def pushAtBottom(inputStack,x):
    sizeOfStack = len(inputStack)

    if sizeOfStack == 0:
        inputStack.append(x)
        return
    
    element = inputStack.pop()
    pushAtBottom(inputStack,x)
    inputStack.append(element)

def main():
    """ 
    Problem: Insert an element in a stack at the end of it using recurrsion.
    Input:  [7,2,0,0]
    Output: [9,7,2,0,0]
    """
    print(main.__doc__)
    inputStack = [7,2,0,0]
    x = 9
    print(f"Before Inserting: {inputStack}")
    print("After Inserting element 9 at the bottom of stack")
    pushAtBottom(inputStack=inputStack,x=x)
    print(f"After Inserting: {inputStack}")


if __name__ == "__main__":
    main()
    