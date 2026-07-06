#
# @lc app=leetcode.cn id=608 lang=python3
# @lcpr version=30203
#
# [608] 树节点
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def treeNode(self, tree: List[Dict[str, Optional[int]]]) -> List[Dict[str, str]]:
        parents = {row["p_id"] for row in tree if row["p_id"] is not None}
        result = []
        for row in tree:
            if row["p_id"] is None:
                node_type = "Root"
            elif row["id"] in parents:
                node_type = "Inner"
            else:
                node_type = "Leaf"
            result.append({"id": row["id"], "type": node_type})
        return sorted(result, key=lambda row: row["id"])


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.treeNode,
            (
                [
                    {"id": 1, "p_id": None},
                    {"id": 2, "p_id": 1},
                    {"id": 3, "p_id": 1},
                    {"id": 4, "p_id": 2},
                    {"id": 5, "p_id": 2},
                ],
            ),
            [
                {"id": 1, "type": "Root"},
                {"id": 2, "type": "Inner"},
                {"id": 3, "type": "Leaf"},
                {"id": 4, "type": "Leaf"},
                {"id": 5, "type": "Leaf"},
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
# Tree table\n
# @lcpr case=end
