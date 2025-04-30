# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        
        print(root.val)
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def printTree(self, root):
        # print("Printing Tree")
        if root is None:
            return
        print(root.val, end = " ")
        self.printTree(root.left)
        self.printTree(root.right)
    
# Time Complexity: O(n)
# Space Complexity: O(n)
print("Invert Binary Tree")
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)

Solution().printTree(root)
Solution().invertTree(root)
print()
Solution().printTree(root)
