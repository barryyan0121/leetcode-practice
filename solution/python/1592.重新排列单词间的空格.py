# @lc app=leetcode.cn id=1592 lang=python3


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(" ")
        gap, tail = divmod(spaces, len(words) - 1) if len(words) > 1 else (0, spaces)
        return (" " * gap).join(words) + " " * (tail if len(words) > 1 else spaces)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.reorderSpaces,
            ("  this   is  a sentence ",),
            "this   is   a   sentence",
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1592 题 "重新排列单词间的空格" 所有测试用例通过')
