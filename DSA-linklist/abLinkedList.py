import math
llstr = ''
MAX_ELE = -10000
flag = 0
class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data,self.head)
        self.head = new_node
        # print(dir(new_node))

    def insert_at_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node


    def print_ll(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + '-->'
            print(itr)
            itr = itr.next
        print(f"Print Linked List: {llist}")
    

    def print_rec(self,node):
        global llstr
        if node is not None:
            self.print_rec(node.next)
            llstr += str(node.data) + '-->'
        # print(llstr)
    
    def print_count(self,node):
        count = 0
        if(node is None):
            return 0
        else:
            while node is not None:
                count += 1
                node = node.next
        return count

    def print_count_recursion(self,node):
        if node is None:
            return 0
        return self.print_count_recursion(node.next)+1

    def sum_of_nodes_by_recursion(self,node):
        if node is None:
            return 0
        return self.sum_of_nodes_by_recursion(node.next)+node.data
    
    def sum_of_nodes(self,node):
        sum = 0
        if node is None:
            return sum
        while node is not None:
            sum = sum + node.data
            node = node.next
        return sum

    def print_max_element(self,node):
        max = -100
        if node is None:
            return max
        while node is not None:
            if node.data > max:
                max = node.data
            node = node.next
        return max
    
    def print_max_by_recursion(self,node):
        global MAX_ELE
        if node is None:
            return MAX_ELE
        else:
            if node.data > MAX_ELE:
                MAX_ELE = node.data
            self.print_max_by_recursion(node.next)
        return MAX_ELE

    def search_by_loop(self,node, key):
        while node is not None:
            if key == node.data:
                return key
            node = node.next
        return None

    def search_by_recursion(self,node,key):
        if node is None:
            return None
        if key == node.data:
            return key
        return self.search_by_recursion(node.next,key)
    
    def improve_search(self,node,key):
        tail_ptr = None
        if node is None:
            return None
        while node is not None:
            if key == node.data:
                tail_ptr.next = node.next
                node.next = self.head
                self.head = node
                return
             
            tail_ptr = node
            node = node.next
            # print(f"Q:{tail_ptr.data}-->{tail_ptr.next} 
            # P:{node.data}-->{node.next}")
            # print(f"Q-->{tail_ptr.data}")

    def insert_element(self,pos,node):
        current = self.head
        if pos == 0:
            node.next = self.head
            self.head = node
        if pos > 0:
            for i in range(pos-1):
                current = current.next
            node.next = current.next
            current.next = node
    
    def insert_in_sorted_ll(self,node,first):
        tail = None
        current = first

        if first is None:
            first = node
        else:
            while (current is not None and current.data < node.data):
                tail = current
                current = current.next
            if (current == first ):
                node.next = first
                first = node
            else:
                node.next = tail.next
                tail.next = node    

    def delete_node(self,pos):
        if pos == 1:
            deleted_node = self.head.data
            self.head = self.head.next
            return
        tail = None
        current = self.head
        deleted_node = None

        for i in range(pos-1):
            print(i )
            tail = current
            current = current.next

        if current:
            tail.next = current.next
            deleted_node = current.data
            print(f"Node Deleted: {deleted_node}")
        return
    
    def is_sorted(self):
        current = self.head
        max = -32456

        while current is not None:
            if current.data > max:
                max = current.data
                current = current.next
            else:
                return False
        return True
        # 5-->6-->9-->8-->8-->8 
    def remove_duplicates(self):
        p = self.head
        q = self.head.next

        while q is not None:
            if q.data != p.data:
                p=q
                q = q.next
            else:
                p.next = q.next
                q = p.next


    def reverse_ll(self):
        aux=[]
        current = self.head

        while current is not None:
            aux.append(current.data)
            current = current.next
    
        index = len(aux)-1
        
        current = self.head
        while current is not None:
            current.data = aux[index]
            current = current.next
            index -= 1

    def reverse_ll_ptr(self):
        '''
        Utilises the 3 pointer method p q r
        '''
        p = self.head
        q = None
        r = None
        while p is not None:
            r = q
            q = p
            p = p.next
            q.next = r
        self.head = q

    def reverse_ll_recur(self, q, p):
        if p is not None:
            self.reverse_ll_recur(p,p.next)
            p.next = q
        else:
            # print('else -->')
            self.head = q

    def merge_ll(self,first,sec):
        third = None
        last = None
        llstr = ""
        if(first.data<sec.data):
            third = first
            last = first
            first = first.next
            last.next = None
        else:
            third = sec
            last = sec
            sec = sec.next
            last.next = None
        
        while (sec is not None and first is not None):
            if(first.data<sec.data):
                last.next = first
                last = first
                first = first.next
                last.next = None
            else:
                last.next = sec
                last = sec
                sec = sec.next
                last.next = None

        if(sec is not None):
            last.next = sec
        
        if(first is not None):
            last.next = first
        
        while(third is not None):
            llstr += str(third.data) + '-->'
            third = third.next
        print(f"Merged Linked List: {llstr}")
    
    def length_of_ll(self):
        len = 0
        current = self.head
        while current:
            len += 1
            current = current.next
        return len
       
    def return_middle_element(self):
        no_of_elements = self.length_of_ll()
        middle_index = no_of_elements//2
        current = self.head
        for i in range(middle_index-1): ## There is a catch over here loop starts from 0 therefore, you have minus one from end of the loop to stay on the index that you want.
            # print(i)
            current = current.next
        return current.data

    def return_middle_ele(self):
        p=q=self.head
        while (q):
            q = q.next
            if(q):
                q=q.next
            if (q):
                p=p.next
        return p.data

    def return_middle_elem_by_stack(self):
        stack=[]
        current = self.head
        while current:
            stack.append(current)
            current = current.next
        for i in range(len(stack)//2):
            stack.pop()
        
        return stack[len(stack)-1].data

#----------------------------------------------------------------------------------------------------------------------------
class CircularLinkedList():
    flag = 0
    def __init__(self) -> None:
        self.start = None

    def add_node(self,data):
        new_node = Node(data)
        if not self.start:
            self.start = new_node
            new_node.next = self.start
        else:
            temp = self.start
            while (temp.next != self.start):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.start
    
    def show_circular_ll(self):
        temp = self.start
        while True:
            print(temp.data, end="-->")
            temp = temp.next
            if temp == self.start:
                print("...")
                break
    
    def show_circular_by_recursion(self,p):
        global flag
        if (flag == 0 or p != self.start):
            flag = 1
            print(p.data,end="-->")
            self.show_circular_by_recursion(p.next)
        flag = 0


    def insert_element(self,pos,data):
        e1 = Node(data)
        p = self.start

        if pos == 0:
            e1.next = self.start
            while (p.next != self.start):
                p = p.next
            p.next = e1
            self.start = e1
        else:
            for i in range(0,pos-1):
                p = p.next
            
            e1.next = p.next
            p.next = e1


    def delete_element_cl(self,pos):
        # Delete from postion: 1
        p = self.start
        if (pos == 1):
            while (p.next != self.start):
                p = p.next
            x = self.start.data
            if (p == self.start):
                self.start = None
            else:
                p.next = self.start.next
                self.start = None
                self.start = p.next
            return x
        else: # Delete from postiion: n
            for i in range(pos-2):
                p = p.next
            q = p.next
            x = q.next.data
            p.next = q.next
            q = None
            return x


class Dnode:
    def __init__(self,data) -> None:
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinked:
    def __init__(self) -> None:
        self.first = None
    
    def create(self,data):
        new_node = Dnode(data)
        if self.first is None:
            self.first = new_node
            return
        current = self.first
        print(current.next)
        while current.next:
            # print(current.prev,current.data,current.next)
            current = current.next
        current.next = new_node
        new_node.prev = current

    def print_dll(self):
        dlstr = ""
        current = self.first
        while current is not None:
            dlstr += str(current.data)+"<==>"
            current = current.next
        print(dlstr)

    def insert_in_dll(self,data,pos):
        new_node = Dnode(data)
        current = self.first
        if pos == 0:
            new_node.next = current
            current.prev = new_node
            self.first = new_node
        else:
            if pos < self.length_of_dll():
                for i in range(pos-1):
                    current = current.next
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                new_node.prev = current
            else:
                for i in range(pos-1):
                    current = current.next
                new_node.prev = current
                current.next = new_node

    def length_of_dll(self):
        len = 0
        current = self.first
        while current:
            len += 1
            current = current.next
        return len

    def delete_node_dl(self,pos):
        p = self.first
        if pos > self.length_of_dll() or pos < 1:
            return f"Available Element in Doubly Linked list: {self.length_of_dll()} and you sent {pos}"
        if pos == 1:
            self.first = self.first.next
            x = p.data
            if (self.first):
                self.first.prev = None
        else:
            for i in range(pos-1):
                p = p.next
            p.prev.next = p.next
            if (p.next):
                p.next.prev = p.prev
            x = p.data
        return x
        
    def reverse_dl(self):
        p = self.first
        while (p):
            temp = p.next
            if (p.next is None):
                # print(p.data)
                self.first = p
            p.next = p.prev
            p.prev = temp
            p=p.prev
        print(self.first.data)


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.start = None
    
    def add_node(self,data):
        new_node = Dnode(data)

        if not self.start:
            self.start = new_node
            new_node.next = self.start
            return
        current = self.start
        while (current.next != self.start):
            current = current.next
        current.next = new_node
        new_node.prev = current
        new_node.next = self.start
        self.start.prev = new_node
    
    def show_circular_doubly_ll(self):
        current = self.start
        dcll = ""
        while True:
            dcll += str(current.data) + "<==>"
            # print(current.prev,current.data,current.next)
            current = current.next
            if current == self.start:
                break
        print(dcll)

    def length(self):
        len=0
        current = self.start
        while True:
            len += 1
            current = current.next
            if current == self.start:
                break
        return len

    def insert_element(self,data,pos):
        new_node = Dnode(data)
        current = self.start
        # if pos=1
        if (pos == 0):
            # print(new_node.prev,new_node.data,new_node.next)
            # print(self.start.prev,self.start.data,self.start.next)
            new_node.next = self.start
            new_node.prev = self.start.prev
            self.start.prev.next = new_node
            self.start.prev = new_node
            new_node = self.start

        elif (pos > 1 and pos < self.length()):
            for i in range(pos-1):
                current = current.next
            new_node.prev = current         ## Tackling Out Going Pointer from new-node
            new_node.next = current.next    ## Tackling Out Going Pointer from new-node
            current.next.prev = new_node    ## Tackling In Coming Pointer to new-node
            current.next = new_node         ## Tackling In Coming Pointer to new-node

    def delete_element(self,pos):
        current = self.start
        if (pos < 1):
            print(f"No position number: {pos}")
            return
        for i in range(pos-1):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        current.next = None
        current.prev = None


        # if pos > 0 and pos < length of Circular Linked List





            


# Main Driver Code

### First Linked List: Instance of Class Linked List
ll1 = LinkedList()
ll1.insert_at_beginning("A")
ll1.insert_at_beginning("B")
ll1.insert_at_beginning("C")
print('Insert at beginning ll1:')
ll1.print_ll()

### Second Linked List: Instance of Class Linked List
ll2 = LinkedList()
ll2.insert_at_last(5)
ll2.insert_at_last(10)
ll2.insert_at_last(20)
ll2.insert_at_last(40)
ll2.insert_at_last(60)

print(f"ll2 is sorted: {ll2.is_sorted()}")
print('ll2 Insert at last:')
ll2.print_ll()
first = ll2.head
ll2.print_rec(first)
print(llstr) ## This will print the linklist that got executed from recursion function that is called just above.

print(f"ll2: Count No. of Nodes in LinkedList: {ll2.print_count(first)}")
print(f"ll2: Count No. of Nodes in LinkedList by Recursion: {ll2.print_count_recursion(first)}")

print(f"ll2: Sum of Nodes: {ll2.sum_of_nodes(first)}")
print(f"ll2: Sum of Nodes By Recursion: {ll2.sum_of_nodes_by_recursion(first)}")
float('-inf')

print(f"ll2: Using Loop, Maximum Element in LL: {ll2.print_max_element(first)}")
print(f"ll2: Using Recursion, Maximum Elemetn in LL: {ll2.print_max_by_recursion(first)}")

print('** Elements in Linked List can be searched by Linear Search. You cannot search by Binary Search! **')

print(f"ll2: Using Loop, Search an Element: {ll2.search_by_loop(first,40)}")
print(f"ll2: Using Recursion, Search an Element: {ll2.search_by_recursion(first,99)}")

# Insert an element in the sorted array
ll2.print_ll() ## Before insert
e2 = Node(90)
ll2.insert_in_sorted_ll(e2,first)
ll2.print_ll() ## After insert

# Searching an element in the linked list
ll2.improve_search(first,40)
ll2.print_ll()

# Insert element in the given position
e1 = Node(50)
ll2.insert_element(3,e1)
ll2.print_ll()

# Delete the node
ll2.delete_node(1)
ll2.print_ll()

# Check if linked list is sorted or not
print(f"ll2: is sorted: {ll2.is_sorted()}")

# Reverse a link list: Method-3
print("ll2: Reverse a Linked list by recursion")
ll2.print_ll()
ll2.reverse_ll_recur(None,first)
ll2.print_ll()

# Reverse a link list: Method-1
print("ll2: Reverse a Linked list by reversing the links of the nodes")
ll2.print_ll()
ll2.reverse_ll_ptr()
ll2.print_ll()

# Reverse a link list: Method-2
print("ll2: Reverse a Linked list by swapping the data of the nodes")
ll2.print_ll()
ll2.reverse_ll()
ll2.print_ll()

### Third Linked List: Instance of Class Linked List
ll3 = LinkedList()
ll3.insert_at_last(5)
ll3.insert_at_last(6)
ll3.insert_at_last(8)
ll3.insert_at_last(8)
ll3.insert_at_last(8)
ll3.insert_at_last(7)

# Remove duiplicate elements from linked list
print(f"ll3: Remove duplicates")
ll3.print_ll()
ll3.remove_duplicates()
ll3.print_ll()


# Merge two sorted Linked List
f_list = LinkedList()
s_list = LinkedList()
t_list = LinkedList()

f_list.insert_at_last(3)
f_list.insert_at_last(4)
f_list.insert_at_last(8)
f_list.insert_at_last(9)
f_list.insert_at_last(12)
s_list.insert_at_last(1)
s_list.insert_at_last(5)
s_list.insert_at_last(10)
s_list.insert_at_last(15)
s_list.insert_at_last(20)

print("Before Merge: Linked List")
f_list.print_ll()
s_list.print_ll()

f_ll = f_list.head
s_ll = s_list.head

t_list.merge_ll(f_ll,s_ll)

## How to check if the LL is linear or looped
# TODO:

## Create and display Circular Linked List
print("Creating Circular Linked List ...")
cl = CircularLinkedList()
cl.add_node("Nikhil")
cl.add_node("Sneha")
cl.add_node("Shamaila")
cl.add_node("Ankita")

cl.show_circular_ll()
head = cl.start
cl.show_circular_by_recursion(head)

## Insert an element in the circular linked list: pos=0, pos=n
print("\nInsert Element in Ciructular linkedlist at given position")
cl.insert_element(2,"Shreyashi")
cl.insert_element(0,"Suman")
cl.show_circular_ll()

## Delete and element in the circular link list: pos=1, pos=n
print("\nDelete Element in Ciructular linkedlist at given position")
cl.show_circular_ll()
cl.delete_element_cl(pos=1)
cl.delete_element_cl(pos=3)
cl.show_circular_ll()

## Doubly Linked List
print("\nDoubly Linked List ------->")
dl = DoublyLinked()
dl.create("A")
dl.create("B")
dl.create("C")
dl.create("D")
dl.print_dll()

## Insert in Doubly Linked List
print("\nInsert into Doubly Linked List")
dl.insert_in_dll("A1",0)
dl.insert_in_dll("B1",3)
dl.insert_in_dll("D1",6)
dl.print_dll()
print(f"Lenght of Doubly Linked List: {dl.length_of_dll()}")

## Delete an element in Doubly Linked List
print("\nDelete an element in Doubly Linked List")
dl.print_dll()
result = dl.delete_node_dl(pos=0)
print(result)
dl.print_dll()

## Reverse the Doubly Linked List
print("\nReverse the element in the Doubly Linked List")
dl.print_dll()
dl.reverse_dl()
dl.print_dll()

## Circular Doubly Linked List
print("\nCreate Circular Doubly Linked List")
dcll = CircularDoublyLinkedList()
dcll.add_node("Np")
dcll.add_node("St")
dcll.add_node("Sa")
dcll.add_node("As")
dcll.show_circular_doubly_ll()
print("Insert an element at given position >  0: ", end=" ")
dcll.insert_element("Ss",3)
dcll.insert_element("Ak",4)
dcll.show_circular_doubly_ll()
print("Insert an element at given position =  0: ", end=" ")
dcll.insert_element("Sg",0)
dcll.show_circular_doubly_ll()
print("Delete an element at given position != 0: ", end=" ")
dcll.delete_element(3)
dcll.show_circular_doubly_ll()
print(f"Length Of Circular Doubly Linked List: {dcll.length()}")

## Problem Statement: Finding Middle Element of Linked List
ll2.print_ll()
print(f"Length of Linked List: {ll2.length_of_ll()}")
print(f"Middle Element in Linked List using Length and Scan Method: {ll2.return_middle_element()}")
print(f"Middle Element in Linked List using TWO POINTER Method    : {ll2.return_middle_ele()}")
print(f"Middle Element in Linked List using Stack Method          : {ll2.return_middle_elem_by_stack()}")


## Intersectio of Two Linked List

ll2 = LinkedList()
ll2.insert_at_last(5)
ll2.insert_at_last(10)
ll2.insert_at_last(20)
ll2.insert_at_last(40)
ll2.insert_at_last(60)

ll4 = LinkedList()
ll4.insert_at_last(80)
ll4.insert_at_last(90)
ll4.insert_at_last(20)
ll4.insert_at_last(40)
ll4.insert_at_last(60)