class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            hr = 0

            for p in piles:
                hr += math.ceil(p / m)
            
            if h < hr:
                l = m + 1
            elif h >= hr:
                r = m - 1

        return l