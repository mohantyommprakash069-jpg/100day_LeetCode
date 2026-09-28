class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth+=1
                ans = max(ans,depth)
            elif s[i] == ')':
                depth-=1
        return ans