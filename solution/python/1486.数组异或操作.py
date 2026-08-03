# @lc app=leetcode.cn id=1486 lang=python3


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for index in range(n):
            result ^= start + 2 * index
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.xorOperation, (5, 0), 8)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1486 题 "数组异或操作" 所有测试用例通过')
