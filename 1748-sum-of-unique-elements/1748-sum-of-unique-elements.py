class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]] = 1
        for key in d:
            if d[key] ==1:
                sum1+=key
           
        return sum1
            
        