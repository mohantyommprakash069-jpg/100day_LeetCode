# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        
#         return len(s.split()[-1])

# class Solution(object):
#     def lengthOfLastWord(self, s):

#         count = 0
#         i = len(s) - 1

#         # Skip trailing spaces
#         while i >= 0 and s[i] == " ":
#             i -= 1

#         # Count last word characters
#         while i >= 0 and s[i] != " ":
#             count += 1
#             i -= 1

#         return count
class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == " " and count == 0:
                continue
            elif s[i] == " ":
                break
            count+=1
        return count
