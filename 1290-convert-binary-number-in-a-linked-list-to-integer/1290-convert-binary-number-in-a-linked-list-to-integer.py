# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        count = 0
        temp = head

        while temp.next is not None:
            count += 1
            temp = temp.next
        print(count)

        sum1 = 0
        temp = head

        while temp is not None:
            sum1 += temp.val * (2 ** (count))
            temp = temp.next
            count -= 1

        return sum1