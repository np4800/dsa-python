"""
Problem-1: Implment 2-stack with a single array
"""
import math
class Twostack:
    def __init__(self,n) -> None:
        self.size = n
        self.arr = [None] * n ## This is the trick here
        self.top1 = math.floor(n/2)+1
        self.top2 = math.floor(n/2)

    def push1(self,data):
        if self.top1 > 0:
            self.top1 = self.top1 - 1
            self.arr[self.top1] = data
        else:
            print(f"Stack-1 is overflow by element: {data}")
    
    def push2(self,data):
        if self.top2 < self.size - 1:
            self.top2 = self.top2+1
            self.arr[self.top2] = data
        else:
            print(f"Stack-2 is overflow by element: {data}")
    
    def pop1(self):
        if self.top1 <= self.size/2:
            popped = self.arr[self.top1]
            self.arr[self.top1] = None
            print(f"{popped} is popped")
            self.top1 = self.top1+1
        else:
            print(f"Stack-1 is empty now")

    def pop2(self):
        if self.top2 > self.size/2:
            popped = self.arr[self.top2]
            print(f"{popped} is popped from Stack-2")
            self.arr[self.top2] = None
            self.top2 = self.top2 - 1
        else:
            print(f"Stack-2 is empty now")

ts = Twostack(6)
print("Implement 2-Stack in a single array")

print(f"Empty Array:    {ts.arr}")
print(f"Size of Array:  {ts.arr.__len__()}")
print("-----Push Operation------")
ts.push1("A")
ts.push1("B")
ts.push1("C")
ts.push1("N")
ts.push1("D")
print(f"Top-1 is at: {ts.top1}")
print(f"Elements in Stack-1: {ts.arr}")
print("--------------------------------------")
ts.push2(10)
ts.push2(20)
ts.push2(30)
ts.push2(50)
print(f"Top-2 is at: {ts.top2}")
print(f"Elements in Stack-2: {ts.arr}")
print("-----Popped Operation------")
ts.pop1()
ts.pop1()
ts.pop1()
ts.pop1()
ts.pop1()
print("------------------------------")
print(f"Elements in Stack-1: {ts.arr}")
ts.pop2()
ts.pop2()
ts.pop2()
print("------------------------------")
print(f"Elements in Stack-1: {ts.arr}")
