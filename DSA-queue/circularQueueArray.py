class CircularQueue:
    def __init__(self,size) -> None:
        self.front = self.rear = -1
        self.size = size
        self.queue = [None for i in range(size)]

    def isQueuFull(self):
        if (self.front != 0 and self.rear == (self.front-1)%(self.size-1)):
            print("Circular Queue is Full!")
            return True
        else:
            return False
            
    def isQueueEmpty(self):
        return (self.front == -1 and self.rear == -1)
        

    def enqueue(self,data):
        ## Check if the Queue is empty by checking the pointer indexes of array F & R == -1
        if self.isQueueEmpty():
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = data 
        elif not self.isQueuFull():    
            if (self.front != 0 and self.rear == self.size-1):
                self.rear = 0
                self.queue[self.rear] = data
            else:
                self.rear += 1
                self.queue[self.rear] = data
        return self.queue

    def dequeue(self):
        if (self.front == (self.size - 1) and self.rear == (self.size-1)):
            self.front = -1
            self.rear  = -1
        else: 
            self.front += 1
            self.queue[self.front-1] = None
        return self.queue


cq = CircularQueue(4)
print(f"BEFORE: Status of Circular Queue: {cq.queue}")
cq.enqueue("A")
cq.enqueue("B")
cq.enqueue("C")
cq.enqueue("D")
print(f"AFTER: Status of Circular Queue: {cq.queue}")
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
print(f"AFTER DEQUEUE: Status of Circular Queue: {cq.queue}")


# class CircularQueue:
#     def __init__(self,size):
#         self.front = self.rear = -1
#         self.size = size
#         self.queue = [None for i in range(size)]

#     def enqueue(self,data):
#         # Check if the circular queue is full: the rear pointer is just before the front pointer in the queue
#         if ((self.rear+1) % self.size == self.front):
#             print("Queue is Full \n")
#         # Check if th queue is empty: Rear and Front pointer should point to -1
#         elif (self.front == -1):
#             self.front = 0
#             self.rear = 0
#             self.queue[self.rear] = data
#         else:
#             self.rear = (self.rear + 1) % self.size
#             self.queue[self.rear] = data

#     def dequeue(self):
#         if (self.front == -1):
#             print("Queue is Empty \n")
#         # If the queue has only one element
#         elif (self.front == self.rear):
#             temp = self.queue[self.front]
#             self.queue[self.front] = None
#             self.front = -1
#             self.rear = -1
#             return temp
#         else:
#             temp = self.queue[self.front]
#             self.queue[self.front] = None
#             self.front = (self.front +1) % self.size
#             return temp


# def main():
#     """
#     Problem: Implement CIRCULAR QUEUE using Array
#     """
#     print(main.__doc__)
#     q = CircularQueue(5)
#     print(q.queue)
#     q.enqueue("A")
#     q.enqueue("B")
#     q.enqueue("C")
#     q.enqueue("D")
#     q.enqueue("E")
#     print(f"Dequeued: {q.dequeue()} | Front Index: {q.front} | Rear Index: {q.rear}")
#     q.enqueue("F")
#     print(q.queue)


# if __name__=="__main__":
#     main()