# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        # temp1 = headA
        # temp2 = headB

        # while temp1 != temp2:

        #     if temp1 is None:
        #         temp1 = headB
        #     else:
        #         temp1 = temp1.next

        #     if temp2 is None:
        #         temp2 = headA
        #     else:
        #         temp2 = temp2.next

        # return temp2
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


        
        dic1 = {}
        dic2 = {}

        temp1 = headA
        temp2 = headB

        while temp1 is not None:
            dic1[temp1] = True
            temp1 = temp1.next

        while temp2 is not None:
            if temp2 in dic1:
                return temp2
            temp2 = temp2.next

        return None