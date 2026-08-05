class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return -1
        a, b = min(nums), max(nums)
        return next(x for x in nums if a < x < b)


if __name__ == "__main__":
    assert Solution().findNonMinOrMax([3, 2, 1, 4]) == 3
