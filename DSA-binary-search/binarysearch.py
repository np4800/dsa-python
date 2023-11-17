def binarysearch(arr, size, key):
    start = 0
    end = size - 1
 
    while (start < end):
        # conventional method: in this you have the problem if the integer value is maximum in start and end = 2^32
        # mid = (start + end) // 2

        # therefore, we apply chalaki
        mid = start + (end - start)//2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

def main():
    '''
        Binary Search: It follows the O(log n) time Complexity
    '''

    print(main.__doc__)

    even = [2,4,6,8,10,12]
    key = 10

    ans = binarysearch(even, len(even), key)
    print(f"The element {key} is found at index {ans} in the list {even}")

    odd = [1,3,5,7,9]
    key = 7
    ans = binarysearch(odd, len(odd), key)
    print(f"The element {key} is found at index {ans} in the list {odd}")

if __name__ == "__main__":
    main()