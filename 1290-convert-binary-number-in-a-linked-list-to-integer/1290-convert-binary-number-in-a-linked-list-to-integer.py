# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def getDecimalValue(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: int
#         """

#         count = 1
#         temp = head

#         while temp.next is not None:
#             count += 1
#             temp = temp.next
#         print(count)

#         sum1 = 0
#         temp = head

#         while temp is not None:
#             sum1 += temp.val * (2 ** (count-1))
#             temp = temp.next
#             count -= 1

#         return sum1 
class Solution(object):
    def getDecimalValue(self, head):
        ans = 0
        temp = head
        while temp is not None:
            ans = ans*2+temp.val
            temp = temp.next
        return ans