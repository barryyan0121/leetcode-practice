from functools import cache


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        suffix = [0] * (len(piles) + 1)
        for index in range(len(piles) - 1, -1, -1):
            suffix[index] = suffix[index + 1] + piles[index]

        @cache
        def dfs(index, maximum):
            if index + 2 * maximum >= len(piles):
                return suffix[index]
            return max(
                suffix[index] - dfs(index + take, max(maximum, take))
                for take in range(1, 2 * maximum + 1)
            )

        return dfs(0, 1)


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 9, 4, 4], 10),
        ([1, 2, 3, 4, 5, 100], 104),
        ([1], 1),
        ([1, 2], 3),
    ]
    for _, (piles, expected) in enumerate(test_cases):
        assert Solution().stoneGameII(piles) == expected
