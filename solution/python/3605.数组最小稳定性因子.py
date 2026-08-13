from math import gcd
from typing import List


class Solution:
    def minimumStabilityFactor(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1
        st = [nums[:]]
        j = 1
        while (1 << j) <= n:
            prev = st[-1]
            size = n - (1 << j) + 1
            cur = [0] * size
            half = 1 << (j - 1)
            for i in range(size):
                cur[i] = gcd(prev[i], prev[i + half])
            st.append(cur)
            j += 1

        def window_gcd(l, r):
            k = lg[r - l + 1]
            return gcd(st[k][l], st[k][r - (1 << k) + 1])

        def check(length):
            need = 0
            last = -1
            for l in range(0, n - length + 1):
                if window_gcd(l, l + length - 1) >= 2 and l > last:
                    need += 1
                    last = l + length - 1
                    if need > maxC:
                        return False
            return True

        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid + 1):
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.minimumStabilityFactor([3, 5, 10], 1) == 1
    assert s.minimumStabilityFactor([2, 6, 8], 2) == 1
    assert s.minimumStabilityFactor([2, 4, 9, 6], 1) == 2
    print("3605 ok")
