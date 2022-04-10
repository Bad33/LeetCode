
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        
        for i in range(len(ops)):
            if ops[i].isdigit() == True:
                res.append(int(ops[i]))
            elif ops[i][0] in ('-'):
                if ops[i][1].isdigit() == True:
                    res.append(int(ops[i]))
            elif ops[i] == '+':
                res.append(res[len(res)-2]+res[len(res)-1])
            elif ops[i] == 'D':
                res.append(res[len(res)-1]*2)
            elif ops[i] == 'C':
                res.remove(res[len(res)-1])
                
                
     
        return sum(res)  

    
            
