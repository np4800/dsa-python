def reverseArray(arr,m):
    start = m-1
    end = len(arr)-1

    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

    print(arr)


def main():
    '''
    Reverse the given Array
    '''
    print(main.__doc__)

    arr = [4,2,6,8,1]
    reverseArray(arr,3)

if __name__ == "__main__":
    main()