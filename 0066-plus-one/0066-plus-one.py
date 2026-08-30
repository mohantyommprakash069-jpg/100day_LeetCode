class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(len(digits)):
            num=num*10+digits[i]
        num=num+1
        l1=list(map(int,str(num)))
        return l1