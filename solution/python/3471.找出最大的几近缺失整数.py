class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        draxemilon = (nums, k)
        occurrences = {value: 0 for value in set(nums)}
        for start in range(len(nums) - k + 1):
            for value in set(nums[start : start + k]):
                occurrences[value] += 1
        candidates = [value for value, count in occurrences.items() if count == 1]
        return max(candidates, default=-1)


if __name__ == "__main__":
    test_cases = [
        (([3, 9, 2, 1, 7], 3), 7),
        (([3, 9, 7, 2, 1, 7], 4), 3),
        (([0, 0], 1), -1),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().largestInteger(nums, k) == expected
