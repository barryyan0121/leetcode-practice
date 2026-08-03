# @lc app=leetcode.cn id=2552 lang=python3


class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        length = len(nums)
        answer = 0
        for third in range(2, length - 1):
            suffix_mask = 0
            for value in nums[third + 1 :]:
                suffix_mask |= 1 << value
            left_smaller = 0
            for second in range(1, third):
                if nums[second - 1] < nums[third]:
                    left_smaller += 1
                if nums[third] < nums[second]:
                    answer += left_smaller * (suffix_mask >> nums[second]).bit_count()
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countQuadruplets, ([1, 3, 2, 4],), 1),
        (solution.countQuadruplets, ([1, 2, 3, 4],), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2552 题 "统计上升四元组" 所有测试用例通过')
