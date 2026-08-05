"""3591. 检查元素频次是否为质数"""

from collections import Counter


class Solution:
    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        for frequency in Counter(nums).values():
            if frequency > 1 and all(
                frequency % divisor for divisor in range(2, int(frequency**0.5) + 1)
            ):
                return True
        return False


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5, 4],), True),
        (([1, 2, 3, 4, 5],), False),
        (([2, 2, 2, 4, 4],), True),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().checkPrimeFrequency(nums) == expected
