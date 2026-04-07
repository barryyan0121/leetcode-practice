#
# @lc app=leetcode.cn id=457 lang=python3
# @lcpr version=30203
#
# [457] 环形数组是否存在循环
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue
            slow = fast = i
            direction = nums[i] > 0

            while True:
                next_slow = next_index(slow)
                next_fast = next_index(fast)
                next_fast2 = next_index(next_fast)

                if (
                    nums[slow] == 0
                    or nums[fast] == 0
                    or nums[next_fast] == 0
                    or (nums[next_slow] > 0) != direction
                    or (nums[next_fast] > 0) != direction
                    or (nums[next_fast2] > 0) != direction
                ):
                    break

                slow = next_slow
                fast = next_fast2

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            mark = i
            while nums[mark] != 0 and (nums[mark] > 0) == direction:
                nxt = next_index(mark)
                nums[mark] = 0
                mark = nxt

        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.circularArrayLoop, ([2, -1, 1, 2, 2],), True),
        (solution.circularArrayLoop, ([-1, 2],), False),
        (solution.circularArrayLoop, ([-2, 1, -1, -2, -2],), False),
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
# [2,-1,1,2,2]\n
# @lcpr case=end
