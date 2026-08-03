# @lc app=leetcode.cn id=1434 lang=python3


class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        mod = 10**9 + 7
        by_hat = [[] for _ in range(41)]
        for person, choices in enumerate(hats):
            for hat in choices:
                by_hat[hat].append(person)
        dp = [0] * (1 << len(hats))
        dp[0] = 1
        for people in by_hat:
            next_dp = dp[:]
            for mask, ways in enumerate(dp):
                if not ways:
                    continue
                for person in people:
                    if not mask & (1 << person):
                        next_dp[mask | (1 << person)] = (
                            next_dp[mask | (1 << person)] + ways
                        ) % mod
            dp = next_dp
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.numberWays, ([[3, 4], [4, 5], [5]],), 1)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1434 题 "每个人戴不同帽子的方案数" 所有测试用例通过')
