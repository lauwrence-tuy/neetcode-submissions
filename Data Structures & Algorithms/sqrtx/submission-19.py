class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x

        while l <= h:
            m = (l + h) // 2
            sqrt = m * m

            if x > sqrt:
                l = m + 1
            elif x < sqrt:
                h = m - 1
            else:
                return m
        return l - 1