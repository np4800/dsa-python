class TreeNode:
    def __init__(self,data) -> None:
        self.val = data
        self.left = None
        self.right = None

def buildBT(arrayBT):
    root = TreeNode(arrayBT[0])
    q = [root]
    i = 1

    while i < len(arrayBT):
        curr = q.pop(0)
        if i < len(arrayBT):
            curr.left = TreeNode(arrayBT[i])
            q.append(curr.left)
            i += 1
        if i < len(arrayBT):
            curr.right = TreeNode(arrayBT[i])
            q.append(curr.right)
            i += 1
    return root

def printBT(root):
    if root is None:
        return
    printBT(root.left)
    print(root.val,end=",")
    printBT(root.right)
## Driver Code
## Array
arrayBT=[1, 2, 3, 4, 5, 6, 6, 6, 6]
root = buildBT(arrayBT)
printBT(root)