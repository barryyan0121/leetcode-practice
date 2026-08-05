"""4010. 数对的最大强度"""

from math import gcd


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        answer = 0
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                divisor = gcd(nums[left], nums[right])
                answer = max(answer, nums[left] * nums[right] // (divisor * divisor))
        return answer


if __name__ == "__main__":
    test_cases = [(([2, 3, 5],), 15), (([4, 6, 8],), 12), (([3, 3],), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxPairStrength(*args) == expected
