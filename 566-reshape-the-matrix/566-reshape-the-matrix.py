class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if mat == [] or r*c != len(mat)*len(mat[0]):
            return mat
        
        res = [[0 for j in range(c)] for i in range(r)]
        k = 0
        
        for row in mat:
            for ele in row:
                res[k // c][k % c] = ele
                k += 1
        return res
            
        
        