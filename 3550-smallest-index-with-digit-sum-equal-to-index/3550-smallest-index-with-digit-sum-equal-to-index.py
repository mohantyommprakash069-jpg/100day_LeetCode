class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            temp = nums[i]
            sum1 = 0
            while temp>0:
                remainder = temp%10
                sum1 += remainder
                temp = temp//10
            if i == sum1:
                return i
        return -1