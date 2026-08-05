"""1987. 不同的好子序列数目"""


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10**9 + 7
        end_zero = end_one = 0
        has_zero = False
        for char in binary:
            if char == "0":
                end_zero = (end_zero + end_one) % mod
                has_zero = True
            else:
                end_one = (end_zero + end_one + 1) % mod
        return (end_zero + end_one + has_zero) % mod


if __name__ == "__main__":
    test_cases = [(("001",), 2), (("11",), 2), (("101",), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfUniqueGoodSubsequences(*args) == expected
