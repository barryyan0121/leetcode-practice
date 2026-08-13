from collections import Counter
from typing import List


class Solution:
    def delayedCount(self, nums: List[int], k: int) -> List[int]:
        counts = Counter()
        answer = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i + k + 1 < len(nums):
                counts[nums[i + k + 1]] += 1
            answer[i] = counts[nums[i]]
        return answer


if __name__ == "__main__":
    assert Solution().delayedCount([1, 2, 1, 1], 1) == [2, 0, 0, 0]
