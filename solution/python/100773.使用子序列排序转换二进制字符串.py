#
# @lc app=leetcode.cn id=100773 lang=python3
#
# [100773] 使用子序列排序转换二进制字符串
#

import os
import sys


# @lc code=start
class Solution:
    def transformStr(self, s: str, strs: list[str]) -> list[bool]:
        veltromina = (s, strs)
        prefix = []
        ones = 0
        for char in veltromina[0]:
            ones += char == "1"
            prefix.append(ones)

        answer = []
        for pattern in veltromina[1]:
            need = ones - pattern.count("1")
            if not 0 <= need <= pattern.count("?"):
                answer.append(False)
                continue

            assigned = 0
            result = True
            remaining = pattern.count("?")
            for i, char in enumerate(pattern):
                if char == "1":
                    assigned += 1
                elif char == "?":
                    remaining -= 1
                    if need > remaining:
                        assigned += 1
                        need -= 1
                if assigned > prefix[i]:
                    result = False
                    break
            answer.append(result)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.transformStr,
            ("101", ["1?1", "0?1", "0?0"]),
            [True, True, False],
        ),
        (
            solution.transformStr,
            ("1100", ["0011", "11?1", "1?1?"]),
            [True, False, True],
        ),
        (solution.transformStr, ("1010", ["0011"]), [True]),
        (solution.transformStr, ("0011", ["?1?0", "??11"]), [False, True]),
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
