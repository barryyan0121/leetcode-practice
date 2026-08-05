"""1977. 划分数字的方案数"""

from array import array


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        mod = 10**9 + 7
        n = len(num)
        if num[0] == "0":
            return 0
        lcp = [array("H", [0]) * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            row = lcp[i]
            next_row = lcp[i + 1]
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    row[j] = next_row[j + 1] + 1
        dp = [array("I", [0]) * (n + 1) for _ in range(n)]
        for end in range(1, n + 1):
            if num[0] != "0" or end == 1:
                dp[0][end] = 1
        for start in range(1, n):
            if num[start] == "0":
                dp[start][start + 1] = 0
            column_prefix = [0] * (start + 1)
            for previous in range(start):
                column_prefix[previous + 1] = (
                    column_prefix[previous] + dp[previous][start]
                ) % mod
            for end in range(start + 1, n + 1):
                length = end - start
                if num[start] == "0" and length > 1:
                    continue
                first = max(0, start - length + 1)
                value = (column_prefix[start] - column_prefix[first]) % mod
                equal_start = start - length
                if equal_start >= 0:
                    common = lcp[equal_start][start]
                    if (
                        common >= length
                        or num[equal_start + common] <= num[start + common]
                    ):
                        value = (value + dp[equal_start][start]) % mod
                dp[start][end] = value
        return sum(dp[start][n] for start in range(n)) % mod


if __name__ == "__main__":
    test_cases = [(("327",), 2), (("094",), 0), (("0",), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfCombinations(*args) == expected
