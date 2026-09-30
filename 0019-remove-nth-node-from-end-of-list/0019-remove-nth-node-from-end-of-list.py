# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        count = 1
        temp = head

        while temp.next is not None:
            temp = temp.next
            count += 1

        pos = count - n
        print(count)
        print(pos)
        
        if pos == 0:
            return head.next

        temp = head

        for i in range(1, pos):
            temp = temp.next

        temp.next = temp.next.next

        return head