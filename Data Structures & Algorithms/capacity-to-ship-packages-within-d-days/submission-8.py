class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l ,r = max(weights), sum(weights)

        while l <= r:
            m = (l + r) // 2
            d, curr = 1, 0

            for w in weights:
                curr += w
                if curr > m:
                    d += 1
                    curr = w

            if d > days:
                l = m + 1
            elif d <= days:
                r = m - 1

        return l