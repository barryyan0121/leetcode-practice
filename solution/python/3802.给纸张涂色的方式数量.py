from bisect import bisect_left
from typing import List


class Solution:
    def numberOfWays(self, n: int, limit: List[int]) -> int:
        mod = 10**9 + 7
        values = sorted(limit)
        starts = {1, n}
        for value in values:
            starts.add(value + 1)
            starts.add(n - value + 1)
        starts.add(n // 2 + 1)
        starts = sorted(x for x in starts if 1 <= x <= n)

        def enough(threshold: int) -> int:
            return len(values) - bisect_left(values, threshold)

        answer = 0
        for i, left in enumerate(starts[:-1]):
            right = starts[i + 1] - 1
            if left > right:
                continue
            first = enough(left)
            second = enough(n - left)
            both = enough(max(left, n - left))
            answer += (right - left + 1) * (first * second - both)
        return answer % mod


if __name__ == "__main__":
    s = Solution()
    assert s.numberOfWays(4, [3, 1, 2]) == 6
    assert s.numberOfWays(3, [1, 2]) == 2
    assert s.numberOfWays(3, [2, 2]) == 4
