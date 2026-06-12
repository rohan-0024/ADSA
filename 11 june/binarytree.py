# traversal using binary trees
from collections import deque

inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    mid = inorder.index(root_val)
    root.left = buildTree(preorder[1 : 1 + mid], inorder[:mid])
    root.right = buildTree(preorder[1 + mid:], inorder[mid + 1 :])
    
    return root

def traversalBFS(root):
    if root is None:
        return []
    
    queue = deque()
    queue.append(root)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        
    return result

root1 = buildTree(preorder, inorder)
print(traversalBFS(root1))


    
    
    
    