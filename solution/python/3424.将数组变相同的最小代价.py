class Solution:
    def minCost(self, arr: list[int], brr: list[int], k: int) -> int:
        direct = sum(abs(left - right) for left, right in zip(arr, brr))
        reordered = k + sum(
            abs(left - right) for left, right in zip(sorted(arr), sorted(brr))
        )
        return min(direct, reordered)


if __name__ == "__main__":
    test_cases = [
        (([-7, 9, 5], [7, -2, -5], 2), 13),
        (([2, 1], [2, 1], 0), 0),
    ]
    for _, ((arr, brr, k), expected) in enumerate(test_cases):
        assert Solution().minCost(arr, brr, k) == expected
