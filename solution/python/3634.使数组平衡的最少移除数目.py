"""3634. 使数组平衡的最少移除数目"""


class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = answer = 0
        for right, value in enumerate(nums):
            while value > nums[left] * k:
                left += 1
            answer = max(answer, right - left + 1)
        return len(nums) - answer


if __name__ == "__main__":
    test_cases = [(([2, 1, 5], 2), 1), (([1, 6, 2, 9], 3), 2), (([4, 6], 2), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minRemoval(*args) == expected
