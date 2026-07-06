#
# @lc app=leetcode.cn id=602 lang=python3
# @lcpr version=30203
#
# [602] 好友申请 II ：谁有最多的好友
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def mostFriends(self, request_accepted: List[Dict[str, int]]) -> Dict[str, int]:
        count = Counter()
        for row in request_accepted:
            count[row["requester_id"]] += 1
            count[row["accepter_id"]] += 1
        user_id, num = max(count.items(), key=lambda item: item[1])
        return {"id": user_id, "num": num}


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.mostFriends,
            (
                [
                    {"requester_id": 1, "accepter_id": 2, "accept_date": "2016/06/03"},
                    {"requester_id": 1, "accepter_id": 3, "accept_date": "2016/06/08"},
                    {"requester_id": 2, "accepter_id": 3, "accept_date": "2016/06/08"},
                    {"requester_id": 3, "accepter_id": 4, "accept_date": "2016/06/09"},
                ],
            ),
            {"id": 3, "num": 3},
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
# RequestAccepted table\n
# @lcpr case=end
