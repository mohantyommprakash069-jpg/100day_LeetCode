class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        n = len(intervals)

        arr = []

        for i in range(n):
            l, r, w = intervals[i]
            arr.append((l, r, w, i))

        arr.sort()

        starts = [x[0] for x in arr]

        next_idx = [0] * n

        for i in range(n):
            left = i + 1
            right = n

            while left < right:
                mid = (left + right) // 2

                if starts[mid] > arr[i][1]:
                    right = mid
                else:
                    left = mid + 1

            next_idx[i] = left

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):

            for k in range(1, 5):

                # Don't choose current interval
                skip = dp[i + 1][k]

                # Choose current interval
                score, indices = dp[next_idx[i]][k - 1]

                take = (
                    score + arr[i][2],
                    tuple(sorted(indices + (arr[i][3],)))
                )

                if take[0] > skip[0]:
                    dp[i][k] = take

                elif take[0] < skip[0]:
                    dp[i][k] = skip

                else:
                    dp[i][k] = min(take, skip)

        return list(dp[0][4][1])