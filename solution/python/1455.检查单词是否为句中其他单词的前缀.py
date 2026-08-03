# @lc app=leetcode.cn id=1455 lang=python3


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return next(
            (
                index
                for index, word in enumerate(sentence.split(), 1)
                if word.startswith(searchWord)
            ),
            -1,
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.isPrefixOfWord, ("i love eating burger", "burg"), 4)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1455 题 "检查单词是否为句中其他单词的前缀" 所有测试用例通过')
