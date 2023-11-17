def shiftElementsInArray(arr,k,n):
    
    # Empty list cannot be assigned with the elements at the desired place in the list, hence create a list of same size of original list.
    temp=[0 for i in range(0,n)]

    for i in range(0,n):
        temp[(i+k)%n] = arr[i] ## Very Very Important formula.

    print(temp)

def main():
    '''
    Problem Statement: Shift Elements in an array by a number; if k=2 then shift elements by 2 places in an array, let it be cyclic.
    Time Complexity:
    Space Complexity:
    
    Input: [3,4,5,1,2]
    Output: For k=2; [1,2,3,4,5]
    '''
    print(main.__doc__)

    arr = [3,4,5,1,2]
    k=2
    n=len(arr)
    shiftElementsInArray(arr,k,n)

if __name__ == '__main__':
    main()