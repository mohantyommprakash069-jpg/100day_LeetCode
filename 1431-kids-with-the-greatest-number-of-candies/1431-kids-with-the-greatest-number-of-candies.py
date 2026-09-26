class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = len(candies)
        result = [False] * n

        for i in range(len(candies)):
            max1 = candies[i] + extraCandies
            result[i] = True

            for j in range(len(candies)):
                if max1 < candies[j]:
                    result[i] = False
                    break

        return result