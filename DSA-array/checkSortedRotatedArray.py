def isSortedRotatedArray(arr,n):
    ## we will count the number of pair in the given array including the cyclic situtation as well.
    ## for the given array arr[i-1] > arr[i] then increament the count. And this could should be 0 or 1 else more than 1 pair exists
    ## and this violates the rule

    count = 0

    for i in range(1, n):
        if arr[i-1] > arr[i]:
            count += 1

    ## Cyclic case: to check if the last element in the array is greater than first element (edge case)
    if arr[n-1] > arr[0]:
        count += 1

    if count == 1:
        return True
    
    return False

def main():
    '''
    Problem Statement: Given an array check if the array is sorted and rotated array
    Hint: Check the pivot element

    Input: arr=[3,4,5,1,2]
    Output: True
    '''
    print(main.__doc__)

    # arr = [3,4,5,1,2]
    arr = [1,1,1,1,1]
    print(f"The given array {arr} is: {isSortedRotatedArray(arr,len(arr))}")


if __name__ == "__main__":
    main()