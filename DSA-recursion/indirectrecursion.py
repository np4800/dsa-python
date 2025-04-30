def indirectsub(n):
    if n>1:
        print(n, end=" ")
        indirect(n/2)

def indirect(n):
    if n>0:
        print(n, end=" ")
        indirectsub(n-1)
def main():
    '''
    Problem: Indirect Recursion
    funA(n) -> funB(n) -> funA(n)
    -----------------------------
    '''
    print(main.__doc__)
    print("Output:")
    indirect(20)

if __name__== "__main__":
    main()