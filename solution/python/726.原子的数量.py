#
# @lc app=leetcode.cn id=726 lang=python3
#
# [726] 原子的数量
#

import os
import sys
from collections import Counter


# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        index = 0

        def number() -> int:
            nonlocal index
            start = index
            while index < len(formula) and formula[index].isdigit():
                index += 1
            return int(formula[start:index] or 1)

        while index < len(formula):
            if formula[index] == "(":
                stack.append(Counter())
                index += 1
            elif formula[index] == ")":
                index += 1
                group = stack.pop()
                multiplier = number()
                for atom, count in group.items():
                    stack[-1][atom] += count * multiplier
            else:
                start = index
                index += 1
                while index < len(formula) and formula[index].islower():
                    index += 1
                stack[-1][formula[start:index]] += number()

        return "".join(
            atom + (str(count) if count > 1 else "")
            for atom, count in sorted(stack[0].items())
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countOfAtoms, ("H2O",), "H2O"),
        (solution.countOfAtoms, ("Mg(OH)2",), "H2MgO2"),
        (solution.countOfAtoms, ("K4(ON(SO3)2)2",), "K4N2O14S4"),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
