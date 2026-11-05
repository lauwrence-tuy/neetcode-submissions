class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            hr = 0

            # loop thru piles
            for p in piles:
                # add each pile's to hours @ speed m
                hr += math.ceil(p / m)

            if h < hr:
                l = m + 1
            elif h >= hr:
                r = m - 1

        return l