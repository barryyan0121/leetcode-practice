# @lc app=leetcode.cn id=1471 lang=python3


class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        arr.sort(key=lambda value: (abs(value - median), value), reverse=True)
        return arr[:k]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.getStrongest, ([1, 2, 3, 4, 5], 2), [5, 1])]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1471 题 "数组中的 k 个最强值" 所有测试用例通过')
