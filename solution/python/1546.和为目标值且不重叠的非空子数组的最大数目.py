# @lc app=leetcode.cn id=1546 lang=python3


class Solution:
    def maxNonOverlapping(self, nums: list[int], target: int) -> int:
        prefix = 0
        seen = {0}
        result = 0
        for value in nums:
            prefix += value
            if prefix - target in seen:
                result += 1
                prefix = 0
                seen = {0}
            else:
                seen.add(prefix)
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.maxNonOverlapping, ([1, 1, 1, 1, 1], 2), 2)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1546 题 "和为目标值且不重叠的非空子数组的最大数目" 所有测试用例通过')
