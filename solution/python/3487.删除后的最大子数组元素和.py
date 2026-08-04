"""3487. 删除后的最大子数组元素和"""


class Solution:
    def maxSum(self, nums: list[int]) -> int:
        values = set(nums)
        positive_sum = sum(value for value in values if value > 0)
        return positive_sum if positive_sum else max(values)


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5],), 15),
        (([1, 1, 0, 1, 1],), 1),
        (([1, 2, -1, -2, 1, 0, -1],), 3),
        (([-5, -2, -8],), -2),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().maxSum(nums) == expected
