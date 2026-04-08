#
# @lc app=leetcode.cn id=550 lang=python3
# @lcpr version=30203
#
# [550] 游戏玩法分析 IV
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def gamePlayAnalysis4(self, activity: List[Dict[str, Any]]) -> float:
        first_login: Dict[int, str] = {}
        next_day_login: set[int] = set()
        for row in activity:
            player_id = row["player_id"]
            event_date = row["event_date"]
            if player_id not in first_login or event_date < first_login[player_id]:
                first_login[player_id] = event_date

        def next_day(date: str) -> str:
            from datetime import datetime, timedelta

            dt = datetime.strptime(date, "%Y-%m-%d")
            return (dt + timedelta(days=1)).strftime("%Y-%m-%d")

        login_days = {(row["player_id"], row["event_date"]) for row in activity}
        for player_id, first in first_login.items():
            if (player_id, next_day(first)) in login_days:
                next_day_login.add(player_id)

        if not first_login:
            return 0.0
        return round(len(next_day_login) / len(first_login), 2)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.gamePlayAnalysis4,
            (
                [
                    {
                        "player_id": 1,
                        "device_id": 2,
                        "event_date": "2016-03-01",
                        "games_played": 5,
                    },
                    {
                        "player_id": 1,
                        "device_id": 2,
                        "event_date": "2016-03-02",
                        "games_played": 6,
                    },
                    {
                        "player_id": 2,
                        "device_id": 3,
                        "event_date": "2017-06-25",
                        "games_played": 1,
                    },
                    {
                        "player_id": 2,
                        "device_id": 3,
                        "event_date": "2017-06-26",
                        "games_played": 1,
                    },
                    {
                        "player_id": 3,
                        "device_id": 1,
                        "event_date": "2016-03-02",
                        "games_played": 0,
                    },
                ],
            ),
            0.67,
        ),
        (
            solution.gamePlayAnalysis4,
            (
                [
                    {
                        "player_id": 1,
                        "device_id": 1,
                        "event_date": "2016-03-01",
                        "games_played": 0,
                    }
                ],
            ),
            0.0,
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert abs(result - expected) < 1e-9
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# Activity = Activity table\n
# @lcpr case=end
#
