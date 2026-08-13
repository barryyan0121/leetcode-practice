"""2364. 统计坏数对的数目"""

from collections import Counter


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        total = len(nums) * (len(nums) - 1) // 2
        good = sum(
            v * (v - 1) // 2
            for v in Counter(value - i for i, value in enumerate(nums)).values()
        )
        return total - good

if __name__ == "__main__":
    assert Solution().countBadPairs([4,1,3,3]) == 5
