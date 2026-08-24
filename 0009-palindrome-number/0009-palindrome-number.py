class Solution(object):
    def isPalindrome(self, x):

        temp = x
        reverse = 0
        while x > 0:
            remain = x%10
            reverse = (reverse*10)+remain
            x = x//10

        if temp == reverse:
            return True
        else:
            return False
        