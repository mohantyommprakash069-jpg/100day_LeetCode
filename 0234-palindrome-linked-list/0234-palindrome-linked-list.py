# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        temp = head
        result = []
        while temp is not None:
            result.append(temp.val)
            temp = temp.next

        i = 0
        j = len(result)-1
        
        while i<j:
            if result[i] != result[j]:
                return False
            
            i+=1
            j-=1
        return True
