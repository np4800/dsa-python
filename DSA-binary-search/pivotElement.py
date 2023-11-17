def getPivot(arr, size):
    start = 0
    end = size - 1

    while (start < end):
        mid = start + (end - start)//2
        if arr[mid] >= arr[0]:
            start = mid + 1
        else:
            end = mid
    return start ## This will return the index

def main():
    '''
    Get the pivot element. For Example:
    i/p: [8,10,17,1,3]
    o/p: 1
    '''
    print(main.__doc__)
    arr = [8,10,17,1,3]
    ans = getPivot(arr, len(arr))
    print(f"Pivot Element: {ans}")


if __name__ == "__main__":
    main()