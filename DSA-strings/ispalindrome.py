# Method-1: Using the string syntax pythonic way
def isPalindrome(s):
    return s == s[::-1]

s = 'madam'
print(f"The string {s} is palindrome : {isPalindrome(s)}")

# Method-2: Using Iterative method
def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

s = 'madam'
print(f"Method-2 the string {s} is palindrome : {isPalindrome(s)}")

# Method-3: Using the inbuilt string method - join.reversed(s)
def isPalindrome(fstr):
    rev = ''.join(reversed(fstr))

    if (s == rev):
        return True
    else:
        return False

s = 'madam'
print(f"Method-3 the string {s} is palindrome : {isPalindrome(s)}")



