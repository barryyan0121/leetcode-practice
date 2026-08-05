"""2450. 应用操作后不同二进制字符串的数量"""


class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        return pow(2, len(s) - k + 1, 10**9 + 7)


if __name__ == "__main__":
    test_cases = [(("1001", 3), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countDistinctStrings(*args) == expected
