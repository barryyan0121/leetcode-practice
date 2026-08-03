# @lc app=leetcode.cn id=1358 lang=python3


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]
        result = 0
        for index, char in enumerate(s):
            last[ord(char) - ord("a")] = index
            result += min(last) + 1
        return result


if __name__ == "__main__":
    test_cases = [
        (Solution().numberOfSubstrings, ("abcabc",), 10),
        (Solution().numberOfSubstrings, ("aaacb",), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1358 题 "包含所有三种字符的子字符串数目" 所有测试用例通过')
