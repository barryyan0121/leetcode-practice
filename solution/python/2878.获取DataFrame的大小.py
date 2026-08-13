"""2878. 获取DataFrame的大小"""

import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return [players.shape[0], players.shape[1]]


if __name__ == "__main__":
    players = pd.DataFrame({"player_id": [1, 2, 3], "name": ["A", "B", "C"]})
    assert getDataframeSize(players) == [3, 2]
    print("测试用例通过")
