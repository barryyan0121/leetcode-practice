class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        counts = [0] * 24
        pairs = 0
        for hour in hours:
            remainder = hour % 24
            pairs += counts[(-remainder) % 24]
            counts[remainder] += 1
        return pairs


if __name__ == "__main__":
    test_cases = [([12, 12, 30, 24, 24], 2), ([72, 48, 24, 3], 3)]
    for _, (hours, expected) in enumerate(test_cases):
        assert Solution().countCompleteDayPairs(hours) == expected
