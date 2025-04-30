# Global Variable
s = 1

def e(x,n):
    global s
    if (n==0):
        return s
    s = 1 + x/n*s
    return e(x,n-1)

def main():
    '''
    Problem: Implement Taylor Series using Honner Rule:
    e(x,4) = 1 + x/1 [1 + x/2[1 + x/3[1 + x/4]]]

    e^x = 1 + x/1 + x^2/2! + x^3/3! + x^4/4! + .... + nth term
    e.g e(x,n) => e(1,10)=2.71828

    This will reduce the # of multiplications from the previous recursive method.

    Time Complexity: O(n)
    '''
    print(main.__doc__)
    print(f"Result of e(1,4): {e(1,10)}")

if __name__=='__main__':
    main()