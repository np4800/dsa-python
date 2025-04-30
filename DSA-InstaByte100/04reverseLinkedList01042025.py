# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr = head
        prev = None
        #                             
        # <-- 1 <-- 2 <-- 3 <-- 4 <-- 5
        #                             p     
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
# Time Complexity: O(n)
# Space Complexity: O(1)
print("Reverse Linked List")
print(Solution().reverseList([1,2,3,4,5])) # [5,4,3,2,1]
print(Solution().reverseList([])) # []