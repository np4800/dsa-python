def findPivotIndex(arr, size):
    
    start = 0
    end = len(arr)
    mid = start + (end - start)//2

    lsum = 0
    rsum = 0
    
    for i in range(mid):
        lsum += arr[i]

    for i in range(size-1, mid, -1):
        rsum += arr[i]

    if lsum > rsum:
        print(lsum,rsum)
        while (lsum > rsum and mid > 0):
           rsum += arr[mid]
           lsum -= arr[mid - 1]
           mid += 1
    elif rsum > lsum:
        print(lsum,rsum)
        while (rsum > lsum and mid < size - 1):
            rsum -= arr[mid+1]
            lsum += arr[mid]
            mid -= 1
    
    if lsum == rsum:
        print(lsum,rsum)
        return mid
    else:
        return -1
    

def main():
    '''
    Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
        The pivot index is 3.
        Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
        Right sum = nums[4] + nums[5] = 5 + 6 = 11
    '''

    print(main.__doc__)

    arr = [2,1,-1] # [ 1, 1, 1, -1, 1, 1, 1 ] [1,7,3,6,5,6]
    ans = findPivotIndex(arr, len(arr))

    print(f"The Pivotal Index is : {ans}")

if __name__ == '__main__':
    main()