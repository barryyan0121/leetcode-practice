from collections import Counter
from itertools import product
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half = (n + 1) // 2
        palindromic_counts = set()
        for first in range(1, 10):
            for rest in product(range(10), repeat=half - 1):
                left = (first,) + rest
                right = left[: n // 2][::-1]
                palindrome = left + right
                value = 0
                for digit in palindrome:
                    value = (value * 10 + digit) % k
                if value == 0:
                    palindromic_counts.add(
                        tuple(Counter(palindrome)[digit] for digit in range(10))
                    )

        answer = 0
        for counts in palindromic_counts:
            permutations = factorial(n)
            for count in counts:
                permutations //= factorial(count)
            if counts[0]:
                leading_zero = factorial(n - 1)
                leading_zero //= factorial(counts[0] - 1)
                for count in counts[1:]:
                    leading_zero //= factorial(count)
                permutations -= leading_zero
            answer += permutations
        return answer


if __name__ == "__main__":
    test_cases = [((3, 5), 27), ((1, 4), 2), ((5, 6), 2468)]
    for _, ((n, k), expected) in enumerate(test_cases):
        assert Solution().countGoodIntegers(n, k) == expected
