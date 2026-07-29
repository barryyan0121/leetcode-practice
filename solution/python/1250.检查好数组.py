from functools import reduce
from math import gcd
from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1


if __name__ == "__main__":
    test_cases = [([12, 5, 7, 23], True), ([29, 6, 10], True), ([3, 6], False)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().isGoodArray(nums) == expected
