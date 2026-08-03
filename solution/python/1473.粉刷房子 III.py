# @lc app=leetcode.cn id=1473 lang=python3


class Solution:
    def minCost(
        self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int
    ) -> int:
        infinity = 10**18
        dp = [[infinity] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for index, house in enumerate(houses):
            next_dp = [[infinity] * (target + 1) for _ in range(n + 1)]
            colors = range(1, n + 1) if house == 0 else [house]
            for previous_color in range(n + 1):
                for groups in range(target + 1):
                    previous = dp[previous_color][groups]
                    if previous == infinity:
                        continue
                    for color in colors:
                        new_groups = groups + (color != previous_color)
                        if new_groups <= target:
                            painting = 0 if house else cost[index][color - 1]
                            next_dp[color][new_groups] = min(
                                next_dp[color][new_groups], previous + painting
                            )
            dp = next_dp
        answer = min(dp[color][target] for color in range(1, n + 1))
        return -1 if answer == infinity else answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.minCost,
            ([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3),
            9,
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1473 题 "粉刷房子 III" 所有测试用例通过')
