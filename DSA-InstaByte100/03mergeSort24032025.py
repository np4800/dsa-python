# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        ans = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                ans.append(list1[i])
                i += 1
            elif list1[i] > list2[j]:
                ans.append(list2[j])
                j += 1
            elif list1[i] == list2[j]:
                ans.append(list1[i])
                ans.append(list2[j])
                i += 1
                j += 1
        ans.extend(list1[i:])
        ans.extend(list2[j:])
        return ans
    
# Time Complexity: O(n)
# Space Complexity: O(n)  
print("Merge Two Sorted Lists") 
print(Solution().mergeTwoLists([1,2,4], [1,3,4])) # [1,1,2,3,4,4]
print(Solution().mergeTwoLists([], [])) # []
print(Solution().mergeTwoLists([], [0])) # [0]
print(Solution().mergeTwoLists([1,2,3,4], [5,6,7,8])) # [1,2,3,4,5,6,7,8]
print(Solution().mergeTwoLists([1,2,3,4], [1,2,3,4])) # [1,1,2,2,3,3,4,4]
print(Solution().mergeTwoLists([1,2,3,4], [5,6,7,8,9])) # [1,2,3,4,5,6,7,8,9]
print(Solution().mergeTwoLists([1,2,3,4,5], [1,2,3,4])) # [1,1,2,2,3,3,4,4,5]
print(Solution().mergeTwoLists([1,2,3,4,5], [6,7,8,9])) # [1,2,3,4,5,6,7,8,9]
print(Solution().mergeTwoLists([1,2,3,4], [5,6,7,8,9,10])) # [1,2,3,4,5,6,7,8,9,10]
print(Solution().mergeTwoLists([1,2,3,4,5,6], [1,2,3,4])) # [1,1,2,2,3,3,4,4,5,6]
print(Solution().mergeTwoLists([1,2,3,4,5], [6,7,8,9,10])) # [1,2,3,4,5,6,7,8,9,10]
print(Solution().mergeTwoLists([1,2,3,4,5,6], [7,8,9,10])) # [1,2,3,4,5,6,7,8,9,10]
print(Solution().mergeTwoLists([1,2,3,4], [5,6,7,8,9,10,11])) # [1,2,3,4,5,6,7,8,9,10,11]
print(Solution().mergeTwoLists([1,2,3,4,5,6,7], [1,2,3,4])) # [1,1,2,2,3,3,4,4,5,6,7]
print(Solution().mergeTwoLists([1,2,3,4,5], [6,7,8,9,10,11])) # [1,2,3,4,5,6,7,8,9,10,11]
