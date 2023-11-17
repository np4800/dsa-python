def insertionSort(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            ## You need to swap the numbers bigger number will go on right
            arr[j+1] = arr[j]
            j = j - 1
        ## else: you have to proceed as it is already sorted
        arr[j+1] = key

    print(f"{arr}")


def main():
    '''
    Problem Statement: Insertion Sort
    Hint: Analogy with cards. Take 1st card and compare the next 
    incoming card with the current card in your hand and try to 
    place incoming card on left if it less than current card els
    on right if greater than current card in hand.

    Time Complexity : O(n^2)
    Space Complexity:
    '''
    print(main.__doc__)
    arr = [10,1,7,4,8,2,11]
    # arr = [4,12,11,20]
    insertionSort(arr, len(arr))

if __name__ == '__main__':
    main()