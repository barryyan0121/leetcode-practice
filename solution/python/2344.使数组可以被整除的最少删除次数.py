"""2344. 使数组可以被整除的最少删除次数"""

from math import gcd
from functools import reduce


class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        divisor = reduce(gcd, numsDivide)
        for i, value in enumerate(sorted(nums)):
            if divisor % value == 0:
                return i
        return -1

if __name__ == "__main__":
    assert Solution().minOperations([2,3,2,4,3], [9,6,9,3,15]) == 2
