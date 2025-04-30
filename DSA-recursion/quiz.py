i = 1
def f(n):
    global i
    if (n>=5):
        return n
    n = n + i
    i += 1
    return f(n)
print(f(1))

def foo(n,sum):
    k=0
    j=0
    if (n == 0):
        return
    k=n%10
    j=n//10
    sum = sum+k
    foo(j,sum)
    print(k,end=",")

sum=0
foo(2048,sum)
print(sum)