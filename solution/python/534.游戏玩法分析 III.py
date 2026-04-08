#
# @lc app=leetcode.cn id=534 lang=python3
# @lcpr version=30203
#
# [534] 游戏玩法分析 III
#

import sys
import os
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def gamePlayAnalysis3(
        self, activity: List[Dict[str, Any]]
    ) -> List[Dict[str, Union[int, str]]]:
        daily = defaultdict(lambda: defaultdict(int))
        for row in activity:
            daily[row["player_id"]][row["event_date"]] += row["games_played"]

        result = []
        for player_id in sorted(daily):
            running = 0
            for event_date in sorted(daily[player_id]):
                running += daily[player_id][event_date]
                result.append(
                    {
                        "player_id": player_id,
                        "event_date": event_date,
                        "games_played_so_far": running,
                    }
                )
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.gamePlayAnalysis3,
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
                        "player_id": 1,
                        "device_id": 3,
                        "event_date": "2016-05-02",
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
            [
                {
                    "player_id": 1,
                    "event_date": "2016-03-01",
                    "games_played_so_far": 5,
                },
                {
                    "player_id": 1,
                    "event_date": "2016-05-02",
                    "games_played_so_far": 12,
                },
                {
                    "player_id": 3,
                    "event_date": "2016-03-02",
                    "games_played_so_far": 0,
                },
            ],
        ),
        (
            solution.gamePlayAnalysis3,
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
            [
                {
                    "player_id": 2,
                    "event_date": "2017-01-01",
                    "games_played_so_far": 0,
                }
            ],
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
