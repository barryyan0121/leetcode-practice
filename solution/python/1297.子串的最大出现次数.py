# @lc app=leetcode.cn id=1297 lang=python3

from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = Counter(s[i : i + minSize] for i in range(len(s) - minSize + 1))
        return max(
            (
                frequency
                for word, frequency in counts.items()
                if len(set(word)) <= maxLetters
            ),
            default=0,
        )


if __name__ == "__main__":
    test_cases = [
        (Solution().maxFreq, ("aababcaab", 2, 3, 4), 2),
        (Solution().maxFreq, ("aaaa", 1, 3, 3), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1297 题 "子串的最大出现次数" 所有测试用例通过')
