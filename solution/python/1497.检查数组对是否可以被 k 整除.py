# @lc app=leetcode.cn id=1497 lang=python3

from collections import Counter


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        counts = Counter(value % k for value in arr)
        if counts[0] % 2:
            return False
        for remainder in range(1, (k + 1) // 2):
            if counts[remainder] != counts[k - remainder]:
                return False
        if k % 2 == 0 and counts[k // 2] % 2:
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.canArrange, ([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5), True)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1497 题 "检查数组对是否可以被 k 整除" 所有测试用例通过')
