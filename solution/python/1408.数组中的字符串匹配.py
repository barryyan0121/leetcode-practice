# @lc app=leetcode.cn id=1408 lang=python3


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        return [
            word
            for word in words
            if any(word != other and word in other for other in words)
        ]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.stringMatching,
            (["mass", "as", "hero", "superhero"],),
            ["as", "hero"],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1408 题 "数组中的字符串匹配" 所有测试用例通过')
