from collections import Counter
from functools import reduce
from operator import xor


class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        return reduce(
            xor, (value for value, count in Counter(nums).items() if count == 2), 0
        )


if __name__ == "__main__":
    test_cases = [([1, 2, 1, 3], 1), ([1, 2, 3], 0)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().duplicateNumbersXOR(nums) == expected
