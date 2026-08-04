class Solution:
    def maximumTotalSum(self, maximumHeight: list[int]) -> int:
        total = 0
        next_height = float("inf")
        for limit in sorted(maximumHeight, reverse=True):
            height = min(limit, next_height - 1)
            if height <= 0:
                return -1
            total += height
            next_height = height
        return total


if __name__ == "__main__":
    test_cases = [
        (([2, 3, 4, 3],), 10),
        (([15, 10],), 25),
        (([2, 2, 1],), -1),
    ]
    for _, ((maximum_height,), expected) in enumerate(test_cases):
        assert Solution().maximumTotalSum(maximum_height) == expected
