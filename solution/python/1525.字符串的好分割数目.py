# @lc app=leetcode.cn id=1525 lang=python3


from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        remaining = Counter(s)
        right = len(remaining)
        left = set()
        result = 0
        for index in range(len(s) - 1):
            left.add(s[index])
            remaining[s[index]] -= 1
            if remaining[s[index]] == 0:
                right -= 1
            result += len(left) == right
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.numSplits, ("aacaba",), 2)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1525 题 "字符串的好分割数目" 所有测试用例通过')
