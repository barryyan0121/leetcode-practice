# @lc app=leetcode.cn id=1695 lang=python3


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()
        left = total = answer = 0
        for right, value in enumerate(nums):
            while value in seen:
                seen.remove(nums[left])
                total -= nums[left]
                left += 1
            seen.add(value)
            total += value
            answer = max(answer, total)
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maximumUniqueSubarray, ([4, 2, 4, 5, 6],), 17),
        (solution.maximumUniqueSubarray, ([5, 2, 1, 2, 5, 2, 1, 2, 5],), 8),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1695 题 "删除子数组的最大得分" 所有测试用例通过')
