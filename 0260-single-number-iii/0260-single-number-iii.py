class Solution(object):
    def singleNumber(self, nums):
        # ans = 0

        # for i in nums:
        #     ans ^= i

        # diff = ans & -ans

        # a = 0
        # b = 0

        # for i in nums:
        #     if i & diff:
        #         a ^= i
        #     else:
        #         b ^= i

        # return a, b
        dic = {}
        for i in range(len(nums)):
            if nums[i]  in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]] = 1
        ans = []
        for i in dic:
            if dic[i] == 1:
                ans.append(i)
        return ans