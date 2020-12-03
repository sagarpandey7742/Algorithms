# Morris inorder traversal is a very space efficient algorithm used to traverse the tree in inorder in O(1) space
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def morrisInorderTraversal(root):
    current=root
    while current:
        if not current.left:
            print(current.val,end=" ")
            current=current.right
        else:
            predecessor=current.left            # Finding the current's inorder predecessor
            while predecessor.right and predecessor.right!=current:
                predecessor=predecessor.right

            if not predecessor.right:           # Making a link from predecessor->current
                predecessor.right=current
                current=current.left
            else:                               # Restoring the tree be removing predecessor->current link
                predecessor.right=None
                print(current.val,end=" ")
                current=current.right

root=TreeNode(13,None,None)
root.left=TreeNode(8,None,None)
root.right=TreeNode(18,None,None)
r=root
root=root.left
root.left=TreeNode(6,None,None)
root.right=TreeNode(11,None,None)
root=r.right
root.left=TreeNode(14,None,None)
root.right=TreeNode(20,None,None)
root=r
morrisInorderTraversal(root)

