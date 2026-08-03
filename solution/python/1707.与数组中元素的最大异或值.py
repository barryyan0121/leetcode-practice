# @lc app=leetcode.cn id=1707 lang=python3


class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        mask = (1 << maximumBit) - 1
        current = 0
        for value in nums:
            current ^= value
        answer = []
        for value in reversed(nums):
            answer.append(mask ^ current)
            current ^= value
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.getMaximumXor, ([0, 1, 1, 3], 2), [0, 3, 2, 3]),
        (solution.getMaximumXor, ([2, 3, 4, 7], 3), [5, 2, 6, 5]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1707 题 "与数组中元素的最大异或值" 所有测试用例通过')
