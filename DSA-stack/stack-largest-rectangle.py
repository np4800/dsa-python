def nextSmallerElement(inputArr,n):
    stack = [-1]
    ans = [ -1 for i in range(0,n)]

    for i in range(len(inputArr)-1,-1,-1):
        sizeOfStack = len(stack)
        current = inputArr[i]
        # print("TopOfStack: ",stack[sizeOfStack-1] ," index: ", i, " current: ",current)
        while ( stack[sizeOfStack-1] != -1 and inputArr[stack[sizeOfStack-1]] >= current):
            stack.pop()
            sizeOfStack = len(stack)
            # print(stack)
        ans[i] = stack[sizeOfStack-1]
        stack.append(i)
        # print(stack,"---",ans)
    return ans

def prevSmallerElement(inputArr,n):
    stack = [-1]
    ans = [ -1 for i in range(0,n)]

    for i in range(0,len(inputArr)):
        sizeOfStack = len(stack)
        current = inputArr[i]
        # print("TopOfStack: ",stack[sizeOfStack-1] ," index: ", i, " current: ",current)
        while ( stack[sizeOfStack-1] != -1 and inputArr[stack[sizeOfStack-1]] >= current):
            stack.pop()
            sizeOfStack = len(stack)
            # print(stack)
        ans[i] = stack[sizeOfStack-1]
        stack.append(i)
        # print(stack,"---",ans)
    return ans

def largestRectangleArea(heights):
    n = len(heights)
    next = []
    next = nextSmallerElement(heights,n)

    prev = []
    prev = prevSmallerElement(heights,n)

    area = 1

    for i in range(0,len(heights)):
        l = heights[i]
        b = next[i] - prev[i] - 1
        if (next[i] == -1):
            next[i] = n

        newArea = l * b
        area = max(area, newArea)
    return area

def main():
    """
    Problem: Given an array of integers heights representing the historgram's bar height where width of each bar is 1, return the area
    of the largest rectangle in the histogram
    Input : [2,1,5,6,2,3]
    Output: 10 (Given the breadth = 1 unit)
    """
    print(main.__doc__)
    print("Program Starts from here ...")
    H = [2,1,5,6,2,3]
    print(f"LARGEST AREA OF RECTANGLE: {largestRectangleArea(H)}")

if __name__ == "__main__":
    main()