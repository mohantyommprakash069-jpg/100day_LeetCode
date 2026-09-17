class Solution(object):

    def compress(self, chars):
        left = 0
        right = 0
        n = len(chars)

        while right < n:
            ch = chars[right]
            count = 0

            while right < n and chars[right] == ch:
                count += 1
                right += 1

            chars[left] = ch
            left += 1

            if count > 1:
                for digit in str(count):
                    chars[left] = digit
                    left += 1

        return left