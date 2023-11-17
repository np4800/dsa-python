def findMinimumCost(inputExp):
    sizeOfStr = len(inputExp)
    stack=[]
    if sizeOfStr%2 != 0:
        return -1
    for ch in inputExp:
        sizeOfStack = len(stack)
        print(ch)
        if ch == '{':
            stack.append(ch)
        else:
            if sizeOfStack !=0 and stack[sizeOfStack-1] == '{':
                stack.pop()
            else:
                stack.append(ch)
    print(stack, sizeOfStack)    
    ## Stack now contains invalid expression.
    closeBracketCount = 0
    openBracketCount = 0
    while sizeOfStack != 0:
        if (sizeOfStack !=0 and stack[sizeOfStack-1] == '{'):
            openBracketCount += 1
        else:
            closeBracketCount += 1
        stack.pop()

    ans = (closeBracketCount+1)/2 + (openBracketCount+1)/2
    return ans

def main():
    """
    Problem: Given a string 'STR' containing either '}' or '{' is called valid if all the brackets are balanced.
             Formally for each opening bracket there will be a closing bracket
    """

    print(main.__doc__)
    print(findMinimumCost("{{{}}}"))

if __name__ == "__main__":
    main()