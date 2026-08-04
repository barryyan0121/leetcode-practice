class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        delta = [0] * (k + 2)
        for left, right in zip(nums[: len(nums) // 2], reversed(nums)):
            low, high = sorted((left, right))
            difference = high - low
            one_change_limit = max(high, k - low)
            delta[0] += 1
            delta[one_change_limit + 1] += 1
            delta[difference] -= 1
            delta[difference + 1] += 1

        answer = len(nums)
        changes = 0
        for target in range(k + 1):
            changes += delta[target]
            answer = min(answer, changes)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 0, 1, 2, 4, 3], 4), 2), (([0, 1, 2, 3, 3, 6, 5, 4], 6), 2)]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minChanges(nums, k) == expected
