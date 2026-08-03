# @lc app=leetcode.cn id=1360 lang=python3

from datetime import date


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        first = date.fromisoformat(date1)
        second = date.fromisoformat(date2)
        return abs((first - second).days)


if __name__ == "__main__":
    test_cases = [
        (Solution().daysBetweenDates, ("2019-06-29", "2019-06-30"), 1),
        (Solution().daysBetweenDates, ("2020-01-15", "2019-12-31"), 15),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1360 题 "日期之间隔几天" 所有测试用例通过')
