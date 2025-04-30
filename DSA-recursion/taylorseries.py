## Global/Staic Varaible
p = 1
f = 1

def e(x,n):
    global p
    global f
    if (n==0):
        return 1
    print(f"Calling Time: {p,f,n}")    
    r = e(x,n-1)
    p = p*x
    f = f*n
    print(f"Return Time: {p,f,n}")
    return r+p/f



def main():
    '''
    Problem: Implement Taylor Series.
    e^x = 1 + x/1 + x^2/2! + x^3/3! + x^4/4! + .... + nth term
    e.g e(x,n) => e(1,4)=2.7123
    ----------------------------------------------------------
    '''

    print(main.__doc__)
    print(f"e(1,10) -> {e(1,10)}")

if __name__=="__main__":
    main()