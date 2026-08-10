"""2219. 数组的最大总分"""


class Solution:
    def maximumSumScore(self, nums: list[int]) -> int:
        total = sum(nums)
        prefix = 0
        answer = -(10**30)
        for value in nums:
            prefix += value
            answer = max(answer, prefix, total - prefix + value)
        return answer


if __name__ == "__main__":
    assert Solution().maximumSumScore([4, 3, -2, 5]) == 10
    assert Solution().maximumSumScore([-3, -5]) == -3
