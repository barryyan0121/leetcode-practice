# @lc app=leetcode.cn id=1646 lang=python3


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        nums = [0, 1] + [0] * (n - 1)
        for index in range(2, n + 1):
            nums[index] = (
                nums[index // 2]
                if index % 2 == 0
                else nums[index // 2] + nums[index // 2 + 1]
            )
        return max(nums)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.getMaximumGenerated, (7,), 3),
        (solution.getMaximumGenerated, (2,), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1646 题 "获取生成数组中的最大值" 所有测试用例通过')
