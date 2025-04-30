# Implement QUEUE using Linklist data structure [FIFO]
# Date: 30-11-2024
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        print(f"{self.rear.data} IS ENQUEUED")

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def isEmpty(self):
        return self.front is None

    def que_rear(self):
        return "Queue is Empty" if self.rear is None else self.rear.data

    def que_front(self):
        return "Queue is Empty" if self.front is None else self.front.data

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


def main():
    """
    Problem: Implement QUEUE using Linklist data structure
    Date: 30-11-2024
    """
    print(main.__doc__)
    q = Queue()
    print(f"Is Queue Empty? {q.isEmpty()}")
    print(f"REAR  ELEMENT: {q.que_rear()}")
    print(f"FRONT ELEMENT: {q.que_front()}")

    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")

    print(f"REAR  ELEMENT: {q.que_rear()}")
    print(f"FRONT ELEMENT: {q.que_front()}")

    q.dequeue()
    q.dequeue()

    print(f"REAR  ELEMENT: {q.que_rear()}")
    print(f"FRONT ELEMENT: {q.que_front()}")

    q.dequeue()
    print(f"REAR  ELEMENT: {q.que_rear()}")
    print(f"FRONT ELEMENT: {q.que_front()}")

if __name__=="__main__":
    main()

# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None
# class Queue:
#     def __init__(self) -> None:
#         self.front = None ## TOP  element in the STACK which is LAST  element in QUEUE
#         self.rear = None ## LAST element in the STACK which is FIRST element in QUEUE

#     def enqueue(self,data):
#         newNode = Node(data)
#         if self.rear == None:
#             self.front = self.rear = newNode
#         self.rear.next = newNode
#         self.rear = newNode
#         print(f"{self.rear.data} IS ENQUEUED")
    
#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is Empty"
#         temp = self.front
#         self.front = temp.next
#         if self.front == None:
#             self.rear = None


#     def isEmpty(self):
#         return self.front == self.rear == None

#     def que_rear(self):
#         return "Queue is Empty" if self.rear == self.front == None else self.rear.data
    
#     def que_front(self):
#         return "Queue is Empty" if self.rear == self.front == None else self.front.data

# def main():
#     """
#     Problem: Implement QUEUE using Linklist data structure
#     """
#     print(main.__doc__)
#     q = Queue()
#     print(f"Is Queue Empty? {q.isEmpty()}")
#     print(f"REAR  ELEMENT: {q.que_rear()}")
#     print(f"FRONT ELEMENT: {q.que_front()}")

#     q.enqueue("A")
#     q.enqueue("B")
#     q.enqueue("C")

#     print(f"REAR  ELEMENT: {q.que_rear()}")
#     print(f"FRONT ELEMENT: {q.que_front()}")

#     q.dequeue()
#     q.dequeue()

#     print(f"REAR  ELEMENT: {q.que_rear()}")
#     print(f"FRONT ELEMENT: {q.que_front()}")

#     q.dequeue()
#     print(f"REAR  ELEMENT: {q.que_rear()}")
#     print(f"FRONT ELEMENT: {q.que_front()}")


# if __name__=="__main__":
#     main()


# # ssh -i EVA-for-GL-ED25519.pem ec2-user@i-0cdbdc97d0c4d4481 -L 9999:172.16.143.135:22