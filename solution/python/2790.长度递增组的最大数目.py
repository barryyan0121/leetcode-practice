class Solution:
    def maxIncreasingGroups(self, usageLimits: list[int]) -> int:
        total = groups = 0
        for value in sorted(usageLimits):
            total += value
            if total >= (groups + 1) * (groups + 2) // 2:
                groups += 1
        return groups


if __name__ == "__main__":
    assert Solution().maxIncreasingGroups([1, 2, 5]) == 3
