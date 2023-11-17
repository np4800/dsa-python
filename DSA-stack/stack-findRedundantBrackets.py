def findRedundantBrakets(inputExpression):
    stack = []
    isRedundant = True
    for ch in inputExpression:
        if ch == "(" or ch == "{" or ch =="[" or ch == "/" or ch == "+" or ch == "*" or ch == "-":
            stack.append(ch)
        else:
            if ch == "}" or ch == "]" or ch == ")":
                sizeOfStack = len(stack)
                top = stack[sizeOfStack-1]
                if top == "+" or top == "-" or top == "/" or top == "*":
                    isRedundant = False
                    stack.pop()
                    stack.pop()
                else:
                    isRedundant = True

    return isRedundant

def main():
    """
    Problem: Find the redundant brackets in a given expression
    Input: (a*b)
    Output: True
    """
    print(main.__doc__)
    inputExpression = "(a*(a+b))"
    print(f"The expression: {inputExpression} has redundant brackets?: {findRedundantBrakets(inputExpression=inputExpression)}")


if __name__=="__main__":
    main()