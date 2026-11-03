class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x

        while lo <= hi:
            mid = (lo + hi) // 2
            sqrt = mid * mid

            if sqrt == x:
                return mid
            elif sqrt < x:
                lo = mid + 1
            else:
                hi = mid - 1     
        return lo - 1