class Solution:
    def minMaxSums(self, nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        combinations = [1] + [0] * (k - 1)
        answer = 0
        for index, value in enumerate(nums):
            count = sum(combinations[: min(k, index + 1)]) % mod
            answer = (answer + (value + nums[-index - 1]) * count) % mod
            for length in range(min(k - 1, index + 1), 0, -1):
                combinations[length] = (
                    combinations[length] + combinations[length - 1]
                ) % mod
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], 2), 24),
        (([5, 0, 6], 1), 22),
        (([1, 1, 1], 2), 12),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minMaxSums(nums, k) == expected
