class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        l = []
        if len(nums) == len(set(nums)):
            return nums
        
        res = Counter(nums)
        
        dict(sorted(res.items(), key=lambda item:item[1]))
        l = res.most_common()
        
        return [x[0] for x in l[:k]]
        
        