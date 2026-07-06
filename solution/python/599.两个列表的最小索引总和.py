#
# @lc app=leetcode.cn id=599 lang=python3
# @lcpr version=30203
#
# [599] 两个列表的最小索引总和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {name: i for i, name in enumerate(list1)}
        best = len(list1) + len(list2)
        ans = []

        for j, name in enumerate(list2):
            if name not in index:
                continue
            total = index[name] + j
            if total < best:
                best = total
                ans = [name]
            elif total == best:
                ans.append(name)

        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findRestaurant,
            (["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]),
            ["Shogun"],
        ),
        (
            solution.findRestaurant,
            (["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]),
            ["Shogun"],
        ),
        (solution.findRestaurant, (["happy", "sad", "good"], ["sad", "happy", "good"]), ["sad", "happy"]),
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
# ["Shogun","Tapioca Express","Burger King","KFC"]\n["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]\n
# @lcpr case=end

# @lcpr case=start
# ["Shogun","Tapioca Express","Burger King","KFC"]\n["KFC","Shogun","Burger King"]\n
# @lcpr case=end

#
