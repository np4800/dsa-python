## Date: 24-11-2024

class Queue:
    def __init__(self) -> None:
        self.front = self.rear = -1
        self.queue = []
        self.size = 0

    def isQueueEmpty(self):
        return (self.front == -1 and self.rear == -1)
    
    def isQueueFull(self):
        return (self.rear == self.size-1)
    
    def enqueue(self,data):
        if self.isQueueEmpty():
            self.front +=1
            self.rear += 1
            self.queue.append(data)
        elif self.isQueueFull():
            print("Queue is Full")
        elif not self.isQueueFull():
            self.rear += 1
            self.queue.append(data)
        return self.queue
    
    def dequeue(self):
        if self.isQueueEmpty():
            print("Queue is Empty")
        else:
            self.front += 1
            self.queue.pop(0)
        return self.queue

q = Queue()
q.size = 4
print(f"BEFORE: Status of Queue: {q.queue}")
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
print(f"AFTER: Status of Queue: {q.queue}")
q.dequeue()
q.dequeue()
print(f"AFTER DEQUEUE: Status of Queue: {q.queue}")