def tree(n):
    if n>0:
        print(n, end=",")
        tree(n-1)
        tree(n-1)
        
def main():
    '''
        Problem: Implement Tree Recursion
        Time Complexity: O(2^n)
    '''
    print(main.__doc__)
    tree(3)

if __name__ == "__main__":
    main()