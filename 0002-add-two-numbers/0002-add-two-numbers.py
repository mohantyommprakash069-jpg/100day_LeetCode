# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            sum1 = 0

            if l1:
                sum1 += l1.val
                l1 = l1.next

            if l2:
                sum1 += l2.val
                l2 = l2.next

            sum1 += carry

            carry = sum1 // 10
            remain = sum1 % 10

            temp.next = ListNode(remain)
            temp = temp.next

        return dummy.next