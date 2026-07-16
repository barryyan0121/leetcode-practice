#
# @lc app=leetcode.cn id=984 lang=python3
#
# [984] 不含 AAA 或 BBB 的字符串
#

import os
import sys


# @lc code=start
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        while a or b:
            if len(result) >= 2 and result[-2:] == ["a", "a"]:
                letter = "b"
            elif len(result) >= 2 and result[-2:] == ["b", "b"]:
                letter = "a"
            else:
                letter = "a" if a >= b else "b"
            result.append(letter)
            if letter == "a":
                a -= 1
            else:
                b -= 1
        return "".join(result)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.strWithout3a3b, (1, 2), (1, 2)),
        (solution.strWithout3a3b, (4, 1), (4, 1)),
        (solution.strWithout3a3b, (3, 3), (3, 3)),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result.count("a") == expected[0]
            assert result.count("b") == expected[1]
            assert "aaa" not in result and "bbb" not in result
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 实际 = {result}")
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
