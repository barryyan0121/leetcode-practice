# @lc app=leetcode.cn id=1451 lang=python3


class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.lower().split()
        words.sort(key=len)
        return " ".join([words[0].capitalize(), *words[1:]])


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.arrangeWords, ("Leetcode is cool",), "Is cool leetcode")]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1451 题 "重新排列句子中的单词" 所有测试用例通过')
