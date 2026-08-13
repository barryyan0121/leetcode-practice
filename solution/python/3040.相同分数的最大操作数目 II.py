"""3040. 相同分数的最大操作数目 II"""

from functools import cache


class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        @cache
        def dfs(left: int, right: int, score: int) -> int:
            if right - left + 1 < 2:
                return 0
            best = 0
            if nums[left] + nums[left + 1] == score:
                best = max(best, 1 + dfs(left + 2, right, score))
            if nums[right - 1] + nums[right] == score:
                best = max(best, 1 + dfs(left, right - 2, score))
            if nums[left] + nums[right] == score:
                best = max(best, 1 + dfs(left + 1, right - 1, score))
            return best

        n = len(nums)
        return max(
            1 + dfs(2, n - 1, nums[0] + nums[1]),
            1 + dfs(0, n - 3, nums[-2] + nums[-1]),
            1 + dfs(1, n - 2, nums[0] + nums[-1]),
        )


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 2, 3, 4], 3),
        ([3, 2, 6, 1, 4], 2),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maxOperations(nums) == expected
