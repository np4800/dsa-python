# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        print("Current node value:", root.val)
        left_depth = self.maxDepth(root.left)
        print("Left depth:", left_depth)
        right_depth = self.maxDepth(root.right)
        print("Right depth:", right_depth)
        print("---------------------------------")

        # The maximum depth of the tree is the maximum of the depths of the left and right subtrees plus one for the current node
        # This is a recursive function that traverses the tree and calculates the depth
        # The base case is when the node is None, in which case the depth is 0
        # The recursive case is when the node is not None, in which case the depth is 1 plus the maximum of the depths of the left and right subtrees
        # The function returns the maximum depth of the tree
        # The time complexity of this function is O(n), where n is the number of nodes in the tree
        # The space complexity of this function is O(h), where h is the height of the tree, due to the recursion stack
        # The function uses recursion to traverse the tree and calculate the maximum depth
        return max(left_depth, right_depth) + 1

# Test cases
s = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# Example 1
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2
# Input: root = [1,null,2]
# Output: 2
# Example 3
# Input: root = []
# Output: 0
# Example 4
# Input: root = [0]
# Output: 1
print(s.maxDepth(root)) # Output: 3
