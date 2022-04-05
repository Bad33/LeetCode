class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_final = -sys.maxsize - 1
        max_curr = 0
        for i in range(0,len(nums)):
            max_curr = max_curr + nums[i]
            if(max_final < max_curr):
                max_final = max_curr
            if max_curr < 0:
                max_curr = 0
            
        return(max_final)
            
        