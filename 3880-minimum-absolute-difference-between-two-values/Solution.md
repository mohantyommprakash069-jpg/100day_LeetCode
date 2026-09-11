# Minimum Absolute difference between two values

# Intuition

We need to find the **minimum distance between any `1` and `2`** in the array.

I check every pair of elements. If one element is `1` and the other is `2`, I calculate their distance using:

`j - i`

Then I keep the smallest distance found.

If there is no pair containing `1` and `2`, I return `-1`.

# Approach

1. Set `min_abs` to infinity.
2. Use two loops to check every possible pair `(i, j)`.
3. Check whether the pair contains `1` and `2`.
4. If it does, calculate `j - i`.
5. Update `min_abs` with the smaller distance.
6. If `min_abs` was never changed, return `-1`.

# Complexity

* Time complexity: **O(n²)**

  We use two nested loops to check all possible pairs.

* Space complexity: **O(1)**

  We only use a few variables and don't create any extra data structure.

# Code

```python
class Solution(object):

    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min_abs = float('inf')

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if (nums[i] == 1 and nums[j] == 2) or \
                   (nums[i] == 2 and nums[j] == 1):

                    min_abs = min(min_abs, j - i)

        if min_abs != float('inf'):
            return min_abs
        else:
```
