"""4005. 使数组中所有元素相等的最小操作数 III"""

from collections import Counter
from math import isqrt


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        frequency = Counter(nums)
        if len(frequency) == 1:
            return 0
        divisible_by = Counter()
        for value, amount in frequency.items():
            for divisor in range(1, isqrt(value) + 1):
                if value % divisor == 0:
                    divisible_by[divisor] += amount
                    if divisor * divisor != value:
                        divisible_by[value // divisor] += amount

        answer = 2 * len(nums)
        for target in frequency:
            if target == 1:
                continue
            divisors = 0
            for divisor in range(1, isqrt(target) + 1):
                if target % divisor == 0:
                    divisors += frequency.get(divisor, 0)
                    if divisor * divisor != target:
                        divisors += frequency.get(target // divisor, 0)
            answer = min(answer, 2 * len(nums) - divisible_by[target] - divisors)
        return answer


if __name__ == "__main__":
    test_cases = [(([6, 12, 8],), 3), (([5, 15, 20],), 2), (([7, 7, 7],), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
