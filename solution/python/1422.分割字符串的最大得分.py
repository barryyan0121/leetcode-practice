# @lc app=leetcode.cn id=1422 lang=python3


class Solution:
    def maxScore(self, s: str) -> int:
        ones_right = s.count("1")
        zeros_left = best = 0
        for char in s[:-1]:
            if char == "0":
                zeros_left += 1
            else:
                ones_right -= 1
            best = max(best, zeros_left + ones_right)
        return best


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxScore, ("011101",), 5),
        (solution.maxScore, ("00111",), 5),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1422 题 "分割字符串的最大得分" 所有测试用例通过')
