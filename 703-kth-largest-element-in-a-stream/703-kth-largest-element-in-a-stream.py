class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.ar = nums
        

    def add(self, val: int) -> int:
        self.ar.append(val)
        self.ar.sort()
        return self.ar[len(self.ar) - self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)