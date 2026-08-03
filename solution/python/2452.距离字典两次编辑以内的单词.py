# @lc app=leetcode.cn id=2452 lang=python3


class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        result = []
        for query in queries:
            if any(
                sum(left != right for left, right in zip(query, word)) <= 2
                for word in dictionary
                if len(word) == len(query)
            ):
                result.append(query)
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.twoEditWords,
            (["word", "note", "ants", "wood"], ["wood", "joke", "moat"]),
            ["word", "note", "wood"],
        ),
        (solution.twoEditWords, (["yes"], ["no"]), []),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2452 题 "距离字典两次编辑以内的单词" 所有测试用例通过')
