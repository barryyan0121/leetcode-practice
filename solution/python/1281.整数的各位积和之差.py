from math import prod


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))
        return prod(digits) - sum(digits)


if __name__ == "__main__":
    test_cases = [(234, 15), (4421, 21)]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().subtractProductAndSum(n) == expected
