"""3848. 阶数数字排列"""

from collections import Counter
from math import factorial


class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        factorials = [factorial(digit) for digit in range(10)]
        total = sum(factorials[int(ch)] for ch in str(n))
        return Counter(str(n)) == Counter(str(total))


if __name__ == "__main__":
    test_cases = [((145,), True), ((10,), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isDigitorialPermutation(*args) is expected
