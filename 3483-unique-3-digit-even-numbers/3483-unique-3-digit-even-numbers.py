class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        count = 0

        for num in range(100, 1000):

            # Number must be even
            if num % 2 != 0:
                continue

            # Get the three digits
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Count required digits
            required = [a, b, c]

            # Check if digits are available
            temp = digits[:]
            possible = True

            for d in required:
                if d in temp:
                    temp.remove(d)
                else:
                    possible = False
                    break

            if possible:
                count += 1

        return count