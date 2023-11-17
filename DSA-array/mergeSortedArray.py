def mergeSort(arr1, arr2):
    n_arr1 = len(arr1)
    m_arr2 = len(arr2)
    i = 0
    j = 0
    arr3 = []

    print(f"Array 1: {n_arr1} and Array 2: {m_arr2}")
    while(i<n_arr1 and j < m_arr2):
        print("here")
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while (i < n_arr1):
        arr3.append(arr1[i])
    
    while (j < m_arr2):
        arr3.append(arr2[j])

    print(arr3)


def main():
    '''
    Merge Sorted Array
    Input: arr1=[1,3,5,7,9] arr2=[2,4,6,8]
    Output: arr3=[1,2,3,4,5,6,7,8,9]
    '''
    print(main.__doc__)

    arr1=[1,3,5,7,9] 
    arr2=[2,4,6,8]

    mergeSort(arr1, arr2)
    

if __name__ == '__main__':
    main()