"""3864. 划分二进制字符串的最小费用"""

from functools import lru_cache


class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        prefix = [0]
        for ch in s:
            prefix.append(prefix[-1] + (ch == "1"))

        @lru_cache(maxsize=None)
        def dfs(start: int, length: int) -> int:
            ones = prefix[start + length] - prefix[start]
            keep = flatCost if ones == 0 else length * ones * encCost
            if length % 2 == 1:
                return keep
            half = length // 2
            return min(keep, dfs(start, half) + dfs(start + half, half))

        return dfs(0, len(s))


if __name__ == "__main__":
    test_cases = [(("1010", 2, 1), 6), (("1010", 3, 10), 12), (("00", 1, 2), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCost(*args) == expected
