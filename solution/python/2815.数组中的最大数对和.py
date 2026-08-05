class Solution:
    def maxSum(self, nums: list[int]) -> int:
        best = {}
        ans = -1
        for value in nums:
            digit = max(map(int, str(value)))
            if digit in best:
                ans = max(ans, value + best[digit])
            best[digit] = max(best.get(digit, 0), value)
        return ans


if __name__ == "__main__":
    assert Solution().maxSum([51, 71, 17, 24, 42]) == 88
