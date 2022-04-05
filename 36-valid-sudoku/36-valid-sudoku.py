class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res = []
    
        def row_valid():
            for row in board:
                if not valid_fun(row):
                    return False
            return True
        
        def col_valid():
            for col in zip(*board):
                if not valid_fun(col):
                    return False
            return True
            
        def sub_box_valid():
            for i in (0,3,6):
                for j in (0,3,6):
                    box = [board[x][y] for x in range(i,i+3) for y in range(j, j+3)]
                    if not valid_fun(box):
                        return False
            return True

                
       
        def valid_fun(val):
            res =  [i for i in val if i != '.']
            return len(res) == len(set(res))
        
        return row_valid() and col_valid() and sub_box_valid()
        