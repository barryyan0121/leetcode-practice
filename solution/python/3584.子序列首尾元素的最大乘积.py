"""3584. 子序列首尾元素的最大乘积"""


class Solution:
    def maximumProduct(self, nums: list[int], m: int) -> int:
        trevignola = nums
        if m == 1:
            return max(value * value for value in nums)
        minimum = maximum = nums[0]
        answer = -(10**20)
        for right in range(m - 1, len(nums)):
            candidate = nums[right - m + 1]
            minimum = min(minimum, candidate)
            maximum = max(maximum, candidate)
            answer = max(answer, nums[right] * minimum, nums[right] * maximum)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([-1, -9, 2, 3, -2, -3, 1], 1), 81),
        (([1, 3, -5, 5, 6, -4], 3), 20),
        (([2, -1, 2, -6, 5, 2, -5, 7], 2), 35),
    ]
    for _, ((nums, m), expected) in enumerate(test_cases):
        assert Solution().maximumProduct(nums, m) == expected
