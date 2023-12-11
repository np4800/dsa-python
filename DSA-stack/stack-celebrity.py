def main():
    """
    Problem: Identify who is the celebrity in the given party. This can be identified by the matrix given below:
    [
        0 1 0
        0 0 0
        0 1 0
    ]
    """
    print(main.__doc__)
    M = [[0,1,0], [0,0,0],[0,1,0]]
    stack = [i for i in range(0,len(M))]

    while len(stack) != 1:
        A = stack.pop()
        B = stack.pop()
        # if A -> B => A is not a celebrity
        if (M[A][B]):
            stack.append(B)
        else: # if B -> A => B is not a celebrity
            stack.append(A)

    # Now check the element left in the stack with the following conditions to check if he is a celebrity:
        ## Celebrity knows no one    --> All the row elements for this person in Matrix will be 0
        ## Everybody knows celebrity --> Column element will be 1 except the except the diagonal element
    
    oneCount  = 0
    zeroCount = 0
    
    for i in range(0,len(M)):
        if M[i][stack[0]]:
            oneCount += 1
        
    if oneCount != (len(M)-1):
        return -1
    
    for i in range(0,len(M)):
        if M[stack[0]][i] == 0:
            zeroCount += 1
    
    if zeroCount != len(M):
        return -1
    print(f"The Celebrity is: {stack}")

if __name__ == "__main__":
    main()