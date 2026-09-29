# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dummyA = ListNode(0)
        dummyB = ListNode(0)

        dummyA.next = headA
        dummyB.next = headB

        temp1 = dummyA
        temp2 = dummyB

        while temp1 != temp2:
            if temp1 is None:
                temp1 = dummyB.next
            else:
                temp1 = temp1.next

            if temp2 is None:
                temp2 = dummyA.next
            else:
                temp2 = temp2.next

        return temp1
     
