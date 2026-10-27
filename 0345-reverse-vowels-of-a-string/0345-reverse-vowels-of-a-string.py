class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        left = 0
        right = len(s)-1
        vowel = 'aeiouAEIOU'

        while left<right:
            if s[left] not in vowel:
                left+=1
            elif s[right] not in vowel:
                right-=1
            else:
                temp = s[right]
                s[right] = s[left]
                s[left] = temp
                left+=1
                right-=1
        return "".join(s)
