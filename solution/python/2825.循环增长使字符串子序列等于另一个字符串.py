# @lc app=leetcode.cn id=2825 lang=python3


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        target = 0
        for char in str1:
            if target < len(str2) and (
                char == str2[target]
                or chr((ord(char) - ord("a") + 1) % 26 + ord("a")) == str2[target]
            ):
                target += 1
        return target == len(str2)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.canMakeSubsequence, ("abc", "ad"), True),
        (solution.canMakeSubsequence, ("zc", "ad"), True),
        (solution.canMakeSubsequence, ("ab", "d"), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2825 题 "循环增长使字符串子序列等于另一个字符串" 所有测试用例通过')
