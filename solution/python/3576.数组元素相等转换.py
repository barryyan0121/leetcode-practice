"""3576. 数组元素相等转换"""


class Solution:
    def canMakeEqual(self, nums: list[int], k: int) -> bool:
        for target in (1, -1):
            flips = 0
            sign = 1
            for index in range(len(nums) - 1):
                if nums[index] * sign != target:
                    flips += 1
                    sign = -1
                else:
                    sign = 1
            if nums[-1] * sign == target and flips <= k:
                return True
        return False


if __name__ == "__main__":
    test_cases = [
        (([1, -1, 1, -1, 1], 3), True),
        (([-1, -1, -1, 1, 1, 1], 5), False),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().canMakeEqual(nums, k) == expected
