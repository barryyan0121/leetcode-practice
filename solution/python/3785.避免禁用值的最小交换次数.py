from collections import Counter
from typing import List


class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        a, b = Counter(nums), Counter(forbidden)
        if any(a[x] + b[x] > n for x in a):
            return -1
        bad = Counter(x for x, y in zip(nums, forbidden) if x == y)
        m = sum(bad.values())
        if not m:
            return 0
        return max((m + 1) // 2, max(bad.values()))


if __name__ == "__main__":
    s = Solution()
    assert s.minSwaps([1, 2, 3], [3, 2, 1]) == 1
    assert s.minSwaps([4, 6, 6, 5], [4, 6, 5, 5]) == 2
    assert s.minSwaps([7, 7], [8, 7]) == -1
    assert s.minSwaps([1, 2], [2, 1]) == 0
