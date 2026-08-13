"""3863. 将一个字符串排序的最小操作次数"""


class Solution:
    def minOperations(self, s: str) -> int:
        if list(s) == sorted(s):
            return 0

        minimum = min(s)
        maximum = max(s)
        if s[0] == minimum or s[-1] == maximum:
            return 1
        if s[0] == maximum and s[-1] == minimum:
            return -1

        has_min_prefix = minimum in s[:-1]
        has_max_suffix = maximum in s[1:]
        if not has_min_prefix and not has_max_suffix:
            return 3
        return 2


if __name__ == "__main__":
    test_cases = [(("dog",), 1), (("card",), 2), (("gf",), -1)]
    for args, expected in test_cases:
        assert Solution().minOperations(*args) == expected
