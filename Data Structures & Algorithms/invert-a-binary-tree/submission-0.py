# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.left == None and root.right == None :
            return TreeNode(root.val)

        if root.left != None and root.right != None :
            return TreeNode(root.val,self.invertTree(root.right),self.invertTree(root.left)) 

        inverted_tree = TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))

        return inverted_tree
        