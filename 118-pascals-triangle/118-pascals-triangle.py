class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]].append(
        """
        res = []
        final= []
        for x in range(numRows):
            l = len(res)
            res = [1 if i == 0 or i == l else res[i-1]+res[i] for i in range(l+1)]
            final.append(res)
        return final

            
    
