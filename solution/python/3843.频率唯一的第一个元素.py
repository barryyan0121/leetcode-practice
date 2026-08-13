from collections import Counter
from typing import List


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        frequencies = Counter(nums)
        frequency_count = Counter(frequencies.values())
        for value in nums:
            if frequency_count[frequencies[value]] == 1:
                return value
        return -1


if __name__ == "__main__":
    assert Solution().firstUniqueFreq([20, 10, 30, 30]) == 30
    assert Solution().firstUniqueFreq([10, 10, 20, 20]) == -1
