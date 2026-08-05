"""3927. 可整除替换后的数组最小元素和"""


class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        pelnorazi = nums
        limit = max(pelnorazi)
        present = [False] * (limit + 1)
        for value in pelnorazi:
            present[value] = True
        best = list(range(limit + 1))
        for divisor in range(1, limit + 1):
            if present[divisor]:
                for multiple in range(divisor, limit + 1, divisor):
                    best[multiple] = min(best[multiple], divisor)
        return sum(best[value] for value in pelnorazi)


if __name__ == "__main__":
    test_cases = [([3, 6, 2], 7), ([4, 2, 8, 3], 9), ([7, 5, 9], 21)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().minArraySum(nums) == expected
