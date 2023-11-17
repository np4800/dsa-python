# def func1(n):
#     if (n>0):
#         print(n)
#         func1(n-1)

# def func2(n):
#     if (n>0):
#         func2(n-1)
#         print(n)


# func1(5)
# print("------")
# func2(5)

### Static & Global variable recurrsion functions
# x = 0
# def func(n):
#     global x ## Here the variable is declared as global.
#     if n > 0:
#         x += 1
#         return func(n-1)+x ## the values of the x will be calculated when the function returns the values after all the recurrsion is completed.
#     return 0

# print(func(5))

### Nested Recursion

# def func(n):
#     if n > 100:
#         return n-10
#     return func(func(n+11))

# print(func(99))

### Indirect Recursion

# def funcB(n):
#     pass

# def funcA(n):
#     if n > 0:
#         print(f"A: {n} ")
#         funcB(n-1)

# def funcB(n):
#     if n > 1:
#         print(f"B: {n}")
#         funcA(int(n/2))

# funcB(20)

### Head Recurssion
# def funcH(n):
#     if n > 0:
#         funcH(n-1)
#         print(n)

# funcH(10)

## Tail Recurssion

# def funcT(n):
#     if n > 0:
#         print(n)
#         funcT(n-1)

# funcT(10)

## Function to get the sum of first N natural numbers using recursion

# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return sum(n-1) + n

# print(sum(5))

## Function to get the factorial of first N natural numbers using recursion

# def factorial(n):
#     if n == 0:
#         return 1
#     
#     return factorial(n-1)*n

# print(factorial(5))


## Function to get the power of natural number using recursion
### Time complexity = O(n) as there in this below example there are 9+1 calls therefore for n there will be n calls. Therefore, O(n)
# def pow(m,n):
#     if n == 0:
#         return 1
#     return pow(m,n-1)*m

# print(pow(2,100))

## Function to get the power of natural number using recursion but with reduced multiplication process
# def pow(m,n):
#     if n == 0:
#         return 1
#     if n%2 == 0:
#         return pow(m*m,n/2)
#     return m*pow(m*m,(n-1)/2)

# print(pow(2,100))

## Function to get the factorial of a number
# def fact(n):
#     if n == 0:
#         return 1
#     return n*fact(n-1)

# print(fact(4))

# ## Function to get the fibonacci series of a number
# # 0 1 1 2 3 5 8 13
# # n=8

# def fib(n):
#     if n > 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1)+fib(n-2)

# print(fib(8))

## Function to calculate the sum of elements in an array using recursion
# arr = [1,2,3,4,5]

def sum_of_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        # print(arr)
        return arr[0] + sum_of_array(arr[1:])  ## Slicing is the trick here and remove the element from the array in every recursive call till the base condition

arr = [1,2,3,4,5]
N = len(arr)
print(f"Sum = {sum_of_array(arr)}")

## Function to calculate the exponent
def pow(x,n):
    if n == 0:
        return 1
    return x * pow(x,n-1)

print(f"Exponent = {pow(2,6)}")


