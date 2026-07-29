from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int, {0: 1})
        answer = odds = 0
        for num in nums:
            odds += num % 2
            answer += count[odds - k]
            count[odds] += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 1, 2, 1, 1], 3), 2), (([2, 4, 6], 1), 0)]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().numberOfSubarrays(nums, k) == expected
