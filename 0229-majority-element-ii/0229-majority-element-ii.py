class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]] = 1
        result = []
        for key,value in dict1.items():
            if value > len(nums)//3:
                result.append(key)
        return result
