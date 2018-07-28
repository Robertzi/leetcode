# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nextone):
        self.val = x
        if(nextone):
            self.next = nextone
        else:
            self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        L = []
        p = head
        switch = 1
        while p:
            L.append(p)
            p = p.next
        l = 1
        r = len(L)-1
        p = head
        while l <= r:
            if switch < 0:
                p.next = L[l]
                l +=1
            else:
                p.next = L[r]
                r -=1
            p = p.next
            switch *=-1
        if(hasattr(p,'next')):
            p.next = None
x = Solution()
l5 = ListNode(5 ,None)
l4 = ListNode(4 ,l5)
l3 = ListNode(3 ,l4)
l2 = ListNode(2 ,l3)
l1 = ListNode(1 ,l2)
x.reorderList(l1)
node = l1
while node:
    print(node.val)
    node = node.next
        