# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Base case: if the tree is empty, return 0
        if root is None:
            return 0
        
        # Helper function to calculate the height of the tree
        def height(node):
            if node is None:
                return 0
            
            print("Node Value:", node.val)
            print("--------------------")
            print("Pre-Order ----> Node Value:", node.val, "Left Child:", node.left, "Right Child:", node.right)
            # Recursively calculate the height of left and right subtrees
            left_height = height(node.left)
            print("In-Order >>> Node Value:", node.val, "Left Height:", left_height)
            right_height = height(node.right)
            
            print("Post-Order ---> Node Value:", node.val, "Left Height:", left_height, "Right Height:", right_height)
            # Update the diameter
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node
            return max(left_height, right_height) + 1
        

        # Initialize diameter as a class variable
        self.diameter = 0
        # Start the height calculation from the root
        height(root)
        # Return the diameter of the tree
        return self.diameter
# Example usage:
# Constructing a binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
# Creating an instance of the Solution class
solution = Solution()
# Calling the diameterOfBinaryTree method
diameter = solution.diameterOfBinaryTree(root)
# Printing the result
print("Diameter of the binary tree:", diameter)  # Output: 3
# The diameter of the tree is the longest path between any two nodes in the tree.
# In this case, the longest path is from node 4 to node 5, passing through nodes 2 and 1.

            