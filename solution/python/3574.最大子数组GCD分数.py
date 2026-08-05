"""3574. 最大子数组 GCD 分数"""

from math import gcd


class Solution:
    def maxGCDScore(self, nums: list[int], k: int) -> int:
        answer = 0
        for left in range(len(nums)):
            current_gcd = 0
            minimum_twos = 60
            minimum_count = 0
            for right in range(left, len(nums)):
                value = nums[right]
                current_gcd = gcd(current_gcd, value)
                twos = (value & -value).bit_length() - 1
                if twos < minimum_twos:
                    minimum_twos, minimum_count = twos, 1
                elif twos == minimum_twos:
                    minimum_count += 1
                length = right - left + 1
                multiplier = 2 if minimum_count <= k else 1
                answer = max(answer, length * current_gcd * multiplier)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([2, 4], 1), 8),
        (([3, 5, 7], 2), 14),
        (([5, 5, 5], 1), 15),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().maxGCDScore(nums, k) == expected
