class Solution(object):
    def subsets(self, nums):
        result = []
        temp = []

        def solve(index):
            result.append(temp[:])

            for i in range(index, len(nums)):
                temp.append(nums[i])

                solve(i + 1)

                temp.pop()

        solve(0)
        return result