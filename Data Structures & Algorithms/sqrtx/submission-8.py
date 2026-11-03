class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x

        while lo <= hi:
            mid = (lo + hi) // 2
            sqrt = mid * mid

            if sqrt < x:
                lo = mid + 1
            elif sqrt > x:
                hi = mid - 1
            else:
                return mid
        return lo - 1