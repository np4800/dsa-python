def sortedInsert(inputStack,element):
    sizeOfStack = len(inputStack)
    if (sizeOfStack == 0 or (inputStack[sizeOfStack-1]<element)):
        inputStack.append(element)
        return
    top = inputStack.pop()
    sortedInsert(inputStack,element)
    inputStack.append(top)


def sortStack(inputStack):
    sizeOfStack = len(inputStack)
    if sizeOfStack == 0:
        return
    num = inputStack.pop()
    sortStack(inputStack)
    sortedInsert(inputStack,num)

def main():
    """
    Problem: Sort a Stack using recurrsion
    Input:  [7,9,3,0]
    Output: [0,3,7,9]
    """
    print(main.__doc__)
    inputStack = [7,9,3,0]
    print(f"Stack before sort: {inputStack}")
    sortStack(inputStack=inputStack)
    print(f"Stack after sort:  {inputStack}")

if __name__ == "__main__":
    main()