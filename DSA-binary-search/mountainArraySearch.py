def mountainArraySearch(arr, size):
    start = 0
    end = size - 1
    mid = start + (end - start)//2

    # while not (arr[mid+1] < arr[mid] and arr[mid-1] < arr[mid]):
    #     if arr[mid] < arr[mid - 1]:
    #         start = mid - 1
    #     else:
    #         end = mid

    while (start < end):
        if arr[mid] < arr[mid+1]:
            start = mid + 1
        else:
            end = mid
        mid = start + (end - start)//2

    return start


def main():
    '''
    Moutain Array Search for peak element on the mountain array.
    i/p: 1,2,3,1,0
    o/p: 3
    Time Complexity = O(log n)
    '''
    arr = [1,2,4,4,5,2,1,0]
    ans = -1
    ans = mountainArraySearch(arr, len(arr))

    print(f"Peak element = {ans}")

if __name__ == "__main__":
    main()