class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        answer = None
        for start in range(len(nums)):
            total = 0
            for end in range(start, min(len(nums), start + r)):
                total += nums[end]
                if end - start + 1 >= l and total > 0:
                    answer = total if answer is None else min(answer, total)
        return -1 if answer is None else answer


if __name__ == "__main__":
    test_cases = [
        (([3, -2, 1, 4], 2, 3), 1),
        (([-1, -2, -3], 1, 2), -1),
        (([1, 2, 3], 1, 2), 1),
    ]
    for _, ((nums, l, r), expected) in enumerate(test_cases):
        assert Solution().minimumSumSubarray(nums, l, r) == expected
