class Solution(object):
    def countElements(self, nums):
        count = 0

        minimum = min(nums)
        maximum = max(nums)

        for i in range(len(nums)):
            if nums[i] > minimum and nums[i] < maximum:
                count += 1

        return count