#
# @lc app=leetcode.cn id=314 lang=python3
# @lcpr version=30203
#
# [314] 二叉树的垂直遍历
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import deque, defaultdict
from common.node import *


# @lc code=start
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        col_map = defaultdict(list)
        queue = deque([(root, 0)])
        min_col = max_col = 0

        while queue:
            node, col = queue.popleft()
            col_map[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [col_map[c] for c in range(min_col, max_col + 1)]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.verticalOrder,
            (TreeNode.create_root([3, 9, 20, None, None, 15, 7]),),
            [[9], [3, 15], [20], [7]],
        ),
        (
            solution.verticalOrder,
            (TreeNode.create_root([3, 9, 8, 4, 0, 1, 7]),),
            [[4], [9], [3, 0, 1], [8], [7]],
        ),
        (solution.verticalOrder, (None,), []),
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
# [3,9,20,null,null,15,7]\n
# @lcpr case=end
