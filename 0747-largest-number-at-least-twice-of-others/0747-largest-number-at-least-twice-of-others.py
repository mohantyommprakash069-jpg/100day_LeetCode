class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = float('-inf')
        max2 = float('-inf')
        index = -1
        for i in range(len(nums)):
            if nums[i]>max1:
                max2 = max1
                max1 = nums[i]
                index = i
            elif nums[i]>max2:
                max2 = nums[i]

        if max1 >= 2*max2:
            return index
        else  :
            return -1