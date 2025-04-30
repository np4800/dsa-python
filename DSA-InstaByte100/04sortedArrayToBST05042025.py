# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        # Base case: if the list is empty, return None
        if not nums:
            return None

        # Find the middle index of the list
        mid = len(nums) // 2

        # Create a new tree node with the middle element as the root
        root = TreeNode(nums[mid])

        # Recursively build the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        # Return the root of the constructed BST
        return root
# Example usage:
# Constructing a sorted array
nums = [-10, -3, 0, 5, 9]
# Creating an instance of the Solution class
solution = Solution()
# Calling the sortedArrayToBST method
root = solution.sortedArrayToBST(nums)
# Function to print the tree in pre-order traversal
def pre_order_traversal(node):
    if node:
        print(node.val, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
# Printing the constructed BST
print("Pre-order Traversal of the BST:")
pre_order_traversal(root)
# Output: Pre-order Traversal of the BST: 0 -10 -3 5 9
# The output will show the pre-order traversal of the constructed BST
# The expected output is the pre-order traversal of the BST     