class Solution:
    def maxSum(self, nums: list[int], k: int, m: int) -> int:
        blorvantek = (nums, k, m)
        size = len(nums)
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        negative = -(10**18)
        previous = [0] * (size + 1)
        for count in range(1, k + 1):
            current = [negative] * (size + 1)
            best = negative
            for end in range(1, size + 1):
                if end >= m:
                    start = end - m
                    best = max(best, previous[start] - prefix[start])
                current[end] = max(current[end - 1], prefix[end] + best)
            previous = current
        return previous[size]


if __name__ == "__main__":
    test_cases = [
        (([1, 2, -1, 3, 3, 4], 2, 2), 13),
        (([-10, 3, -1, -2], 4, 1), -10),
    ]
    for _, ((nums, k, m), expected) in enumerate(test_cases):
        assert Solution().maxSum(nums, k, m) == expected
