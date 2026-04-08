#
# @lc app=leetcode.cn id=513 lang=python3
# @lcpr version=30203
#
# [513] 找树左下角的值
#

import sys
import os
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        bottom_left = root.val

        while queue:
            bottom_left = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return bottom_left


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (solution.findBottomLeftValue, (TreeNode.create_root([2, 1, 3]),), 1),
        (
            solution.findBottomLeftValue,
            (TreeNode.create_root([1, 2, 3, 4, None, 5, 6, None, None, 7]),),
            7,
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
# root = [2,1,3]\n
# @lcpr case=end
#
