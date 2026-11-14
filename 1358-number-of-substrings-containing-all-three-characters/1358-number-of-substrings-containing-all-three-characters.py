# class Solution(object):
#     def numberOfSubstrings(self, s):

#         count = 0
#         for i in range(len(s)):
#             a = 0
#             b = 0
#             c = 0
#             for j in range(i,len(s)):
#                 if s[j] == 'a':
#                     a+=1
#                 elif s[j] == 'b':
#                     b+=1
#                 else:
#                     c+=1
#                 if a>0 and b>0 and c>0:
#                     count+=1
#         return count
class Solution(object):
    def numberOfSubstrings(self, s):

        left = 0
        count = 0
        d = {'a': 0, 'b': 0, 'c': 0}

        for right in range(len(s)):

            d[s[right]] += 1

            while d['a'] > 0 and d['b'] > 0 and d['c'] > 0:

                count += len(s) - right

                d[s[left]] -= 1
                left += 1

        return count