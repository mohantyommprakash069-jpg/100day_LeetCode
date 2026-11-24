
# class Solution(object):
#     def distinctPrimeFactors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         d = set()

#         for num in nums:
#             i = 2

#             while i * i <= num:
#                 if num % i == 0:
#                     d.add(i)

#                     while num % i == 0:
#                         num = num // i

#                 i += 1

#             if num > 1:
#                 d.add(num)

#         return len(d)

class Solution(object):
    def distinctPrimeFactors(self, nums):
        d = set()

        for num in nums:
            i = 2

            while num > 1:
                if num % i == 0:
                    d.add(i)
                    num = num // i
                else:
                    i += 1

        return len(d)

