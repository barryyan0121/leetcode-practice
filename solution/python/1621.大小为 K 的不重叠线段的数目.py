# @lc app=leetcode.cn id=1621 lang=python3


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        choose = [[0] * (2 * k + 1) for _ in range(n + k)]
        for row in range(len(choose)):
            choose[row][0] = 1
            for col in range(1, min(row, 2 * k) + 1):
                choose[row][col] = (
                    choose[row - 1][col - 1] + choose[row - 1][col]
                ) % mod
        return choose[n + k - 1][2 * k]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numberOfSets, (4, 2), 5),
        (solution.numberOfSets, (3, 1), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1621 题 "大小为 K 的不重叠线段的数目" 所有测试用例通过')
