# @lc app=leetcode.cn id=2202 lang=python3


class Solution:
    def maximumTop(self, nums: list[int], k: int) -> int:
        length = len(nums)
        if k == 0:
            return nums[0]
        if length == 1:
            return nums[0] if k % 2 == 0 else -1
        if k == length:
            return max(nums[:-1])
        if k > length:
            return max(nums)
        return max(max(nums[: k - 1], default=-1), nums[k])


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maximumTop, ([5, 2, 2, 4, 0, 6], 4), 5),
        (solution.maximumTop, ([2], 1), -1),
        (solution.maximumTop, ([1, 2, 3], 2), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2202 题 "K 次操作后最大化顶端元素" 所有测试用例通过')
