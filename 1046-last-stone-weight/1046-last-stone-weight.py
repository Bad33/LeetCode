class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if len(stones) > 1:
                r1 = max(stones)
                stones.remove(r1)
                print(stones)
                r2 = max(stones)
                stones.remove(r2)
                if r1 >= r2:
                    res = r1 - r2
                    stones.append(res)
            elif len(stones) == 1:
                return stones[0]
            elif len(stones) == 0:
                return 0