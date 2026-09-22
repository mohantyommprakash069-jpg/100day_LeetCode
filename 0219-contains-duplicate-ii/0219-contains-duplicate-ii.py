class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        seen = {}

        for i in range(len(nums)):

            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True

            seen[nums[i]] = i

        return False
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             return True
        # return False
