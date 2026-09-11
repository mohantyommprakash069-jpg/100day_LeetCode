class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        min_capacity = float('inf')
        answer = -1

        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                if capacity[i] < min_capacity:
                    min_capacity = capacity[i]
                    answer = i

        return answer
