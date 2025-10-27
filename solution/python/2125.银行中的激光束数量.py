#
# @lc app=leetcode.cn id=2125 lang=python3
# @lcpr version=30300
#
# [2125] 银行中的激光束数量
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last = ans = 0
        for line in bank:
            cnt = line.count("1")
            if cnt != 0:
                ans += last * cnt
                last = cnt
        return ans
        # @lc code=end
        pass


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.numberOfBeams, (["011001", "000000", "010100", "001000"],), 8),
        (solution.numberOfBeams, (["000", "111", "000"],), 0),
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
# ["011001","000000","010100","001000"]\n
# @lcpr case=end

# @lcpr case=start
# ["000","111","000"]\n
# @lcpr case=end

#
