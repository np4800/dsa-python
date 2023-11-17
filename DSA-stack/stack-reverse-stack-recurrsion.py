def pushAtBottom(inputStack,element):
    sizeOfStack = len(inputStack)
    if sizeOfStack == 0:
        inputStack.append(element)
        return
    x = inputStack.pop()
    pushAtBottom(inputStack,element)
    inputStack.append(x)

def reverseStack(inputStack):
    sizeOfStack = len(inputStack)
    if sizeOfStack == 0:
        return
    
    element = inputStack.pop()
    reverseStack(inputStack)
    pushAtBottom(inputStack,element)
    print(inputStack)

def main():
    """
    Problem: Reverse Stack using recurssion
    Input:  [7,9,0,1]
    Output: [1,0,9,7]
    Time Complexity: O(n^2)
    """
    print(main.__doc__)
    inputStack = [1,2,3,4]
    print(f"Stack Before: {inputStack}")
    reverseStack(inputStack=inputStack)
    print(f"Stack After:  {inputStack}")

if __name__ == "__main__":
    main()


# def reverseStack(inputStack,outputStack):
#     sizeOfStack = len(inputStack)

#     if sizeOfStack == 0:
#         return
#     element = inputStack.pop()
#     outputStack.append(element)
#     reverseStack(inputStack,outputStack)

# def main():
#     """
#     Problem: Reverse Stack using recurssion
#     Input:  [7,9,0,1]
#     Output: [1,0,9,7]
#     """
#     print(main.__doc__)
#     inputStack = [1,2,3,4]
#     outputStack = []
#     print(f"Stack Before: {inputStack}")
#     reverseStack(inputStack=inputStack,outputStack=outputStack)
#     print(f"Stack After:  {outputStack}")

# if __name__ == "__main__":
#     main()