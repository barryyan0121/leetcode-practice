class Solution:
    def maxEnergyBoost(self, energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        n = len(energyDrinkA)
        best_a = [0] * n
        best_b = [0] * n
        best_a[0], best_b[0] = energyDrinkA[0], energyDrinkB[0]
        for hour in range(1, n):
            best_a[hour] = best_a[hour - 1] + energyDrinkA[hour]
            best_b[hour] = best_b[hour - 1] + energyDrinkB[hour]
            if hour >= 2:
                best_a[hour] = max(best_a[hour], best_b[hour - 2] + energyDrinkA[hour])
                best_b[hour] = max(best_b[hour], best_a[hour - 2] + energyDrinkB[hour])
            else:
                best_a[hour] = max(best_a[hour], energyDrinkA[hour])
                best_b[hour] = max(best_b[hour], energyDrinkB[hour])
        return max(best_a[-1], best_b[-1])


if __name__ == "__main__":
    test_cases = [
        (([1, 3, 1], [3, 1, 1]), 5),
        (([4, 1, 1], [1, 1, 3]), 7),
    ]
    for _, ((energy_a, energy_b), expected) in enumerate(test_cases):
        assert Solution().maxEnergyBoost(energy_a, energy_b) == expected
