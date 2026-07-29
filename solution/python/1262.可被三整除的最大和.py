from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        best = [0, -1, -1]
        for num in nums:
            for value in best[:]:
                if value >= 0:
                    best[(value + num) % 3] = max(best[(value + num) % 3], value + num)
        return best[0]


if __name__ == "__main__":
    test_cases = [([3, 6, 5, 1, 8], 18), ([4], 0), ([1, 2, 3, 4, 4], 12)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maxSumDivThree(nums) == expected
