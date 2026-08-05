"""3698. 分割数组得到最小绝对差"""


class Solution:
    def splitArray(self, nums: list[int]) -> int:
        n = len(nums)
        increasing = [True] * n
        decreasing = [True] * n
        for index in range(1, n):
            increasing[index] = increasing[index - 1] and nums[index] > nums[index - 1]
        for index in range(n - 2, -1, -1):
            decreasing[index] = decreasing[index + 1] and nums[index] > nums[index + 1]
        total = sum(nums)
        left_sum = 0
        answer = None
        for index in range(n - 1):
            left_sum += nums[index]
            if increasing[index] and decreasing[index + 1]:
                answer = min(
                    answer or abs(2 * left_sum - total), abs(2 * left_sum - total)
                )
        return -1 if answer is None else answer


if __name__ == "__main__":
    test_cases = [(([1, 3, 2],), 2), (([1, 2, 4, 3],), 4), (([3, 1, 2],), -1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().splitArray(*args) == expected
