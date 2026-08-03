# @lc app=leetcode.cn id=1397 lang=python3
from functools import lru_cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        mod = 10**9 + 7
        prefix = [0] * len(evil)
        matched = 0
        for index in range(1, len(evil)):
            while matched and evil[index] != evil[matched]:
                matched = prefix[matched - 1]
            if evil[index] == evil[matched]:
                matched += 1
            prefix[index] = matched

        @lru_cache(None)
        def dp(index, state, low, high):
            if state == len(evil):
                return 0
            if index == n:
                return 1
            total = 0
            start = s1[index] if low else "a"
            end = s2[index] if high else "z"
            for char in map(chr, range(ord(start), ord(end) + 1)):
                next_state = state
                while next_state and evil[next_state] != char:
                    next_state = prefix[next_state - 1]
                if evil[next_state] == char:
                    next_state += 1
                if next_state == len(evil):
                    continue
                total += dp(
                    index + 1, next_state, low and char == start, high and char == end
                )
            return total % mod

        return dp(0, 0, True, True)


if __name__ == "__main__":
    test_cases = [
        (Solution().findGoodStrings, (2, "aa", "da", "b"), 51),
        (Solution().findGoodStrings, (8, "leetcode", "leetgoes", "leet"), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1397 题 "找到所有好字符串" 所有测试用例通过')
