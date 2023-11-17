class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None


def main():
    '''
    --------------------------------------------------------------
    | Problem statement: Program to demonstrate linklist         |
    | Input:                                                     |
    | Output:                                                    |
    --------------------------------------------------------------
    '''
    print(main.__doc__)
    print('---------------------------')

    firstNode = LinkList()

    firstNode.head = Node(1)    
    secondNode = Node(2)
    thirdNode = Node(3)

    firstNode.head.next = secondNode
    secondNode.next = thirdNode
    thirdNode.next = None

    print(firstNode, secondNode, thirdNode)



if __name__ == '__main__':
    main()