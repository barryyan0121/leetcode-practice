# @lc app=leetcode.cn id=1370 lang=python3

from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        counts = Counter(s)
        result = []
        while len(result) < len(s):
            for char in sorted(counts):
                if counts[char]:
                    result.append(char)
                    counts[char] -= 1
            for char in sorted(counts, reverse=True):
                if counts[char]:
                    result.append(char)
                    counts[char] -= 1
        return "".join(result)


if __name__ == "__main__":
    test_cases = [
        (Solution().sortString, ("aaaabbbbcccc",), "abccbaabccba"),
        (Solution().sortString, ("rat",), "art"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1370 题 "上升下降字符串" 所有测试用例通过')
