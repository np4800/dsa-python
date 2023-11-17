def bubbleSort(arr,n):
    for i in range(1,n):
        isSwapped = False
        for j in range(0, n-i):
            temp = -1
            if arr[j] > arr[j+1]:
                print("Switch to check if there is a swap")
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                isSwapped = True
        
        if not isSwapped:
            print("Already Sorted Array")
            break

    print(f"The array is sorted by Bubble Sort Algorithm: {arr}")

def main():
    '''
    Problem Statement: Bubble Sort
    Time Complexity: O(n^2) because: 1+2+...(n-2)+(n-1) = n(n-1)/2 = n^2
    Space Complexity: O(1) because = there are no variables as such, therefore constant space compleity
    -------------------------------
    '''
    print(main.__doc__)
    arr = [7,6,1,9,14,10]
    # arr = [1,2,3,4,5,6]
    n = len(arr)
    bubbleSort(arr,n)

if __name__ == '__main__':
    main()