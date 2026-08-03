# @lc app=leetcode.cn id=1531 lang=python3

from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def solve(index: int, removed: int, previous: str, run: int) -> int:
            if removed > k:
                return 10**9
            if index == len(s):
                return 0
            best = solve(index + 1, removed + 1, previous, run)
            if s[index] == previous:
                increase = int(run in (1, 9, 99))
                best = min(
                    best,
                    increase + solve(index + 1, removed, previous, min(100, run + 1)),
                )
            else:
                best = min(best, 1 + solve(index + 1, removed, s[index], 1))
            return best

        return solve(0, 0, "", 0)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.getLengthOfOptimalCompression, ("aaabcccd", 2), 4)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1531 题 "压缩字符串 II" 所有测试用例通过')
