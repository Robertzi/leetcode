# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        