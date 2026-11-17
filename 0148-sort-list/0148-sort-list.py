# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []
        temp = head
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        arr.sort()
        dummy = ListNode(0)
        current = dummy
        for i in range(len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return dummy.next
        