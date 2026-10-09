class Solution(object):
    def countAndSay(self, n):
        s = "1"

        for i in range(n - 1):
            ans = ""
            count = 1

            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    count += 1
                else:
                    ans += str(count) + s[j - 1]
                    count = 1

            ans += str(count) + s[-1]
            s = ans

        return s