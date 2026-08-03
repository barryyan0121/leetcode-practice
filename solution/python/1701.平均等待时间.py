# @lc app=leetcode.cn id=1701 lang=python3


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        finish = total = 0
        for arrival, duration in customers:
            finish = max(finish, arrival) + duration
            total += finish - arrival
        return total / len(customers)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.averageWaitingTime, ([[1, 2], [2, 5], [4, 3]],), 5.0)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1701 题 "平均等待时间" 所有测试用例通过')
