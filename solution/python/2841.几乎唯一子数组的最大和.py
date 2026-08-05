class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        counts = {}
        total = 0
        ans = 0
        for i, value in enumerate(nums):
            counts[value] = counts.get(value, 0) + 1
            total += value
            if i >= k:
                old = nums[i - k]
                counts[old] -= 1
                if counts[old] == 0:
                    del counts[old]
                total -= old
            if i >= k - 1 and len(counts) >= m:
                ans = max(ans, total)
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSum([2, 6, 7, 3, 1, 7], 3, 4) == 18
    assert solution.maxSum([1, 2, 1, 2, 1, 2, 1], 3, 3) == 0
