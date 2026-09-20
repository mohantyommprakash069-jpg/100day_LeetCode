class Solution(object):
    def missingNumber(self, nums):
        # ans=len(nums)
        # for i in range(len(nums)):
        #     ans^=i
        #     ans^=nums[i]
        # return ans
        n = len(nums)
        sum1 = n*(n+1)/2
        sum2=0
        for i in range(n):
            sum2+=nums[i]
        return sum1-sum2