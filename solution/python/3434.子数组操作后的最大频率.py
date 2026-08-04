class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nerbalithy = (nums, k)
        answer = nums.count(k)
        for value in range(1, 51):
            if value == k:
                continue
            best = current = 0
            for number in nums:
                current = max(0, current + (number == value) - (number == k))
                best = max(best, current)
            answer = max(answer, nums.count(k) + best)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5, 6], 1), 2),
        (([10, 2, 3, 4, 5, 5, 4, 3, 2, 2], 10), 4),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().maxFrequency(nums, k) == expected
