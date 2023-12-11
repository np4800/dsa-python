class Queue:
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity-1
        self.Q = [None]*capacity

    def isFull(self):
        return self.size == self.capacity
            

    def isEmpty(self):
        return self.size == 0

    def Enqueue(self,item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size += 1
        print(f"{item} enqueued")

    def Dequeue(self):
        if self.isEmpty():
            print("Empty")
            return

        print(f"{self.Q[self.front]} is dequeued from the queue!")
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    def que_front(self):
        if self.isEmpty():
            print("Queue is Empty")
        print(f"Front Element: {self.Q[self.front]}")
    
    def que_rear(self):
        if self.isFull():
            print("Queue is Full")
        print(f"Rear Element: {self.Q[self.rear]}")

def main():
    """
    Problem: Implement QUEUE data structure using Array/List
    """
    print(main.__doc__)
    q1 = Queue(capacity=6)
    q1.Enqueue("A")
    q1.Enqueue("B")
    q1.Enqueue("C")

    print(q1.Q)
    print(f"Is Queue Empty: {q1.isEmpty()}")
    print(f"Is Queue Full : {q1.isFull()}")

    q1.Dequeue()
    print(q1.Q)
    q1.que_front()
    q1.que_rear()

    print(f"Front Element: {q1.Q[q1.front]} - value of Front: {q1.front}")
    print(f"Rear Element : {q1.Q[q1.rear]} - value of Rear : {q1.rear}")
    print(f"Size of Queue: {q1.size}")
    
    

if __name__=="__main__":
    main()