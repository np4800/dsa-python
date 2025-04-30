# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        slow = head
        fast = head
        # Print initial values of slow and fast pointers
        print("Initial Slow Pointer Value:", slow.val)
        print("Initial Fast Pointer Value:", fast.val)
        print("--------------------")
        # Traverse the list with two pointers
        # Fast pointer moves two steps and slow pointer moves one step
        # This will ensure that when fast pointer reaches the end,
        # slow pointer will be at the middle of the list
        # If fast pointer is None or fast pointer's next is None,
        # it means we have reached the end of the list
        # and the slow pointer is at the middle
        # If the list has an even number of nodes, slow will point to the second middle node
        # If the list has an odd number of nodes, slow will point to the middle node
        # This is because when fast pointer reaches the end,
        # slow pointer will be at the middle node
        # Print the values of slow and fast pointers at each step
        # This will help in understanding how the pointers are moving
        # and how the middle node is being found
        # Print the values of slow and fast pointers at each step
        # This will help in understanding how the pointers are moving
        # and how the middle node is being found
        # Print the values of slow and fast pointers at each step
        # This will help in understanding how the pointers are moving
        # and how the middle node is being found
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print("Slow Pointer Value:", slow.val)
            print("Fast Pointer Value:", fast.val if fast else None)
            print("--------------------")
        # When fast pointer reaches the end, slow pointer will be at the middle
        return slow
# Example usage:
# Constructing a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

s = Solution()
print(s.middleNode(head))