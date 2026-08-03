# @lc app=leetcode.cn id=1541 lang=python3


class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = balance = 0
        index = 0
        while index < len(s):
            if s[index] == "(":
                balance += 1
                index += 1
            else:
                if index + 1 < len(s) and s[index + 1] == ")":
                    index += 2
                else:
                    insertions += 1
                    index += 1
                if balance:
                    balance -= 1
                else:
                    insertions += 1
        return insertions + balance * 2


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minInsertions, ("(()))",), 1),
        (solution.minInsertions, ("())",), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1541 题 "平衡括号字符串的最少插入次数" 所有测试用例通过')
