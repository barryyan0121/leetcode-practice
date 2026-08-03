# @lc app=leetcode.cn id=1470 lang=python3


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return [value for pair in zip(nums[:n], nums[n:]) for value in pair]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.shuffle, ([2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7])]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1470 题 "重新排列数组" 所有测试用例通过')
