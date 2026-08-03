# @lc app=leetcode.cn id=1450 lang=python3


class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:
        return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.busyStudent, ([1, 2, 3], [3, 2, 7], 4), 1)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1450 题 "在既定时间做作业的学生人数" 所有测试用例通过')
