# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(val = None)
        current = head
        p = list1
        q = list2

        while p and q:
            if p.val <= q.val:
                current.next = p
                p = p.next
            else:
                current.next = q
                q = q.next
            current = current.next 
        current.next = p if p else q 
        return head.next
