# @lc app=leetcode.cn id=1374 lang=python3


class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * n if n % 2 else "a" * (n - 1) + "b"


if __name__ == "__main__":
    test_cases = [
        (Solution().generateTheString, (4,), "aaab"),
        (Solution().generateTheString, (3,), "aaa"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1374 题 "生成每种字符都是奇数个的字符串" 所有测试用例通过')
