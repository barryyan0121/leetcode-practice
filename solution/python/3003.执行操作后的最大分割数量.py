# @lc app=leetcode.cn id=3003 lang=python3

from functools import lru_cache


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @lru_cache(None)
        def search(index: int, mask: int, changed: bool) -> int:
            if index == len(s):
                return 1

            def advance(char: int, current_mask: int, next_changed: bool) -> int:
                next_mask = current_mask | (1 << char)
                if next_mask.bit_count() > k:
                    return 1 + search(index + 1, 1 << char, next_changed)
                return search(index + 1, next_mask, next_changed)

            original = ord(s[index]) - ord("a")
            best = advance(original, mask, changed)
            if not changed:
                for char in range(26):
                    if char != original:
                        best = max(best, advance(char, mask, True))
            return best

        return search(0, 0, False)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxPartitionsAfterOperations, ("accca", 2), 3),
        (solution.maxPartitionsAfterOperations, ("aabaab", 3), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 3003 题 "执行操作后的最大分割数量" 所有测试用例通过')
