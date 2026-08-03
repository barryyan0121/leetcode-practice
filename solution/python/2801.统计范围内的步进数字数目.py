# @lc app=leetcode.cn id=2801 lang=python3

from functools import lru_cache


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        modulus = 10**9 + 7

        def count(bound: str) -> int:
            @lru_cache(None)
            def search(index: int, previous: int, tight: bool, started: bool) -> int:
                if index == len(bound):
                    return 1
                limit = int(bound[index]) if tight else 9
                result = 0
                for digit in range(limit + 1):
                    next_tight = tight and digit == limit
                    if not started and digit == 0:
                        result += search(index + 1, -1, next_tight, False)
                    elif not started or abs(digit - previous) == 1:
                        result += search(index + 1, digit, next_tight, True)
                return result % modulus

            return search(0, -1, True, False)

        return (count(high) - count(self._decrement(low))) % modulus

    @staticmethod
    def _decrement(value: str) -> str:
        digits = list(value)
        index = len(digits) - 1
        while digits[index] == "0":
            digits[index] = "9"
            index -= 1
        digits[index] = str(int(digits[index]) - 1)
        result = "".join(digits).lstrip("0")
        return result or "0"


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countSteppingNumbers, ("1", "11"), 10),
        (solution.countSteppingNumbers, ("90", "101"), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2801 题 "统计范围内的步进数字数目" 所有测试用例通过')
