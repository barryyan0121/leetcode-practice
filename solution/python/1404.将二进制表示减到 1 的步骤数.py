# @lc app=leetcode.cn id=1404 lang=python3
class Solution:
    def numSteps(self, s: str) -> int:
        value = int(s, 2)
        steps = 0
        while value > 1:
            if value & 1:
                value += 1
            else:
                value //= 2
            steps += 1
        return steps


if __name__ == "__main__":
    test_cases = [
        (Solution().numSteps, ("1101",), 6),
        (Solution().numSteps, ("10",), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1404 题 "将二进制表示减到 1 的步骤数" 所有测试用例通过')
