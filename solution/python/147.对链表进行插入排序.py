#
# @lc app=leetcode.cn id=147 lang=python3
# @lcpr version=30202
#
# [147] 对链表进行插入排序
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = head
        while curr:
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            nxt = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = nxt
        return dummy.next
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.insertionSortList,
            [ListNode.create_head([4, 2, 1, 3])],
            "1 -> 2 -> 3 -> 4",
        ),
        (
            solution.insertionSortList,
            [ListNode.create_head([-1, 5, 3, 4, 0])],
            "-1 -> 0 -> 3 -> 4 -> 5",
        ),
        (solution.insertionSortList, [ListNode.create_head([])], ""),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            result_text = ListNode.print(result)
            assert result_text == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result_text}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result_text}"
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
# [4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,5,3,4,0]\n
# @lcpr case=end

#
