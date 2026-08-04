"""3551. 数位和排序需要的最小交换次数"""


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        target = sorted(nums, key=lambda value: (sum(map(int, str(value))), value))
        position = {value: index for index, value in enumerate(nums)}
        swaps = 0
        for index, value in enumerate(target):
            if nums[index] == value:
                continue
            other = position[value]
            position[nums[index]] = other
            position[value] = index
            nums[index], nums[other] = nums[other], nums[index]
            swaps += 1
        return swaps


if __name__ == "__main__":
    test_cases = [
        (([37, 100],), 1),
        (([22, 14, 33, 7],), 0),
        (([18, 43, 34, 16],), 2),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().minSwaps(nums) == expected
