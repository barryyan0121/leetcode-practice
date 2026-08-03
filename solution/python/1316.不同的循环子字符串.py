# @lc app=leetcode.cn id=1316 lang=python3


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        found = set()
        for start in range(len(text)):
            for half in range(1, (len(text) - start) // 2 + 1):
                middle = start + half
                if text[start:middle] == text[middle : middle + half]:
                    found.add(text[start : middle + half])
        return len(found)


if __name__ == "__main__":
    test_cases = [
        (Solution().distinctEchoSubstrings, ("abcabcabc",), 3),
        (Solution().distinctEchoSubstrings, ("leetcodeleetcode",), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1316 题 "不同的循环子字符串" 所有测试用例通过')
