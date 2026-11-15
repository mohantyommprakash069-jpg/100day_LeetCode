class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count = 0
        sum1 = 0
        d = {0:1}
        for i in range(len(nums)):
            sum1+=nums[i]
            if sum1 - goal in d:
                count+=d[sum1-goal]

            if sum1 in d:
                d[sum1]+=1
            else:
                d[sum1] = 1
        return count

        