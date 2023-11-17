## Method 1 - Reverse a string

def reverse1(s):
    str1 = ""
    for chr in s:
        ## Here there is a technique - if you swap the chr + str1 --> str1 + chr; then it will return original string. Intelligent huh !!
        str1 = chr + str1
    return str1

s = "GeeksforGeeks"
print(f"Given String: {s}")
print(f"Reversed String with Loop: {reverse1(s)}")


## Method 2: Recursion

def reverse2(s):
    if len(s) == 0:
        return s
    return reverse2(s[1:]) + s[0]

s = "Geeksforgeeks"
print(f"Reverse string with Recurssion: {reverse2(s)}")


## Method 3: Extended Slice (python) syntax

def reverse3(s):
    string = s[::-1]
    return string

print(f"Reverse string with Extended Slice(python): {reverse3(s)}")
