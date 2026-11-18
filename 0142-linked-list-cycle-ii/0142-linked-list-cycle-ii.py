# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        pos = 0
        temp = head
        dic1 = {}

        while temp is not None:
            if temp in dic1:
                return temp

            dic1[temp] = pos
            pos += 1
            temp = temp.next

        return None