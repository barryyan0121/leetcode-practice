#
# @lc app=leetcode.cn id=262 lang=python3
# @lcpr version=30203
#
# [262] 行程和用户
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def tripsAndUsers(
        self, trips: List[Dict[str, Any]], users: List[Dict[str, Any]]
    ) -> List[Dict[str, str]]:
        banned = {row["users_id"] for row in users if row["banned"] == "Yes"}
        days = ["2013-10-01", "2013-10-02", "2013-10-03"]
        result = []

        for day in days:
            current = [
                trip
                for trip in trips
                if trip["request_at"] == day
                and trip["client_id"] not in banned
                and trip["driver_id"] not in banned
            ]
            cancelled = [
                trip
                for trip in current
                if trip["status"] in ("cancelled_by_driver", "cancelled_by_client")
            ]
            rate = len(cancelled) / len(current) if current else 0
            result.append({"Day": day, "Cancellation Rate": f"{rate:.2f}"})

        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    trips = [
        {
            "id": 1,
            "client_id": 1,
            "driver_id": 10,
            "city_id": 1,
            "status": "completed",
            "request_at": "2013-10-01",
        },
        {
            "id": 2,
            "client_id": 2,
            "driver_id": 11,
            "city_id": 1,
            "status": "cancelled_by_driver",
            "request_at": "2013-10-01",
        },
        {
            "id": 3,
            "client_id": 3,
            "driver_id": 12,
            "city_id": 6,
            "status": "completed",
            "request_at": "2013-10-01",
        },
        {
            "id": 4,
            "client_id": 4,
            "driver_id": 13,
            "city_id": 6,
            "status": "cancelled_by_client",
            "request_at": "2013-10-01",
        },
        {
            "id": 5,
            "client_id": 1,
            "driver_id": 10,
            "city_id": 1,
            "status": "completed",
            "request_at": "2013-10-02",
        },
        {
            "id": 6,
            "client_id": 2,
            "driver_id": 11,
            "city_id": 6,
            "status": "completed",
            "request_at": "2013-10-02",
        },
        {
            "id": 7,
            "client_id": 3,
            "driver_id": 12,
            "city_id": 6,
            "status": "completed",
            "request_at": "2013-10-02",
        },
        {
            "id": 8,
            "client_id": 2,
            "driver_id": 12,
            "city_id": 12,
            "status": "completed",
            "request_at": "2013-10-03",
        },
        {
            "id": 9,
            "client_id": 3,
            "driver_id": 10,
            "city_id": 12,
            "status": "completed",
            "request_at": "2013-10-03",
        },
        {
            "id": 10,
            "client_id": 4,
            "driver_id": 13,
            "city_id": 12,
            "status": "cancelled_by_driver",
            "request_at": "2013-10-03",
        },
    ]
    users = [
        {"users_id": 1, "banned": "No", "role": "client"},
        {"users_id": 2, "banned": "Yes", "role": "client"},
        {"users_id": 3, "banned": "No", "role": "client"},
        {"users_id": 4, "banned": "No", "role": "client"},
        {"users_id": 10, "banned": "No", "role": "driver"},
        {"users_id": 11, "banned": "No", "role": "driver"},
        {"users_id": 12, "banned": "No", "role": "driver"},
        {"users_id": 13, "banned": "No", "role": "driver"},
    ]

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.tripsAndUsers,
            (trips, users),
            [
                {"Day": "2013-10-01", "Cancellation Rate": "0.33"},
                {"Day": "2013-10-02", "Cancellation Rate": "0.00"},
                {"Day": "2013-10-03", "Cancellation Rate": "0.50"},
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
# trips = Trips table, users = Users table\n
# @lcpr case=end
