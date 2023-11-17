from collections import deque
from queue import LifoQueue
# from inspect import stack

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = Node("head")
        self.size = 0
        # print(f'Head Node: {self.head.data} -- Head.next: {self.head.next} -- head: {self.head}')


    def __str__(self) -> str:
        print(f'{self.head.next}')
        curr = self.head.next
        out = ""
        while curr:
            out += str(curr.data) + "->"
            curr = curr.next
        return out


    def isempty(self):
        return self.size == 0


    def getsize(self):
        return self.size

    
    def peek(self):
        if self.isempty():
            raise Exception('Peeking from empty stack')
        return self.head.next.data


    def pop(self):
        if self.isempty():
            raise Exception('Popping out from empty stack')

        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.data


    def push(self, value):
        node = Node(value)
        # print(f'node.data: {node.data} Node.next: {str(node.next)}')
        # print(f'self.head.value: {self.head.data} -- self.head.next: {str(self.head.next)}')
        node.next = self.head.next ## For 1st element/node it will be None None.
        self.head.next = node ## Head node will store the memory address of current node
        # print(f'After --> node.data: {node.data} Node.next: {str(node.next)} -- node: {node} -- id(node): {hex(id(node))}')
        # print(f'After --> self.head.value: {self.head.data} -- self.head.next: {str(self.head.next)}')
        # print('\n')
        self.size += 1


def stack_using_llist():
    print('Demonstate Stack Concept Using Link List\n')
    stack = Stack()

    for i in range(1,5):
        stack.push(i)
    print(f'Initial Stack: {stack} with size: {stack.getsize()}')

    print('Peek:',stack.peek())

    for _ in range(1,3):
        remove = stack.pop()
        print(f'Pop: {remove}')
    print('Peek:',stack.peek())
    print(f'Remaining Stack: {stack} with size: {stack.getsize()}')


    
def stack_using_queue():
    print('Demonstate Stack Concept Using queue Python Library Module\n')
    stack = LifoQueue(maxsize=3)

    stack.put('A')
    stack.put('B')
    stack.put('C')

    print(f'Yes its {stack.full()}, stack is full with size: {stack.qsize()}')
    print('Elements popped from stack:',stack.get(), stack.get(), stack.get())
    print(f'Yes its {stack.empty()}, stack is empty with size: {stack.qsize()}')


def stack_using_list():
    print('Demonstate Stack Concept Using Python List\n')
    stack=[]
    stack.append('A')
    stack.append('B')
    stack.append('C')
    print('Initial Stack:',stack)
    print('Element popped from stack:',stack.pop(),stack.pop(),stack.pop())
    print('Final Stack:',stack)
    


def stack_using_deque():
    print('Demonstate Stack Concept Using deque Python Library Module\n')
    stack = deque()

    stack.append('A')
    stack.append('B')
    stack.append('C')

    print('Initial Stack:',stack)
    print('Elements popped from stack:', stack.pop(),stack.pop(),stack.pop())
    print('Final Stack:',stack)


def main():
    '''
    --------------------------------------------------------------
    | Problem statement: Program to demonstrate stack            |
    | Input:                                                     |
    | Output:                                                    |
    --------------------------------------------------------------
    '''
    print(main.__doc__)
    print('---------------------------')

    stack_using_list()
    print('\n---------------------------')
    stack_using_deque()
    print('\n---------------------------')
    stack_using_queue()
    print('\n---------------------------')
    stack_using_llist()


if __name__ == '__main__':
    main()