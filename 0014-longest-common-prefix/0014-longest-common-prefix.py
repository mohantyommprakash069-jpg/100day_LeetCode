# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         prefix = strs[0]

#         for word in strs[1:]:
#             while not word.startswith(prefix):
#                 prefix = prefix[:-1]

#                 if prefix == "":
#                     return ""

#         return prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        left = strs[0]
        right = strs[-1]
        i = 0
        while i<len(left) and i<len(right):
            if left[i] != right[i]:
                break
            i+=1
        return left[:i]