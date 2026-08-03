# @lc app=leetcode.cn id=1556 lang=python3


class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:,}".replace(",", ".")


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.thousandSeparator, (987,), "987"),
        (solution.thousandSeparator, (1234,), "1.234"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1556 题 "千位分隔数" 所有测试用例通过')
