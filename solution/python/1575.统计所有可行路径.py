# @lc app=leetcode.cn id=1575 lang=python3


class Solution:
    def countRoutes(
        self, locations: list[int], start: int, finish: int, fuel: int
    ) -> int:
        mod = 10**9 + 7
        n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]
        for remaining in range(fuel + 1):
            for city in range(n):
                dp[city][remaining] = (city == finish) + sum(
                    dp[next_city][
                        remaining - abs(locations[city] - locations[next_city])
                    ]
                    for next_city in range(n)
                    if next_city != city
                    and abs(locations[city] - locations[next_city]) <= remaining
                ) % mod
        return dp[start][fuel]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countRoutes, ([2, 3, 6, 8, 4], 1, 3, 5), 4),
        (solution.countRoutes, ([4, 3, 1], 1, 0, 6), 5),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1575 题 "统计所有可行路径" 所有测试用例通过')
