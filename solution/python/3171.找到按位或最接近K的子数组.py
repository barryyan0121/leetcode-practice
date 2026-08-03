class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        answer = abs(nums[0] - k)
        previous = set()
        for number in nums:
            current = {number}
            current.update(value | number for value in previous)
            answer = min(answer, *(abs(value - k) for value in current))
            previous = current
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 4, 5], 3), 0),
        (([1, 3, 1, 3], 2), 1),
        (([1], 10), 9),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minimumDifference(nums, k) == expected
