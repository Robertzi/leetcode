# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.list = []
        self.prev = None
        self.times = []
        if root != None:
            self.node(root)
            if self.times[0] < self.times[-1]:
                self.list = self.list[-1:]
            elif self.times[0] > self.times[-1]:
                self.list.pop()
        return self.list

    def node(self, node):
        if node.left != None:
            self.node(node.left)
        if node.val != None:
            if(self.list != []):
                if self.list[-1] == node.val:
                    self.times[-1] += 1
                else:
                    if self.times[0] < self.times[-1]:
                        self.list = self.list[-1:]
                        self.times = self.times[-1:]
                    elif self.times[0] > self.times[-1]:
                        self.list.pop()
                        self.times.pop()
                    self.list.append(node.val)
                    self.times.append(1)
            else:
                self.times.append(1)
                self.list.append(node.val)
        if node.right != None:
            self.node(node.right)