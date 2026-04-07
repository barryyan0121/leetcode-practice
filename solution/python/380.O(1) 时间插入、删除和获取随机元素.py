#
# @lc app=leetcode.cn id=380 lang=python3
# @lcpr version=30203
#
# [380] O(1) 时间插入、删除和获取随机元素
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
import random
from common.node import *


# @lc code=start
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.pos[last] = idx
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
        # @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    test_cases = [
        (
            [
                ("init", []),
                ("insert", [1]),
                ("remove", [2]),
                ("insert", [2]),
                ("getRandom", []),
                ("remove", [1]),
                ("insert", [2]),
                ("getRandom", []),
            ],
            [None, True, False, True, {1, 2}, True, False, {2}],
        ),
        (
            [
                ("init", []),
                ("insert", [1]),
                ("insert", [1]),
                ("remove", [1]),
                ("remove", [1]),
            ],
            [None, True, False, True, False],
        ),
    ]

    all_passed = True
    for idx, (ops, expected) in enumerate(test_cases):
        try:
            result = []
            obj = None
            orig_choice = random.choice
            random.choice = lambda seq: seq[0]
            for op, args in ops:
                if op == "init":
                    obj = RandomizedSet()
                    result.append(None)
                elif op == "insert":
                    result.append(obj.insert(*args))
                elif op == "remove":
                    result.append(obj.remove(*args))
                else:
                    result.append(obj.getRandom())
            random.choice = orig_choice
            if isinstance(expected[4], set):
                assert result[4] in expected[4]
                assert result[7] in expected[7]
                result_cmp = result
            else:
                assert result == expected
                result_cmp = result
            print(f"测试用例 {idx + 1} 通过: n = {ops}, result = {result_cmp}")
        except AssertionError:
            random.choice = orig_choice
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {ops}, 期望 = {expected}, 实际 = {result}"
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
# ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n[[],[1],[2],[2],[],[1],[2],[]]\n
# @lcpr case=end

#
