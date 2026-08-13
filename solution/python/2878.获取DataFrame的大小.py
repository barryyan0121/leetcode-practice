import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return [players.shape[0], players.shape[1]]


class Solution:
    def getDataframeSize(self, players: pd.DataFrame) -> list[int]:
        return getDataframeSize(players)


if __name__ == "__main__":
    test_cases = [
        (pd.DataFrame({"player_id": [1, 2, 3], "name": ["A", "B", "C"]}), [3, 2])
    ]

    solver = Solution()
    for index, (players, expected) in enumerate(test_cases):
        actual = solver.getDataframeSize(players)
        assert actual == expected, f"case {index} failed"
