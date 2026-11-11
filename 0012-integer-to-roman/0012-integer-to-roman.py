
class Solution(object):
    def intToRoman(self, num):

        values = [1000, 900, 500, 400, 100, 90,
                  50, 40, 10, 9, 5, 4, 1]

        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                  'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        result = ""

        for i in range(len(values)):
            count = num // values[i]

            result += symbol[i] * count

            num = num % values[i]

        return result
