from bisect import bisect_left, insort


class Solution:
    def minAbsoluteDifference(self, nums: list[int], x: int) -> int:
        values = []
        ans = 10**18
        for i in range(x, len(nums)):
            insort(values, nums[i - x])
            pos = bisect_left(values, nums[i])
            if pos < len(values):
                ans = min(ans, values[pos] - nums[i])
            if pos:
                ans = min(ans, nums[i] - values[pos - 1])
        return ans


if __name__ == "__main__":
    assert Solution().minAbsoluteDifference([4, 3, 2, 4], 2) == 0
