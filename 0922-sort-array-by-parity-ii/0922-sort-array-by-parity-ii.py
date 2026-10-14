
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = 0
        odd = 1

        while even < len(nums) and odd < len(nums):
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 != 0:
                odd += 2
            else:
                temp = nums[even]
                nums[even] = nums[odd]
                nums[odd] = temp
                even += 2
                odd += 2

        return nums
