class Solution:
    def earliestSecondToMarkIndices(
        self, nums: list[int], changeIndices: list[int]
    ) -> int:
        def feasible(seconds: int) -> bool:
            last = [-1] * len(nums)
            for time in range(seconds):
                last[changeIndices[time] - 1] = time
            if -1 in last:
                return False
            available = 0
            for time in range(seconds):
                index = changeIndices[time] - 1
                if last[index] == time:
                    if available < nums[index]:
                        return False
                    available -= nums[index]
                else:
                    available += 1
            return True

        left, right = 1, len(changeIndices)
        if not feasible(right):
            return -1
        while left < right:
            middle = (left + right) // 2
            if feasible(middle):
                right = middle
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    test_cases = [
        (([2, 2, 0], [2, 2, 2, 2, 3, 2, 2, 1]), 8),
        (([1, 3], [1, 1, 1, 2, 1, 1, 1]), 6),
        (([0, 1], [2, 2, 2]), -1),
    ]
    for _, ((nums, change_indices), expected) in enumerate(test_cases):
        assert Solution().earliestSecondToMarkIndices(nums, change_indices) == expected
