def main():
    """
    You are given an array ARR of integers of length N. Your task is to find the next smaller element for each of the array elements.
    Next smaller element for an array element is the first element in the right of that element which has a value strictly smaller than the element.
    If for any array element the next smaller element does not exists, you should print -1 for that array element.
    
    Input:  [2,3,1]
    Output: [-1,1,-1]
    """
    print(main.__doc__)
    stack = [-1]
    ans = [-1,-1,-1,-1]
    inputArr = [2,1,4,3]


    for i in range(len(inputArr)-1,-1,-1):
        sizeOfStack = len(stack)
        current = inputArr[i]
        print("TopOfStack: ",stack[sizeOfStack-1] ," index: ", i, " current: ",current)
        while (stack[sizeOfStack-1] >= current):
            stack.pop()
            sizeOfStack = len(stack)
            print(stack)
        ans[i] = stack[sizeOfStack-1]
        stack.append(current)
        # print(stack,"---",ans)
    return ans

if __name__ == "__main__":
    print(main())