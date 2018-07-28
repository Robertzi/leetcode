# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None) :
            return True
        return self.checkTree(root.left, float('-inf'), root.val) and self.checkTree(root.right, root.val, float('inf'))
    def checkTree(self, node, min, max):
        """
        :type node: TreeNode
        """
        if(node == None): 
            return True
        elif node.val>min and node.val<max:
            return self.checkTree(node.left, min, node.val) and self.checkTree(node.right, node.val, max)
        else :
            return False








n6 = TreeNode()
n5 = TreeNode()
n4 = TreeNode()
n3 = TreeNode()
n2 = TreeNode()
n1 = TreeNode()
