from collections import Counter
from typing import List


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        counts = Counter()
        total = 0
        left = 0
        answer = len(nums) + 1
        for right, value in enumerate(nums):
            if counts[value] == 0:
                total += value
            counts[value] += 1
            while total >= k:
                answer = min(answer, right - left + 1)
                old = nums[left]
                counts[old] -= 1
                if counts[old] == 0:
                    total -= old
                left += 1
        return -1 if answer == len(nums) + 1 else answer


if __name__ == "__main__":
    s = Solution()
    assert s.minLength([2, 2, 3, 1], 4) == 2
    assert s.minLength([3, 2, 3, 4], 5) == 2
    assert s.minLength([5, 5, 4], 5) == 1
