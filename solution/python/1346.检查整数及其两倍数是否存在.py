# @lc app=leetcode.cn id=1346 lang=python3

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for value in arr:
            if value * 2 in seen or (value % 2 == 0 and value // 2 in seen):
                return True
            seen.add(value)
        return False


if __name__ == "__main__":
    test_cases = [
        (Solution().checkIfExist, ([10, 2, 5, 3],), True),
        (Solution().checkIfExist, ([3, 1, 7, 11],), False),
        (Solution().checkIfExist, ([0, 0],), True),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1346 题 "检查整数及其两倍数是否存在" 所有测试用例通过')
