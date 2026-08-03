# @lc app=leetcode.cn id=1545 lang=python3


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        middle = 1 << (n - 1)
        if k == middle:
            return "1"
        if k < middle:
            return self.findKthBit(n - 1, k)
        mirrored = (1 << n) - k
        return "1" if self.findKthBit(n - 1, mirrored) == "0" else "0"


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findKthBit, (3, 1), "0"),
        (solution.findKthBit, (4, 11), "1"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1545 题 "找出第 N 个二进制字符串中的第 K 位" 所有测试用例通过')
