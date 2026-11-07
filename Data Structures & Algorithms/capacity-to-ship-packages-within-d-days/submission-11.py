class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l <= r:
            m = (l + r) // 2
            curr = 0
            d = 1

            for w in weights:
                curr += w
                if curr > m:
                    d += 1
                    curr = w
            
            if days < d:
                l = m + 1
            else:
                r = m - 1
        return l