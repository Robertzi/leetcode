class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right
searchTreeList = [2,None,3,None,None]
leftSon = True
def nodeFirstCreatTree(nodelist):
    global leftSon
    if nodelist == []:
        leftSon = True
        return None
    val = nodelist.pop(0)
    if val == None:
        leftSon = False
        return None
    if leftSon == True :
        left = nodeFirstCreatTree(nodelist)
    if len(nodelist) > 0:
        right = nodeFirstCreatTree(nodelist)
    else:
        right = None
    return TreeNode(val, left, right)

def printTree(root):
    root.left and printTree(root.left)
    root.right and printTree(root.right)
    print(root.val, ',')
tree = nodeFirstCreatTree(searchTreeList)
printTree(tree)
pass