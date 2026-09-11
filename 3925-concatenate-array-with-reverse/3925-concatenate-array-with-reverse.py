class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list1=[]
        for i in range(len(nums)):
            list1.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            list1.append(nums[i])
        return list1
        