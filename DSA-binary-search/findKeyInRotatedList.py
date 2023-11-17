import pivotElement

def findElement(arr, start, end, key):
    start = start
    end = end
    
    while (start <= end):
        mid = start + (end - start)//2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            start = mid + 1
        elif arr[mid] < key:
            end = mid - 1
    return -1 

def main():
    '''
    Find and element in the rotated array. For example:
    i/p: [8,10,17,1,2,3]
    o/p: 4
    '''

    print(main.__doc__)
    
    arr = [8,10,17,1,2,3]
    key = 2
    size = len(arr)

    pivot = pivotElement.getPivot(arr=arr,size=len(arr))
    print(f"Pivot Element: {pivot}")

    if arr[pivot] <= key and key <= arr[size - 1]:
        ans = findElement(arr, pivot, len(arr) - 1, key)
    else:
        ans = findElement(arr, 0, pivot-1, key)

    print(f"Key Element found at: {ans}")


if __name__ == "__main__":
    main()