# @lc app=leetcode.cn id=1478 lang=python3


class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        houses.sort()
        length = len(houses)
        cost = [[0] * length for _ in range(length)]
        for left in range(length):
            for right in range(left, length):
                median = houses[(left + right) // 2]
                cost[left][right] = sum(
                    abs(houses[index] - median) for index in range(left, right + 1)
                )
        infinity = 10**18
        dp = [[infinity] * (length + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for mailboxes in range(1, k + 1):
            for count in range(1, length + 1):
                for previous in range(count):
                    if dp[mailboxes - 1][previous] != infinity:
                        dp[mailboxes][count] = min(
                            dp[mailboxes][count],
                            dp[mailboxes - 1][previous] + cost[previous][count - 1],
                        )
        return dp[k][length]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.minDistance, ([1, 4, 8, 10, 20], 3), 5)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1478 题 "安排邮筒" 所有测试用例通过')
