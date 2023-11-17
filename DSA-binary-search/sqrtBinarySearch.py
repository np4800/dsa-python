def sqrt(num, precision):
    ans = sqrtInt(num)
    factor = 1

    for i in range(0,precision):
        j=ans
        factor = factor / 10
        while (j * j) < num:
            j = j + factor
    ans = j
    return ans

def sqrtInt(num):
    start = 0
    end = num
    ans = -1

    while(start < end):
        mid = start + (end - start)//2
        if (mid * mid) > num:
            end = mid - 1
        elif (mid * mid) < num:
            ans = mid
            start = mid + 1
        elif (mid * mid) == num:
            ans = mid
    return ans


def main():
    '''
    Square Root of a number using binary search
    **** Search Space Concept
    '''
    print(main.__doc__)
    number= 37
    ans = sqrt(number,3)
    print(f"Square Root of {number} is: {ans}")


if __name__ == "__main__":
    main()