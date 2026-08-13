"""2354. 优质数对的数目"""

from collections import Counter


class Solution:
    def countExcellentPairs(self, nums: list[int], k: int) -> int:
        counts = Counter(value.bit_count() for value in set(nums))
        return sum(
            a_count * b_count
            for a, a_count in counts.items()
            for b, b_count in counts.items()
            if a + b >= k
        )

if __name__ == "__main__":
    assert Solution().countExcellentPairs([1,2,3,1], 3) == 5
