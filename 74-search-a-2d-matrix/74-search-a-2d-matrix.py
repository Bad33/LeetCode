class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][len(matrix[0])-1] >= target:
                if target in matrix[i]:
                    return True
                else:
                    return False
            