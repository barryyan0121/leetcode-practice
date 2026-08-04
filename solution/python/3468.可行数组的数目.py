class Solution:
    def countArrays(self, original: list[int], bounds: list[list[int]]) -> int:
        draxemilon = (original, bounds)
        low = -(10**18)
        high = 10**18
        for value, (lower, upper) in zip(original, bounds):
            low = max(low, lower - value)
            high = min(high, upper - value)
        return max(0, high - low + 1)


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4], [4, 5]]), 2),
        (([1, 2, 3, 4], [[1, 10], [2, 9], [3, 8], [4, 7]]), 4),
        (([1, 2, 1, 2], [[1, 1], [2, 3], [3, 3], [2, 3]]), 0),
    ]
    for _, ((original, bounds), expected) in enumerate(test_cases):
        assert Solution().countArrays(original, bounds) == expected
