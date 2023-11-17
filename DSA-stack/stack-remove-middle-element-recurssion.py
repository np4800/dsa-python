class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
 
    def style_text(code):
        return "\33[{code}m".format(code=code)
 
    def color_text(code):
        return "\33[{code}m".format(code=code)
 
def deleteMiddleElement(inputStack, count, size):
    
    middleElement = (size//2)
    print(inputStack, count, middleElement)
    if count == middleElement:
        inputStack.pop()
        return 
    
    prevElement = inputStack[-1]
    inputStack.pop()
    deleteMiddleElement(inputStack, count+1, size)
    inputStack.append(prevElement)


## Driver Code
def main():
    """
    Problem: Remove the middle element from the existing stack using stack - use recursion todo this.
    Input  = [5,6,7,8,2]
    Output = [5,6,8,2]
    """
    print(main.__doc__)
    inputStack = [5,6,7,8,2]
    print(f"Before Removal: {inputStack}")
    deleteMiddleElement(inputStack,0,len(inputStack))
    print(f"After Removal: {inputStack}")
    example_ansi = ANSI.background(
    97) + ANSI.color_text(35) + ANSI.style_text(4) + " TESTE ANSI ESCAPE CODE"
    print(example_ansi)


if __name__ == "__main__":
    main()