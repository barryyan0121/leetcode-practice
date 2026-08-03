# @lc app=leetcode.cn id=1639 lang=python3


class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        mod = 10**9 + 7
        width = len(words[0])
        counts = [[0] * 26 for _ in range(width)]
        for word in words:
            for index, char in enumerate(word):
                counts[index][ord(char) - 97] += 1
        dp = [0] * (len(target) + 1)
        dp[0] = 1
        for column in range(width):
            for index in range(min(column + 1, len(target)), 0, -1):
                dp[index] = (
                    dp[index]
                    + dp[index - 1] * counts[column][ord(target[index - 1]) - 97]
                ) % mod
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numWays, (["acca", "bbbb", "caca"], "aba"), 6),
        (solution.numWays, (["abba", "baab"], "bab"), 4),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1639 题 "通过给定词典构造目标字符串的方案数" 所有测试用例通过')
