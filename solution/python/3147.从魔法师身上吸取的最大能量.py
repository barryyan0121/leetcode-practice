class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        best = energy[:]
        for index in range(len(energy) - k - 1, -1, -1):
            best[index] += best[index + k]
        return max(best)


if __name__ == "__main__":
    test_cases = [([5, 2, -10, -5, 1], 3, 3), ([-2, -3, -1], 2, -1)]
    for _, (energy, k, expected) in enumerate(test_cases):
        assert Solution().maximumEnergy(energy, k) == expected
