# @lc app=leetcode.cn id=1342 lang=python3


class Solution:
    def numberOfSteps(self, num: int) -> int:
        return num.bit_length() + num.bit_count() - 1 if num else 0


if __name__ == "__main__":
    test_cases = [
        (Solution().numberOfSteps, (14,), 6),
        (Solution().numberOfSteps, (8,), 4),
        (Solution().numberOfSteps, (0,), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1342 题 "将数字变成 0 的操作次数" 所有测试用例通过')
