class Solution:
    def medianOfUniquenessArray(self, nums: list[int]) -> int:
        total = len(nums) * (len(nums) + 1) // 2
        target = (total + 1) // 2

        def count_at_most(limit: int) -> int:
            counts = {}
            left = 0
            total_subarrays = 0
            for right, value in enumerate(nums):
                counts[value] = counts.get(value, 0) + 1
                while len(counts) > limit:
                    counts[nums[left]] -= 1
                    if counts[nums[left]] == 0:
                        del counts[nums[left]]
                    left += 1
                total_subarrays += right - left + 1
            return total_subarrays

        left, right = 1, len(set(nums))
        while left < right:
            middle = (left + right) // 2
            if count_at_most(middle) >= target:
                right = middle
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    test_cases = [([1, 2, 3], 1), ([3, 4, 3, 4, 5], 2), ([4, 3, 5, 4], 2)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().medianOfUniquenessArray(nums) == expected
