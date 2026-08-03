# @lc app=leetcode.cn id=1481 lang=python3

from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        frequencies = sorted(Counter(arr).values())
        removed = 0
        for frequency in frequencies:
            if k < frequency:
                break
            k -= frequency
            removed += 1
        return len(frequencies) - removed


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.findLeastNumOfUniqueInts, ([5, 5, 4], 1), 1)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1481 题 "不同整数的最少数目" 所有测试用例通过')
