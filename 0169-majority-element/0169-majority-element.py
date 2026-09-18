class Solution(object):
    def majorityElement(self, nums):
        # candidate = 0
        # count = 0

        # for num in nums:
        #     if count == 0:
        #         candidate = num

        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1

        # return candidate

        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

            if count[i] > len(nums) // 2:
                return i
