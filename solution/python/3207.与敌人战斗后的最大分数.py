class Solution:
    def maximumPoints(self, enemyEnergies: list[int], currentEnergy: int) -> int:
        minimum = min(enemyEnergies)
        if currentEnergy < minimum:
            return 0
        return (sum(enemyEnergies) + currentEnergy) // minimum - 1


if __name__ == "__main__":
    test_cases = [(([3, 2, 2], 2), 3), (([2], 10), 5), (([5, 6], 4), 0)]
    for _, ((enemy_energies, current_energy), expected) in enumerate(test_cases):
        assert Solution().maximumPoints(enemy_energies, current_energy) == expected
