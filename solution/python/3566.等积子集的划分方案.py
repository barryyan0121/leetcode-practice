"""3566. 等积子集的划分方案"""


class Solution:
    def checkEqualPartitions(self, nums: list[int], target: int) -> bool:
        total = 1
        for value in nums:
            total *= value
        if total != target * target:
            return False

        n = len(nums)
        for mask in range(1, (1 << n) - 1):
            product = 1
            for index, value in enumerate(nums):
                if mask >> index & 1:
                    product *= value
                    if product > target:
                        break
            if product == target:
                return True
        return False


if __name__ == "__main__":
    test_cases = [
        (([3, 1, 6, 8, 4], 24), True),
        (([2, 5, 3, 7], 15), False),
    ]
    for _, ((nums, target), expected) in enumerate(test_cases):
        assert Solution().checkEqualPartitions(nums, target) == expected
