class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None


def lowestCommonAncestor(root, p, q):
    if root is None:
        return None
    
    if root.val == p or root.val == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    if left is None:
        return right
    return left



root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)



ans = lowestCommonAncestor(root, 5, 1)
print("LCA is ",ans.val)  
ans = lowestCommonAncestor(root, 6, 4)
print("LCA is ",ans.val)   
ans = lowestCommonAncestor(root, 7, 4)
print("LCA is ",ans.val)
 