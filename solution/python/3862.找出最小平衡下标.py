"""3862. 找出最小平衡下标"""


class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        limit = total + 1
        right = [1] * len(nums)
        product = 1
        for index in range(len(nums) - 1, -1, -1):
            right[index] = product
            if product <= limit:
                product *= nums[index]
                if product > limit:
                    product = limit

        left_sum = 0
        for index, value in enumerate(nums):
            if left_sum == right[index]:
                return index
            left_sum += value
        return -1


if __name__ == "__main__":
    test_cases = [(([2, 1, 2],), 1), (([2, 8, 2, 2, 5],), 2), (([1],), -1)]
    for args, expected in test_cases:
        assert Solution().smallestBalancedIndex(*args) == expected
