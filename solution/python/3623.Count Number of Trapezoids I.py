from collections import Counter
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        rows = Counter(y for _, y in points)
        vals = [c * (c - 1) // 2 for c in rows.values() if c >= 2]
        ans = 0
        pref = 0
        for v in vals:
            ans = (ans + pref * v) % MOD
            pref = (pref + v) % MOD
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]) == 3
    assert s.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]) == 1
    print("3623 ok")
