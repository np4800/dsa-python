def fun(n):
    if n>100:
        print(f"Primary Call: {n}")
        return n-10
    else:
        print(f"Nested Call: {n}")
        return fun(fun(n+11))
        
def main():
    '''
    Problem: Implement Nested Recurssion
    ------------------------------------
    '''
    print(main.__doc__)
    print("\\n")
    print(f"Final Output: {fun(95)}")

if __name__== '__main__':
    main()