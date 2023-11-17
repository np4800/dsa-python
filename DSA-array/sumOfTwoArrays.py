def sumOfTwoArrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    carryFwd = 0
    arr3 = []
    ans = 0

    i = n-1
    j = m-1

    while (i>=0 and j>=0):
        val1 = arr1[i]
        val2 = arr2[j]
        sum = val1 + val2 + carryFwd
        carryFwd = sum/10
        sum = sum%10
        arr3.append(sum)
        i -= 1
        j -= 1

    ## First case where normal addintion of the last element of both the arrays
    

def main():
    '''
    Problem Statement: Given two array you have to sum them as follows
    Input: arr1[1,2,3} arr2={9,9}
    Output: {2,2,2}

    '''
    print(main.__doc__)
    arr1 = [1,2,3]
    arr2 = [9,9]

    print(f"The sum of two arrays {arr1} and {arr2} is: {sumOfTwoArrays(arr1,arr2)}")


if __name__ == "__main__":
    main()