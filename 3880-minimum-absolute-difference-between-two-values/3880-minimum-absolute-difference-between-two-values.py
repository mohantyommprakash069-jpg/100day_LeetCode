class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_abs=float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len (nums)):
                if (nums[i] == 1 and nums[j] == 2) or (nums[i] == 2 and nums[j] == 1):
                    min_abs = min(min_abs, j - i)
                    

        if min_abs != float('inf'):
            return min_abs
        else:
            return -1
    
        