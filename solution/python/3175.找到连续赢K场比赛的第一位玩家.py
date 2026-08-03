class Solution:
    def findWinningPlayer(self, skills: list[int], k: int) -> int:
        winner = 0
        wins = 0
        for index, skill in enumerate(skills[1:], 1):
            if skills[winner] < skill:
                winner = index
                wins = 0
            wins += 1
            if wins == k:
                return winner
        return winner


if __name__ == "__main__":
    test_cases = [(([4, 2, 6, 3, 9], 2), 2), (([2, 5, 4], 3), 1)]
    for _, ((skills, k), expected) in enumerate(test_cases):
        assert Solution().findWinningPlayer(skills, k) == expected
