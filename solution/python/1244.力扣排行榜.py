class Leaderboard:
    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, k: int) -> int:
        return sum(sorted(self.scores.values(), reverse=True)[:k])

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]


if __name__ == "__main__":
    test_cases = [((), 73)]
    for _, (_, expected) in enumerate(test_cases):
        leaderboard = Leaderboard()
        for player_id, score in ((1, 73), (2, 56), (3, 39), (4, 51), (5, 4)):
            leaderboard.addScore(player_id, score)
        assert leaderboard.top(1) == expected
