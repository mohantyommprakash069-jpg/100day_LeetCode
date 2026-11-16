class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True  
        row = 0
        col = len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]>target:
                col-=1
            else:
                row+=1      