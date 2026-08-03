# @lc app=leetcode.cn id=1318 lang=python3


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            abit, bbit, cbit = a & 1, b & 1, c & 1
            if cbit == 0:
                flips += abit + bbit
            elif abit == 0 and bbit == 0:
                flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips


if __name__ == "__main__":
    test_cases = [
        (Solution().minFlips, (2, 6, 5), 3),
        (Solution().minFlips, (4, 2, 7), 1),
        (Solution().minFlips, (1, 2, 3), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1318 题 "或运算的最小翻转次数" 所有测试用例通过')
