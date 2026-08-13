"""2256. 最小平均差"""


class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        total = sum(nums)
        prefix = answer = 0
        best = float("inf")
        for i, value in enumerate(nums):
            prefix += value
            difference = (
                abs(prefix // (i + 1) - (total - prefix) // (len(nums) - i - 1))
                if i + 1 < len(nums)
                else abs(prefix // (i + 1))
            )
            if difference < best:
                best, answer = difference, i
        return answer


if __name__ == "__main__":
    assert Solution().minimumAverageDifference([2, 5, 3, 9, 5, 3]) == 3
