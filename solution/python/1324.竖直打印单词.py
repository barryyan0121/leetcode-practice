# @lc app=leetcode.cn id=1324 lang=python3

from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        result = []
        for column in range(max(map(len, words))):
            result.append(
                "".join(
                    word[column] if column < len(word) else " " for word in words
                ).rstrip()
            )
        return result


if __name__ == "__main__":
    test_cases = [
        (Solution().printVertically, ("HOW ARE YOU",), ["HAY", "ORO", "WEU"]),
        (
            Solution().printVertically,
            ("TO BE OR NOT TO BE",),
            ["TBONTB", "OEROOE", "   T"],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1324 题 "竖直打印单词" 所有测试用例通过')
