def toh(n, A, B,C):
    if (n>0):
        toh(n-1,A,C,B)
        print(f"{A} -> {C}")
        toh(n-1,B,A,C)

def main():
    '''
    Problem: Solve tower of Hanoi recurssively
    For n=3; show the steps in the output
    ------------------------------------------
    '''
    print(main.__doc__)
    print("Following steps are required to solve Tower of Hanoi for n=3")
    toh(3,1,2,3)

if __name__=='__main__':
    main()