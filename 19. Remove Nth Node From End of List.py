# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        top = ListNode(0)
        top.next = head
        q = p = top
        for i in range(n+1):
            p = p.next
        while p:
            p = p.next
            q = q.next
        q.next = q.next.next
        return top.next