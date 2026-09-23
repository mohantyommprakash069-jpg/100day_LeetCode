class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
        l1 = [False]*26
        for c in range(len(sentence)):
            index = ord(sentence[c]) - ord('a')
            l1[index] = True

        for i in l1:
            if not i:
                return False
        return True