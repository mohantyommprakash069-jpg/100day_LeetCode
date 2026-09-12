# Minimum cuts to divide a circle

# Intuition

If there is only `1` part, we do not need any cut.

If `n` is even, one straight cut can create two equal parts. Therefore, we need `n / 2` cuts.

If `n` is odd, each cut can create one new equal part, so we need `n` cuts.

# Approach

1. If `n == 1`, return `0`.
2. If `n` is even, return `n // 2`.
3. If `n` is odd, return `n`.

# Complexity

* Time complexity: **O(1)**
* Space complexity: **O(1)**

# Code

```python
class Solution(object):

    def numberOfCuts(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 0

        elif n % 2 == 0:
            return n // 2

        elif n % 2 != 0:
            return n
```
