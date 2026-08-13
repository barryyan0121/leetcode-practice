"""3855. 给定范围内 K 位数字之和"""


class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        mod = 10**9 + 7
        count = r - l + 1
        digit_sum = (l + r) * count // 2
        repeated = (pow(10, k, mod) - 1) * pow(9, mod - 2, mod) % mod
        return digit_sum % mod * pow(count, k - 1, mod) % mod * repeated % mod


if __name__ == "__main__":
    test_cases = [((1, 2, 2), 66), ((0, 1, 3), 444), ((5, 5, 10), 555555520)]
    for args, expected in test_cases:
        assert Solution().sumOfNumbers(*args) == expected
