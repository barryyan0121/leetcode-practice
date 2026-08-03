# @lc app=leetcode.cn id=1569 lang=python3


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        comb = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % mod

        def count(values: list[int]) -> int:
            if len(values) <= 2:
                return 1
            left = [x for x in values[1:] if x < values[0]]
            right = [x for x in values[1:] if x > values[0]]
            return comb[len(values) - 1][len(left)] * count(left) * count(right) % mod

        return (count(nums) - 1) % mod


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numOfWays, ([2, 1, 3],), 1),
        (solution.numOfWays, ([3, 4, 5, 1, 2],), 5),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1569 题 "将子数组重新排序得到同一个二叉搜索树的方案数" 所有测试用例通过')
