from timeit import default_timer as timer
from datetime import timedelta

F=[]

def fib_memo(n):
    if (n<=1):
        F[n] = n
        return n
    else:
        if (F[n-2]==1):
            F[n-2] = fib_memo(n-2)
        if (F[n-1] == -1):
            F[n-1] = fib_memo(n-1)
        return F[n-2]+F[n-1]
def fib(n):
    if (n<=1):
        return n
    return fib(n-2)+fib(n-1)

def main():
    '''
    Problem: Print the nth term in Fibonacci Series
    e.g: For fib(5) = 5
    Fibonacci: 0 1 1 2 3 5

    Normal Recursion: 
    Time Complexity: O(2^n)

    Use Memoiztion:
    Time Complexity: O(n) as good as loops
    ---------------------------------------------------
    '''
    global F

    n=input("Input N: ")
    n=int(n)
    F = [-1 for i in range(n)]

    print(main.__doc__)

    start = timer()
    print("With Normal Recursion:")
    print(f"nth term in Fibonacci series -> fib({n}): {fib(n)}")
    end = timer()
    print(f"Time Elasped: {timedelta(seconds=end-start)}")
    
    print("---------------------------------------------------")

    start = timer()
    print("With Memoization:")
    print(f"nth term in Fibonacci series -> fib_memo({n}): {fib_memo(n)}")
    end = timer()
    print(f"Time Elasped: {timedelta(seconds=end-start)}")
    print(f"Memoization Table Content: {F}")

if __name__ == '__main__':
    main()