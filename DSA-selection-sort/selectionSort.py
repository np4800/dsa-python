def selectionSort(arr):
    temp = -1
    for i in range(0, len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[minIndex]
        arr[minIndex] = arr[i]
        arr[i] = temp

    print(f"Array sorted with selection sort: {arr}")

def main():
    '''
    Problem Statement: Selection Sort
    input:  [22,25,11,64]
    output: [11,22,25,64]

    Time Complexity: O(n^2)
    -----------------------------------------------------------------------------------------------
    '''

    print(main.__doc__)

    arr = [22, 25, 11, 64]
    selectionSort(arr)

if __name__ == '__main__':
    main()