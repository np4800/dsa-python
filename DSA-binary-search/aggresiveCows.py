def isPossible(stalls, k, mid):
    cowCount = 1
    lastPos = stalls[0]

    for i in range(0,len(stalls)):
        distance = stalls[i] - lastPos

        if distance >= mid:
            cowCount += 1
            if cowCount == k:
                return True
            lastPos = stalls[i]
    return False

def aggresiveCow(stalls, k):
    start = 0
    maxi = -1
    stalls = [4,1,2,3,6]

    ## Sort the stalls list
    s_stalls = sorted(stalls)
    
    for i in range(0,len(s_stalls)):
        maxi = max(maxi, s_stalls[i])

    ## Finding the maximum element from the stalls array will give us a hint 
    ## that the maximum possible distance will be less than the maximum element in the stalls array.

    end = maxi - 1
    ans = -1
    mid = start + (end - start)//2
    ## stalls = 1,2,3,4,6
    ## range = 0,1,2,3,4,5
    
    while start <= end:
        # print(f"mid = {mid}, start={start}")
        if (isPossible(s_stalls,k,mid)):
            ans = mid
            start = mid + 1  ## because we have to get the largest distance
            # print(f"Answer: {ans}")
        else:
            end = mid - 1
        mid = start + (end - start)//2
    
    return ans

def main():
    '''
    Problem Statement: Aggressive Cows
    input:  stalls = [4,1,2,3,6]
    output: 5 [Largest Minimum Distance between the cows]

    Explaination: The maximum number from the list is 6, therefore, the answer will be less than 6.
    Hence, we have to calculate mid between 0 to 5
    -----------------------------------------------------------------------------------------------
    '''
    print(main.__doc__)
    stalls = [4,1,2,3,6]
    k = 2
    maxi_distance = aggresiveCow(stalls,k)

    print(f"Maximum Distance between two cows: {maxi_distance}\n")

if __name__ == '__main__':
    main()