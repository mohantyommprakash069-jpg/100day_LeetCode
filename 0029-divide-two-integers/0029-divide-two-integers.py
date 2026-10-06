# class Solution(object):
#     def divide(self, dividend, divisor):

#         if dividend == -2147483648 and divisor == -1:
#             return 2147483647

#         negative = (dividend < 0) != (divisor < 0)

#         dividend = abs(dividend)
#         divisor = abs(divisor)

#         quotient = 0

#         while dividend >= divisor:

#             dividend -= divisor

#             quotient += 1

#         if negative:
#             quotient = -quotient

#         return quotient
class Solution(object):
    def divide(self, dividend, divisor):
        # Handle overflow case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Find the sign of the answer
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            value = divisor
            count = 1

            # Double the divisor while possible
            while dividend >= (value << 1):
                value = value << 1
                count = count << 1

            dividend -= value
            quotient += count

        # Apply sign
        if negative:
            quotient = -quotient

        return quotient