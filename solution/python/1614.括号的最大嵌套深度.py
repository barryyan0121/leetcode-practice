# @lc app=leetcode.cn id=1614 lang=python3


class Solution:
    def maxDepth(self, s: str) -> int:
        depth = answer = 0
        for char in s:
            if char == "(":
                depth += 1
                answer = max(answer, depth)
            elif char == ")":
                depth -= 1
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxDepth, ("(1+(2*3)+((8)/4))+1",), 3),
        (solution.maxDepth, ("(1)+((2))+(((3)))",), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1614 题 "括号的最大嵌套深度" 所有测试用例通过')
