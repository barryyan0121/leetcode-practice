# @lc app=leetcode.cn id=1544 lang=python3


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.makeGood, ("leEeetcode",), "leetcode")]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1544 题 "整理字符串" 所有测试用例通过')
