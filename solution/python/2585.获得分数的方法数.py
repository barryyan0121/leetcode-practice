"""2585. 获得分数的方法数"""


class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        modulo = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for count, marks in types:
            for score in range(target, -1, -1):
                for used in range(1, min(count, score // marks) + 1):
                    dp[score] = (dp[score] + dp[score - used * marks]) % modulo
        return dp[target]


if __name__ == "__main__":
    test_cases = [((6, [[6, 1], [3, 2], [2, 3]]), 7)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().waysToReachTarget(*args) == expected
