# @lc app=leetcode.cn id=2306 lang=python3


class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        groups = [set() for _ in range(26)]
        for idea in ideas:
            groups[ord(idea[0]) - ord("a")].add(idea[1:])
        result = 0
        for first in range(26):
            for second in range(first + 1, 26):
                common = len(groups[first] & groups[second])
                result += (
                    2 * (len(groups[first]) - common) * (len(groups[second]) - common)
                )
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.distinctNames, (["coffee", "donuts", "time", "toffee"],), 6),
        (solution.distinctNames, (["lack", "back"],), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2306 题 "公司命名" 所有测试用例通过')
