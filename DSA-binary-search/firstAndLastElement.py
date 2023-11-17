def firstPosition(arr, size, key):
    start = 0
    end = size - 1
    ans = -1

    while (start <= end):
        mid = start + (end - start)//2
        if arr[mid] == key:
            ans = mid
            end = mid - 1 
        elif arr[mid] > key:
            start = mid + 1
        elif arr[mid] < key:
            end = mid - 1
    return ans

def lastPosition(arr, size, key):
    start = 0
    end = size - 1
    ans = -1

    while (start <= end):
        mid = start + (end - start)//2
        if arr[mid] == key:
            ans = mid
            start = mid + 1 
        elif arr[mid] > key:
            start = mid + 1
        elif arr[mid] < key:
            end = mid - 1
    return ans

def main():
    '''
    First and Last Position of an Element in a sorted array using binary search
    e.g 
    input: [1,2,3,3,5]
    ouput: 2,3
    -------------------------------------------------------
    '''
    print(main.__doc__)

    arry = [1,2,3,3,3,3,3,3,3,3,5]
    key = 3
    first = firstPosition(arry, len(arry), key)
    last = lastPosition(arry, len(arry), key)
    print(f"First, Last occurance of {key} is {first}, {last} in {arry}")

if __name__ == "__main__":
    main()