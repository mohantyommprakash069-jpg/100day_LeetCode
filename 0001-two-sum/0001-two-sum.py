class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            second = target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == second:
                    return i,j
                    
        