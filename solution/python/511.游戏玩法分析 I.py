#
# @lc app=leetcode.cn id=511 lang=python3
# @lcpr version=30203
#
# [511] 游戏玩法分析 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def gamePlayAnalysis(
        self, activity: List[Dict[str, Any]]
    ) -> List[Dict[str, Union[int, str]]]:
        first_login: Dict[int, str] = {}
        for row in activity:
            player_id = row["player_id"]
            event_date = row["event_date"]
            if player_id not in first_login or event_date < first_login[player_id]:
                first_login[player_id] = event_date

        return [
            {"player_id": player_id, "first_login_date": first_login[player_id]}
            for player_id in sorted(first_login)
        ]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            solution.gamePlayAnalysis,
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
                        "event_date": "2016-05-02",
                        "games_played": 6,
                    },
                    {
                        "player_id": 2,
                        "device_id": 3,
                        "event_date": "2017-06-25",
                        "games_played": 1,
                    },
                    {
                        "player_id": 3,
                        "device_id": 3,
                        "event_date": "2016-03-02",
                        "games_played": 0,
                    },
                ],
            ),
            [
                {"player_id": 1, "first_login_date": "2016-03-01"},
                {"player_id": 2, "first_login_date": "2017-06-25"},
                {"player_id": 3, "first_login_date": "2016-03-02"},
            ],
        ),
        (
            solution.gamePlayAnalysis,
            (
                [
                    {
                        "player_id": 2,
                        "device_id": 1,
                        "event_date": "2017-01-01",
                        "games_played": 0,
                    }
                ],
            ),
            [{"player_id": 2, "first_login_date": "2017-01-01"}],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
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
