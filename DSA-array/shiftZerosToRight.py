from unicodedata import name


def shiftZeros(arr):
    non_zero = 0
    for i in range(0,len(arr)):
        print(f"arr[non_zero:{non_zero}]={arr[non_zero]} <---> arr[i:{i}]={arr[i]}")
        if arr[i] != 0:
            temp = arr[non_zero]
            arr[non_zero] = arr[i]
            arr[i] = temp
            non_zero += 1
    
    print(arr)


def main():
    '''
    Problem Statement: Shift all zeros to right in a array
    Input: arr = [0,1,0,3,12]
    Output: arr = [1,3,12,0,0]
    '''

    print(main.__doc__)

    arr = [0,1,0,3,12]

    shiftZeros(arr)

if __name__ == '__main__':
    main()