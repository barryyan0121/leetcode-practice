# @lc app=leetcode.cn id=1399 lang=python3
from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = Counter(sum(map(int, str(value))) for value in range(1, n + 1))
        largest = max(counts.values())
        return sum(value == largest for value in counts.values())


if __name__ == "__main__":
    test_cases = [
        (Solution().countLargestGroup, (13,), 4),
        (Solution().countLargestGroup, (2,), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1399 题 "统计最大组的数目" 所有测试用例通过')
