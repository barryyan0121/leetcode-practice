# @lc app=leetcode.cn id=1433 lang=python3


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        first, second = sorted(s1), sorted(s2)
        return all(a <= b for a, b in zip(first, second)) or all(
            a >= b for a, b in zip(first, second)
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.checkIfCanBreak, ("abc", "xya"), True),
        (solution.checkIfCanBreak, ("abe", "acd"), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1433 题 "检查一个字符串是否可以打破另一个" 所有测试用例通过')
