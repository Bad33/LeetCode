class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col=len(grid[0])
        nums=sum(grid,[])        
        k = k % len(nums)
        move=len(nums)-k
        res = grid
        count = 0
        nums = nums[move:] + nums[:move]
        for i in range(0,len(nums),col):
            res[count]=nums[i:i+col]
            count+=1
        return res
            
        