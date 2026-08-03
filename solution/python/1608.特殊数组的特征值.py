# @lc app=leetcode.cn id=1608 lang=python3


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        for value in range(1, n + 1):
            if sum(number >= value for number in nums) == value:
                return value
        return -1


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.specialArray, ([3, 5],), 2),
        (solution.specialArray, ([0, 0],), -1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1608 题 "特殊数组的特征值" 所有测试用例通过')
